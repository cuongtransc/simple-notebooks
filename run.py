#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from app import app
#from app import database

#if app.debug is not True:
    #import logging
    #from logging.handlers import RotatingFileHandler

    #file_handler = RotatingFileHandler('logs/glossary.log', maxBytes=1024 * 1024 * 100, backupCount=20)
    ##file_handler.setLevel(logging.ERROR)
    ##file_handler.setLevel(logging.INFO)
    #file_handler.setLevel(logging.DEBUG)

    #formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    #file_handler.setFormatter(formatter)
    #app.logger.addHandler(file_handler)

#app.run(host='0.0.0.0', port=5002, debug=app.debug)

#database.create_tables([Entry, FTSEntry], safe=True)
app.run(port=5000, host='0.0.0.0', debug=True)

