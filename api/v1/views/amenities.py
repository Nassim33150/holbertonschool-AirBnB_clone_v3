#!/usr/bin/python3
""" import requests, JSON & amenity model """
import requests
import json
from models import storage
from models.amenities import Amenity
from api.v1.views import app_views
from flask import jsonify, abort

""" create a new view for Amenity objects """
@app_views.route('/amenities', methods=['GET'])
def get_amenities():
    amenities = storage.all(Amenity)
    amenity_list = []
    for amenity in amenities.values():
        amenity_list.append(amenity.to_dict())
    return jsonify(amenity_list)

""" Retrieve an Amenity object """
@app_views.route('/amenities<amenity_id>', methods=['GET'])
def get_amenity(amenity_id):
    amenity = storage.get(Amenity, amenity_id)
    if amenity is None:
        abort(404)
    return jsonify(amenity.to_dict())

""" Delete an Amenity object """
@app_views.route('/amenities/<amenity_id>', methods=['DELETE'])
def delete_amenity(amenity_id):
    amenity = storage.get(Amenity, amenity_id)
    if amenity is None:
        abort(404)
    storage.delete(amenity)
    storage.save()
    return jsonify({}), 200

""" Create a new Amenity object """
@app_views.route('/amenities', methods=['POST'])
def create_amenity():
    amenity_dict = request.get_json()
    if amenity_dict is None:
        abort(400, "Not a JSON")
    if "name" not in amenity_dict:
        return jsonify({"Missing name"}), 400
    return jsonify(storage.new(Amenity(**amenity_dict))).to_dict(), 200

""" Update an Amenity object """
@app_views.route('/amenities/<amenity_id>', methods=['PUT'])
def update_amenity(amenity_id):
    """ Updates a Amenity object """
    amenity = storage.get(Amenity, amenity_id)
    if amenity is None:
        abort(404)
    amenity_dict = request.get_json()
    if amenity_dict is None:
        abort(400, "Not a JSON")
    for key, value in amenity_dict.items():
        if key not in ['id', 'created_at', 'updated_at']:
            setattr(amenity, key, value)
    
    storage.save()
    return jsonify(amenity.to_dict())
    
