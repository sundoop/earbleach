# all the imports
import os
import random

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


def get_random_worm():
    """
    get a random worm
    """

    rand_index = random.randrange(0, db.session.query(Worm).count())
    return db.session.query(Worm)[rand_index]


@app.route('/')
def index():
    random_worm = get_random_worm()
    return render_template('show_one_worm.html', worm=random_worm)


@app.route('/<name>')
def name_route(name):
    return "Hello {}!".format(name)


if __name__ == "__main__":
    app.run()
