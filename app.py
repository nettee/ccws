#!/usr/bin/env python3

import json
import base64

from bottle import route, get, post, put, delete
from bottle import request, response, error
from bottle import run, abort

@route('/')
def login():
    abort(404, 'Page Not Found')

if __name__ == '__main__':
    run(host='localhost', port=3000, debug=True)
