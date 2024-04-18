<<<<<<< HEAD
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
=======
# api/v1/app.py
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
>>>>>>> 66aceb74c43ec53b6f3f97318bd7bccf3082a81c
