#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   __init__.py
@Time    :   2021/01/14 20:01:18
@Author  :   FenFen Xu
@Version :   1.0
@Contact :   fenfen.xu@zhangmen.com
@Desc    :   创建程序是咧，初始化扩展
'''


from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_debugtoolbar import DebugToolbarExtension


app = Flask('sayHello')
app.config.from_pyfile('settings.py')

app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True


db = SQLAlchemy(app)
bootstrap = Bootstrap(app)
moment = Moment(app)
# toolbar = DebugToolbarExtension(app)


from sayHello import views, errors, commands

