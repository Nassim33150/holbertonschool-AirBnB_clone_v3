# api/v1/app.py
from flask import Flask
from models import storage
from api.v1.views import app_views
import os
from flask import jsonify

app = Flask(__name__)

@app.teardown_appcontext
def teardown_appcontext(exception):
    storage.close()

<<<<<<< HEAD
=======
@app.errorhandler(404)
def not_found(error):
    """Handles 404 Not Found errors."""
    return jsonify({"error": "Not found"}), 404


>>>>>>> 12325ea09b8cff8324b82fe9d9ccf8ad66e5c2eb
if __name__ == "__main__":
    host = os.getenv('HBNB_API_HOST', '0.0.0.0')
    port = int(os.getenv('HBNB_API_PORT', 5000))
    app.run(host=host, port=port, threaded=True)
