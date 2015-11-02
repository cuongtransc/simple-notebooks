#!/usr/bin/env python3

from flask import Flask
from micawber import bootstrap_basic
from micawber.cache import Cache as OEmbedCache
from playhouse.flask_utils import FlaskDB

from .momentjs import momentjs

# Create a Flask WSGI app and configure it using values from the module.
app = Flask(__name__)
# app.config.from_object(__name__)
app.config.from_object('config')
app.jinja_env.globals['momentjs'] = momentjs

# FlaskDB is a wrapper for a peewee database that sets up pre/post-request
# hooks for managing database connections.
flask_db = FlaskDB(app)

# The `database` is the actual peewee database, as opposed to flask_db which is
# the wrapper.
database = flask_db.database

# Configure micawber with the default OEmbed providers (YouTube, Flickr, etc).
# We'll use a simple in-memory cache so that multiple requests for the same
# video don't require multiple network requests.
oembed_providers = bootstrap_basic(OEmbedCache())

from elasticsearch import Elasticsearch

es = Elasticsearch(hosts=[app.config.get('ES_HOST')])

from app.routes import index
from app.routes import search
