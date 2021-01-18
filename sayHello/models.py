#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   models.py
@Time    :   2021/01/14 19:36:04
@Author  :   FenFen Xu
@Version :   1.0
@Contact :   fenfen.xu@zhangmen.com
@Desc    :   数据库模型
'''
from datetime import datetime
from sayHello import db


class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(20))
    message = db.Column(db.String(200))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, index=True)

