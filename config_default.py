# -*- coding: utf-8 -*-
"""
Created on 2015-10-23 08:06:00

@author: Tran Huu Cuong <tranhuucuong91@gmail.com>

"""
import os

# Blog configuration values.

# You may consider using a one-way hash to generate the password, and then
# use the hash again in the login view to perform the comparison. This is just
# for simplicity.
ADMIN_PASSWORD = 'admin@secret'
APP_DIR = os.path.dirname(os.path.realpath(__file__))

PATH_SQLITE_DB=os.path.join(APP_DIR, 'blog.db')
# The playhouse.flask_utils.FlaskDB object accepts database URL configuration.
DATABASE = 'sqliteext:///{}'.format(PATH_SQLITE_DB)
DEBUG = False

# The secret key is used internally by Flask to encrypt session data stored
# in cookies. Make this unique for your app.
SECRET_KEY = 'shhh, secret!'

# This is used by micawber, which will attempt to generate rich media
# embedded objects with maxwidth=800.
SITE_WIDTH = 800

APP_HOST='127.0.0.1'
APP_PORT=5000

# disable elasticsearch by default
IS_ES_INDEX = False

ES_HOST = {
    "host": "172.17.42.1",
    "port": 9200
}

ES_INDEX_NAME = 'notebooks'
ES_TYPE_NAME = 'notebooks'

