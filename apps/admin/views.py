#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------------------------------------
   @Name:     views.py
   @Desc:     
   @Author:   liangz.org@gmail.com
   @Create:   2020.08.09   23:20
-------------------------------------------------------------------------------
   @Change:   2020.08.09
-------------------------------------------------------------------------------
"""
from flask_admin import Admin, BaseView, expose
from flask_admin.contrib.sqla.view import ModelView


class MyView(ModelView):

    @expose('/')
    def home(self):
        return self.render('index.html')

    @expose('/index')
    def index(self):
        return self.render('admin/index.html')
