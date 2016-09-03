from sqlalchemy import create_engine
from sqlalchemy import MetaData, Table, Column, Integer, String
from sqlalchemy.orm import sessionmaker

dburl = 'sqlite:///sqlite.db'

engine = create_engine(dburl, echo=False)
conn = engine.connect()

metadata = MetaData()

Session = sessionmaker(bind=engine)
session = Session()

print('database initialized')

