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
from flask import render_template
from apps.models import Post, User
from apps.main import main


@main.route('/')
def home():
    articles = Post.query.filter_by(post_type='page').first()
    return render_template('base.html', article=articles.post_title)


@main.route('/<id>')
def article(id):
    article = Post.query.filter_by(ID=id).first()
    author = User
    print(article.article_category)
    # print(article[0].post_title)
    return render_template('article-detail.html', article=article)
