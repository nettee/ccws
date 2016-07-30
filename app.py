#!/usr/bin/env python3

import json
import base64

from bottle import route, get, post, put, delete
from bottle import request, response, error
from bottle import run, abort
from bottle import redirect
from bottle import static_file

from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader('views'))

@route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='public')

@route('/template/a.html')
def a_html():
    template = env.get_template('a.html')
    return template.render(action='hate')

@route('/dashboard')
def show_dashboard():
    return 'haha'
	# template = env.get_template('dashboard.html')
	# return template.render()	

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

if __name__ == '__main__':
    run(host='localhost', port=5000, debug=True)
