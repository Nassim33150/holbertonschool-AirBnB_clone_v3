#!/usr/bin/python3
from flask import Flask
from api import app
from models import storage
from api.v1.views import app_views
import os
from flask import jsonify
from . import app_views



@app.teardown_appcontext
def teardown(exception):
    """Handles teardown of the application."""
    storage.close()

@app_views.app_errorhandler(404)
def not_found(error):
    """Handles 404 Not Found errors."""
    response = jsonify({"erreur": "Non trouvé"})
    response.status_code = 404
    return response

if __name__ == "__main__":
    host = os.getenv("HBNB_API_HOST", "0.0.0.0")
    port = int(os.getenv("HBNB_API_PORT", "5000"))
    app.run(host=host, port=port, threaded=True)
