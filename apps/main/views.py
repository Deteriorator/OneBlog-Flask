#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------------------------------------
   @Name:     views.py
   @Desc:     
   @Author:   liangz.org@gmail.com
   @Create:   2020.08.02   12:09
-------------------------------------------------------------------------------
   @Change:   2020.08.02
-------------------------------------------------------------------------------
"""
from flask import Blueprint

main = Blueprint('main', __name__)


@main.route('/')
def home():
    return '<h1>Hello World!</h1>'
