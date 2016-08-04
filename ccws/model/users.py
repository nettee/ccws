from .database import *
from .base import *

class User(Base):
    __tablename__ = 'users'

    headers = ('id', 'name', 'level', 'region', 'description', 'phone')

    id = Column('id', String, primary_key=True)
    name = Column('name', String)
    level = Column('level', Integer)
    region = Column('region', String)
    description = Column('description', String)
    phone = Column('phone', String)

    def asdict(self):
        return {attr: getattr(self, attr) for attr in self.headers} 

    def __str__(self):
        return "<User(id='{id}', name='{name}', level='{level}', region='{region}', description='{description}', phone='{phone}')>".format(**self.asdict())

    __repr__ = __str__

def create(user_dict):
    print('create user {}'.format(user_dict))
    user = User(**user_dict)
    session.add(user)
    session.commit()
    return user_dict

def read(id=None):
    if id:
        user = session.query(User).filter(User.id == id).one_or_none()
        return user.asdict() if user else None
    else:
        user_list = session.query(User).all()
        return [user.asdict() for user in user_list]

def exists(user):
    id = user['id']
    exist = session.query(User).filter(User.id == id).one_or_none()
    return exist

Base.metadata.create_all(engine)


