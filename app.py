#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------------------------------------
   @Name:     app.py
   @Desc:     
   @Author:   liangz.org@gmail.com
   @Create:   2020.07.24   17:51
-------------------------------------------------------------------------------
   @Change:   2020.07.24
-------------------------------------------------------------------------------
"""

from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from apps.main.views import main

db = SQLAlchemy()


def create_app():
    application = Flask(__name__)
    configure_app(application)
    db.init_app(application)
    application.register_blueprint(main)
    return application


def configure_app(app, config=Config):
    app.config.from_object(config)


