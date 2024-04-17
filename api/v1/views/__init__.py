#!/usr/bin/python3
""" import Blueprint from flask doc """
from flask import Blueprint


""" Create a Blueprint object """
app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')
