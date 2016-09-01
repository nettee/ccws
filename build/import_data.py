#!/usr/bin/env python3

from sqlalchemy import create_engine
import json

dbfile = '/tmp/sqlite.db'
files = ['primer-dataset/users.json']

def import_table(filename):
    
    tablename = filename.split('.')[0]
    try:
        with open(filename, 'r') as f:
            for line in f:
                line = line.rstrip('\n')
                obj = json.loads(line)
                print(obj)
    except IOError as e:
        print('error:', e)

if __name__ == '__main__':

    engine = create_engine(dbfile)

    for filename in files:
        import_table(filename)
        




