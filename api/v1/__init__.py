<<<<<<< HEAD
#!/usr/bin/python3
from flask import Blueprint

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

from api.v1.views import *
=======
from flask import Blueprint


app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')


from api.v1.views.index import *
>>>>>>> 66aceb74c43ec53b6f3f97318bd7bccf3082a81c
