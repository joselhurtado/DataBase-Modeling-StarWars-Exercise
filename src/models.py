import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    
    class Planet(Base):
        __tablename__ = 'planet'
        id = Column(Integer, primary_key=True)
        name = Column(String(250), nullable=False)
    
    class Planet_Fav(Base):
        __tablename__ = 'planet_fav'
    # Here we define columns for the table address.
        id = Column(Integer, primary_key=True)
        user_id = Column(Integer, ForeignKey('user.id'))
        planet_id = Column(Integer, ForeignKey('planet.id'))
        
        def to_dict(self):
            return {}
    
    class Character(Base):
        __tablename__ = 'character'
        id = Column(Integer, primary_key=True)
        name = Column(String(250), nullable=False)
    
    class Character_Fav(Base):
        __tablename__ = 'character_fav'
    # Here we define columns for the table address.
        id = Column(Integer, primary_key=True)
        user_id = Column(Integer, ForeignKey('user.id'))
        character_id = Column(Integer, ForeignKey('character.id'))
    
    def to_dict(self):
        return {}

    class Starship(Base):
        __tablename__ = 'starship'
        id = Column(Integer, primary_key=True)
        name = Column(String(250), nullable=False)
    
    class Starship_Fav(Base):
        __tablename__ = 'starship_fav'
    # Here we define columns for the table address.
        id = Column(Integer, primary_key=True)
        user_id = Column(Integer, ForeignKey('user.id'))
        starship_id = Column(Integer, ForeignKey('starship.id'))
    
    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')