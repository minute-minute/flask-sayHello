#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   forms.py
@Time    :   2021/01/14 19:36:22
@Author  :   FenFen Xu
@Version :   1.0
@Contact :   fenfen.xu@zhangmen.com
@Desc    :   表单
'''

from wtforms.fields.simple import SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length
from flask_wtf import FlaskForm
from wtforms import StringField


class HelloForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(1, 20)])
    body = TextAreaField('Message', validators=[DataRequired(), Length(1, 200)])
    submit = SubmitField()

