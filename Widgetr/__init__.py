"""
The flask application package.
"""
from flask import Flask
app = Flask(__name__)
app.debug = True
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True

import Widgetr.views
import Widgetr.data_access_layer