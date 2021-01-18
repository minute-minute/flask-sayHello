#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   settings.py
@Time    :   2021/01/14 19:35:43
@Author  :   FenFen Xu
@Version :   1.0
@Contact :   fenfen.xu@zhangmen.com
@Desc    :   配置文件
'''

import os

from sayHello import app

dev_db = 'sqlite:///' + os.path.join(os.path.dirname(app.root_path), 'data.db')

SECRET_KEY = os.getenv('SECRET_KEY', 'minute')

SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', dev_db)

BOOTSTRAP_SERVER_LOCAL = True