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
    secret = Column(String(64))

    def __init__(self, name=None):
        self.name = name
        self.secret = hexlify(os.urandom(64))

    def __repr__(self):
        return '<User %r>' % (self.name)

class Game(Base, I_Serializable):
    __tablename__ = 'games'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), unique=True)

    def __init__(self, name=None):
        self.name = name

    def __repr__(self):
        return '<Game %r>' % (self.name)

class Lock(Base, I_Serializable):
    __tablename__ = 'locks'
    id = Column(Integer, primary_key=True)
    key = Column(String(256), unique=False)
    clue = Column(String(256), unique=False)
    treasure = Column(String(256), unique=False)
    game = Column('game_id', Integer, ForeignKey("game.id"), nullable=False)

    def __init__(self, name=None, key=None, clue=None, treasure=None):
        self.name = name
        self.key = key
        self.clue = clue
        self.treasure = treasure

    def __repr__(self):
        return '<Lock %r: %r, %r, %r>' % (self.name, self.key, self.clue, self.treasure)

class UserProgress(Base, I_Serializable):
    __tablename__ = 'users_progress'
    id = Column(Integer, primary_key=True)
    user = Column('user_id', Integer, ForeignKey("user.id"), nullable=False)
    lock = Column('lock_id', Integer, ForeignKey("game.id"), nullable=False)

    def __init__(self, user=None, lock=None):
        self.name = name
        self.lock = lock

    def __repr__(self):
        percentage = (self.lock.order / self.lock.game.total) * 100
        return '<UserProgress %r (%r): %r>' % (self.user.name, self.lock.game.name, percentage)
