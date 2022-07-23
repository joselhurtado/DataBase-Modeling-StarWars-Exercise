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
     # Here we define columns for the table User
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    first_name = Column(String(250))
    last_name = Column(String(250))
    email = Column(String(200))
    password = Column(String, primary_key=True)
    register_date = Column(String)

class Favorites:
    __tablename__ = 'favorites'
    # Here we define columns for the table favorites.
    # Notice that each column is also a normal Python instance attribute.
    available_favs = Column(String(200))
    character_id - Column(String(150))
    starship_id - Column(String(150))
    planet_id - Column(String(150))


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')