# all the imports
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash
from contextlib import closing
from micawber.providers import bootstrap_basic
from micawber.contrib.mcflask import add_oembed_filters


print os.environ['APP_SETTINGS']
# configuration
DATABASE = 'bleacher.db'
DEBUG = True
SECRET_KEY = 'production_key'
USERNAME = 'admin'
PASSWORD = 'default'

# create our little application
app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])

oembed_providers = bootstrap_basic()
add_oembed_filters(app, oembed_providers)


@app.route('/')
def index():
    return "Hellow World!"


@app.route('/<name>')
def name_route():
    return "Hello {}!".format(name)


if __name__ == "__main__":
    app.run()
