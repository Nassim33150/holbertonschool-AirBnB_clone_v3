#!/usr/bin/python3
""" import requests & json"""
from flask import Flask
from flask import jsonify
import requests
import json
from models import storage
from models.state import State
from api.v1.views import app_views
from flask import jsonify, abort
from flask import request


""" Create a new view for State objects """
@app_views.route('/states', methods=['GET'])
def get_states():
    """ Retrieves the list of all State objects """
    states = storage.all(State)
    state_list = []
    for state in states.values():
        state_list.append(state.to_dict())
    return jsonify(state_list)

""" Retrieve a State object """
@app_views.route('/states/<state_id>', methods=['GET'])
def get_state(state_id):
    """ Retrieves a State object """
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    return jsonify(state.to_dict())

""" Delete a State object """
@app_views.route('/states/<state_id>', methods=['DELETE'])
def delete_state(state_id):
    """ Deletes a State object """
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    storage.delete(state)
    storage.save()        
    return jsonify({}), 200

""" Create a new State object """
@app_views.route('/states', methods=['POST'])
def create_state():
    """ Creates a State object """
    state_dict = request.get_json()
    if state_dict is None:
        abort(400, "Not a JSON")
    if "name" not in state_dict:
        return jsonify({"Missing name"}), 400
    return jsonify(storage.new(State(**state_dict)).to_dict()), 201

""" Update a State object """
@app_views.route('/states/<state_id>', methods=['PUT'])
def update_state(state_id):
    """ Updates a State object """
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    state_dict = request.get_json()
    if state_dict is None:
        abort(400, "Not a JSON")
    for key, value in state_dict.items():
        if key not in ['id', 'creates_at', 'updates_at']:
            setattr(state, key, value)

    storage.save()
    return jsonify(state.to_dict()), 200

