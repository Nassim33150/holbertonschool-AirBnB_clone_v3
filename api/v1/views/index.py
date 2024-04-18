#!/usr/bin/python3
""" Index module for the API """

from api.v1.views import app_views
from flask import jsonify
from models import storage
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


<<<<<<< HEAD
@app_views.route('/status', strict_slashes=False)
def get_status():
    """ Return status """
    status = {
        "status": "OK"}
    return jsonify(status)


@app_views.route('/stats', strict_slashes=False)
def stats():
    """ Return stats """
=======
""" Status of the API """

@app_views.route('/status', methods=['GET'])
def get_status():
    return jsonify({"status": "OK"})

""" Stats of objects """
@app_views.route('/api/v1/stats', methods=['GET'])
def get_stats():
>>>>>>> 95797c7baf48e8ca04f1d76eef8f218016181d05
    stats = {
        "amenities": storage.count("Amenity"),
        "cities": storage.count("City"),
        "places": storage.count("Place"),
        "reviews": storage.count("Review"),
        "states": storage.count("State"),
        "users": storage.count("User")
    }
    return jsonify(stats)
