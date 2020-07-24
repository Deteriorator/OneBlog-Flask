#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------------------------------------
   @Name：    app.py
   @Desc:     
   @Author:   liangz.org@gmail.com
   @Create:   2020.07.24   17:51
-------------------------------------------------------------------------------
   @Change:   2020.07.24
-------------------------------------------------------------------------------
"""

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()


