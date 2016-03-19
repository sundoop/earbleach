# all the imports
import os

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from micawber.providers import bootstrap_basic
from micawber.contrib.mcflask import add_oembed_filters


# create our little application
app = Flask(__name__)
app.config.from_object(os.environ.get('APP_SETTINGS'))
db = SQLAlchemy(app)

oembed_providers = bootstrap_basic()
add_oembed_filters(app, oembed_providers)


@app.route('/')
def index():
    return "Hellow World!"


@app.route('/<name>')
def name_route(name):
    return "Hello {}!".format(name)


if __name__ == "__main__":
    app.run()
