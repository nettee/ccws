#!/usr/bin/env python3

import json
import base64

from bottle import route, get, post, put, delete
from bottle import request, response, error
from bottle import redirect, abort
from bottle import static_file
from bottle import run

from jinja2 import Environment, FileSystemLoader

from model import users

env = Environment(loader=FileSystemLoader('ccws/views'))

@route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='ccws/public')

@route('/login')
@route('/')
def login():
    template = env.get_template('login.html')
    return template.render()

@post('/login.do')
def do_login():
    username = request.forms['username']
    password = request.forms['password']
    redirect('/dashboard')

subsystems = ('users', 'informations', 'documents', 'regions')

dashboard_nav = (
    ('users', '用户管理'),
    ('informations', '情报管理'),
    ('documents', '文档管理'),
    ('regions', '区域管理'),
)

@route('/dashboard')
def show_dashboard():
    redirect('/dashboard/users')

@route('/dashboard/<subsystem>')
def show_dashboard_subsystem(subsystem):
    if subsystem not in subsystems:
        abort(404)
    template_file = '{}.html'.format(subsystem)
    template = env.get_template(template_file)
    return template.render(
        nav=dashboard_nav, 
        subsystem=subsystem, 
        data=get_subsystem_data(subsystem)
    )

def get_subsystem_data(subsystem):
    if subsystem == 'users':
        data = users.read()
        return data
    else:
        return None

if __name__ == '__main__':
    run(host='localhost', port=5000, debug=True)
