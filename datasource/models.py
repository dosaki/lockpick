import os
from sqlalchemy import Column, Integer, String
from binascii import hexlify

from database import Base

class I_Serializable():
    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

class User(Base, I_Serializable):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), unique=True)
    secret_key = Column(String(64))

    def __init__(self, name=None):
        self.name = name
        self.secret_key = hexlify(os.urandom(64))

    def __repr__(self):
        return '<User %r>' % (self.name)
