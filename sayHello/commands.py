#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   commands.py
@Time    :   2021/01/14 19:37:00
@Author  :   FenFen Xu
@Version :   1.0
@Contact :   fenfen.xu@zhangmen.com
@Desc    :   自定义flask命令
'''
from sayHello.models import Message
import click
from sayHello import app, db


@app.cli.command('init-db')
@click.option('--drop', is_flag=True, help='create after drop')
def init_db(drop):
    if drop:
        click.confirm('will be delete all the database, are you sure continue?', abort=True)
        db.drop_all()
        click.echo('drop all table')

    db.create_all()
    click.echo('Initialized database.')


@app.cli.command('forge')
@click.option('--count', default=20, help='Quantity of messages, default is 20.')
def forge(count):
    '''Generate fake message'''

    from faker import Faker

    # 重建表
    db.drop_all()
    db.create_all()

    fake = Faker()

    click.echo('Working...')

    # 生成数据
    for _ in range(count):
        message = Message(
            author=fake.name(),
            message=fake.sentence(),
            timestamp=fake.date_time_this_year()
        )
        db.session.add(message)
    db.session.commit()
    click.echo('Create %d fake message.' % count)

