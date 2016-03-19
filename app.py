# all the imports
import os

from flask import Flask, render_template
from flask.ext.sqlalchemy import SQLAlchemy
from micawber.providers import bootstrap_basic
from micawber.contrib.mcflask import add_oembed_filters

# create our little application
app = Flask(__name__)
app.config.from_object(os.environ.get('APP_SETTINGS'))
db = SQLAlchemy(app)

from models import Worm

oembed_providers = bootstrap_basic()
add_oembed_filters(app, oembed_providers)


@app.route('/')
def index():
    return render_template('show_one_worm.html')


@app.route('/<name>')
def name_route(name):
    return "Hello {}!".format(name)


if __name__ == "__main__":
    app.run()
