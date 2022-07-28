import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class Character(Base):
    __tablename__ = 'character'
    character_id = Column(Integer, primary_key=True)
    characterName = Column(String(150))

class Planet(Base):
    __tablename__ = 'planet'
    planet_id = Column(Integer, primary_key=True)
    planetName = Column(String(150))

class Starship(Base):
    __tablename__ = 'starship'
    starship_id = Column(Integer, primary_key=True)
    planetName = Column(String(150))

class Favorites(Base):
    __tablename__ = 'favorites'
    available_favs = Column(String)
    userId = Column(Integer, primary_key=True)
    character_id = Column(Integer, primary_key=True)
    starship_id = Column(Integer, primary_key=True)
    planet_id = Column(Integer, primary_key=True)

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table User
    # Notice that each column is also a normal Python instance attribute.
    available_favs = Column(String)
    userId = Column(Integer, primary_key=True)
    first_name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    email = Column(String(200))
    password = Column(String, primary_key=True)
    register_date = Column(String)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')