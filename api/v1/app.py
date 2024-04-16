#!/usr/bin/python3

from flask import Flask
from api import app
from models import storage
from api.v1.views import app_views
import os

@app.teardown_appcontext
def teardown(exception):
    """Handles teardown of the application."""
    storage.close()

if __name__ == "__main__":
    host = os.getenv("HBNB_API_HOST", "0.0.0.0")
    port = int(os.getenv("HBNB_API_PORT", "5000"))
    app.run(host=host, port=port, threaded=True)