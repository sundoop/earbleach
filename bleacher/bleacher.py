# all the imports
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash
from contextlib import closing
from micawber.providers import bootstrap_basic
from micawber.contrib.mcflask import add_oembed_filters


# configuration
DATABASE = 'bleacher.db'
DEBUG = True
SECRET_KEY = 'production_key'
USERNAME = 'admin'
PASSWORD = 'default'

# create our little application
app = Flask(__name__)
app.config.from_object(__name__)

oembed_providers = bootstrap_basic()
add_oembed_filters(app, oembed_providers)


def connect_db():
    return sqlite3.connect(app.config['DATABASE'])


@app.before_request
def before_request():
    g.db = connect_db()


@app.teardown_request
def teardown_request(exception):
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()


@app.route('/')
def show_one_worm():
    cur = g.db.execute('select * from entries;')
    print "all: ", cur.fetchall()
    worms = [dict(title=row[0], text=row[1]) for row in cur.fetchall()]
    print "worms: %s" % worms
    worm = worms[0] if worms else None
    return render_template('show_one_worm.html', worm=worm)

if __name__ == "__main__":
    app.run()
