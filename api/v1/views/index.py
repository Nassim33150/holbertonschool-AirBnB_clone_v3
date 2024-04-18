#!/usr/bin/python3
from flask import jsonify
from flask import Blueprint
from api.v1.views import app_views
from models import storage
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models.amenity import Amenity


""" Status of the API """


@app_views.route('/status', methods=['GET'])
def get_status():
    return jsonify({"status": "OK"})