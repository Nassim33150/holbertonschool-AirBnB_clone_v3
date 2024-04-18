#!/usr/bin/python3
""" import modules """
from flask import Flask
from models import storage
from api.v1.views import app_views

# Create Flask instance
app = Flask(__name__)

# Register blueprint
app.register_blueprint(app_views, url_prefix="/api/v1")

# Teardown method
@app.teardown_appcontext
def teardown(exception):
    storage.close()

# Run Flask server
if __name__ == "__main__":
    host = environ.get('HBNB_API_HOST', '0.0.0.0')
    port = int(environ.get('HBNB_API_PORT', 5000))
    app.run(host=host, port=port, threaded=True)
