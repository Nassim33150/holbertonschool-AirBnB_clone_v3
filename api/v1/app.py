#!/usr/bin/python3

from flask import Flask
from models import storage
import os
from api.v1.views import app_views


app = Flask(__name__)

app.register_blueprint(app_views)

@app.teardown_appcontext
def teardown(exception):
    """Handles teardown of the application."""
    storage.close()

if __name__ == "__main__":
    host = os.getenv("HBNB_API_HOST", "0.0.0.0")
    port = int(os.getenv("HBNB_API_PORT", "5000"))
    app.run(host=host, port=port, threaded=True)
""" import modules """
from flask import Flask
from models import storage
from api.v1.views import app_views
import os
from flask import jsonify

""" Create a new Flask instance """
app = Flask(__name__)

""" Close the session """
@app.teardown_appcontext
def teardown_appcontext(exception):
    storage.close()

""" Create a 404 error """
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Not found"}), 404

if __name__ == "__main__":
    host = os.getenv('HBNB_API_HOST', '0.0.0.0')
    port = int(os.getenv('HBNB_API_PORT', 5000))
    app.run(host=host, port=port, threaded=True)
