#!/usr/bin/python3
""" import requests & json"""
import requests
import json
from models import storage
from models.state import State
from api.v1.views import app_views
from flask import jsonify, abort

""" create a new view for City objects """
@app_views.route('/states/<state_id>/cities', methods=['GET'])
def get_cities(state_id):
    """ Retrieves the list of all City objects """
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    cities = state.cities
    city_list = []
    for city in cities:
        city_list.append(city.to_dict())
    return jsonify(city_list)

""" Retrieve a City object """
@app_views.route('/cities/<city_id>', methods=['GET'])
def get_city(city_id):
    """ Retrieves a City object """
    city = storage.get(City, city_id)
    if city is None:
        abort(404)
    return jsonify(city.to_dict())

""" Delete a City object """
@app_views.route('/cities/<city_id>', methods=['DELETE'])
def delete_city(city_id):
    """ Deletes a City object """
    city = storage.get(City, city_id)
    if city is None:
        abort(404)
    storage.delete(city)
    storage.save()
    return jsonify({}), 200

""" Create a new city object """
@app_views.route('/states/<state_id>/cities', methods=['POST'])
def create_city(state_id):
    """ Creates a City object """
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    city_dict = request.get_json()
    if city_dict is None:
        abort(400, "Not a JSON")
    if "name" not in city_dict:
        return jsonify({"Missing name"}), 400
    city_dict["state_id"] = state_id
    return jsonify(storage.new(City(**city_dict))).to_dict(), 200

""" Update a City object """
@app_views.route('/cities/<city_id>', methods=['PUT'])
def update_city(city_id):
    """ Updates a City object """
    city = storage.get(City, city_id)
    if city is None:
        abort(404)
    city_dict = request.get_json()
    if city_dict is None:
        abort(400, "Not a JSON")
    for key, value in city_dict.items():
        if key not in ['id', 'created_at', 'updated_at']:
            setattr(city, key, value)
    
    storage.save()
    return jsonify(city.to_dict())
