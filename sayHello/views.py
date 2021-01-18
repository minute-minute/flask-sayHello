#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   views.py
@Time    :   2021/01/14 19:35:17
@Author  :   FenFen Xu
@Version :   1.0
@Contact :   fenfen.xu@zhangmen.com
@Desc    :   视图函数
'''

from flask import render_template, redirect
from flask.helpers import flash, url_for
from sayHello.forms import HelloForm
from sayHello.models import Message
from sayHello import app, db


@app.route('/', methods=['GET', 'POST'])
def index():
    form = HelloForm()
    messages = Message.query.order_by(Message.timestamp.desc()).all()

    if form.validate_on_submit():
        name = form.name.data
        body = form.body.data

        message = Message(author=name, message=body)
        db.session.add(message)
        db.session.commit()

        flash('you message have been sent to the world.')
        return redirect(url_for('index'))

    return render_template('index.html', form=form, messages=messages)

