#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------------------------------------
   @Name:     __init__.py
   @Desc:     
   @Author:   liangz.org@gmail.com
   @Create:   2020.08.02   14:51
-------------------------------------------------------------------------------
   @Change:   2020.08.02
-------------------------------------------------------------------------------
"""

from flask import Blueprint
from . import views, errors

main = Blueprint('main', __name__)


