from .database import *
from .base import *

def create(username, password):
    token = '{}-{}'.format(username, password)
    auth = {'token': token}
    return auth
