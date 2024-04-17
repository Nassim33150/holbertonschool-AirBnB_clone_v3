#!/usr/bin/python3
""" import modules """
from api.v1.views import states
from api.v1.views import cities
from api.v1.views import amenities
from flask import Blueprint
from api.v1.views.index import *

app_views = Blueprint('app_views', __name__)

