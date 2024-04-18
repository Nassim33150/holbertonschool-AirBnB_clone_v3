#!/usr/bin/python3
<<<<<<< HEAD
from flask import Blueprint

app_views = Blueprint('app_views', __name__)

from api.v1.views.index import *
=======
""" import modules """
from api.v1.views import states
from api.v1.views import cities
from api.v1.views import amenities
from flask import Blueprint
from api.v1.views.index import *

app_views = Blueprint('app_views', __name__)

>>>>>>> 66aceb74c43ec53b6f3f97318bd7bccf3082a81c
