import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'User'
    id = Column(Integer, primary_key=True)
    email = Column(String(120), unique=True, nullable=False)
    password = Column(String(80), unique=False, nullable=False)
    is_active = Column(Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.email

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }

class Planets(Base):
    __tablename__ = 'Planet'
    id = Column(Integer, primary_key = True)
    name = Column(String, nullable=False)
    diameter = Column(Integer, nullable=False)
    rotation_period = Column(Integer, nullable=False)
    orbital_period = Column(Integer, nullable=False)
    gravity = Column(Integer, nullable=False)        
    population = Column(Integer, nullable=False)
    climate = Column(String, nullable=False)
    terrain = Column(String, nullable=False)
    surface_water = Column(Integer, nullable=False)
    url = Column(String, nullable=False) 
    movies = Column(String, nullable=False)           
    favorite = Column(Boolean, nullable=False)            
            
    def __repr__(self):
        return '<Planet %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            'name': self.name,
            'diameter': self.diameter,
            'rotation_period': self.rotation_period,
            'orbital_period': self.orbital_period,
            'gravity': self.gravity,
            'population': self.population,
            'climate': self.climate,
            'terrain': self.terrain,
            'surface_water': self.surface_water,
            'url': self.url,
            "movies": self.movies,
            'favorite': self.favorite,
        }    

class People(Base):
    __tablename__ = 'People'
    id = Column(Integer, primary_key = True)
    name = Column(String, nullable=False)
    gender = Column(String, nullable=False)
    height = Column(Integer, nullable=False)
    mass = Column(Integer, nullable=False)
    hair_color = Column(String, nullable=False)
    skin_color = Column(String, nullable=False)
    eye_color = Column(String, nullable=False)
    birth_year = Column(Integer, nullable=False)
    homeworld = Column(String, nullable=False)
    url = Column(String, nullable=False)
    movies = Column(String, nullable=False)
    favorite = Column(Boolean, nullable=False)

    def __repr__(self):
        return '<People %r>' % self.name

    def serialize(self):
        return {
            "name": self.name,
            "height": self.height,
            "mass": self.mass,
            "hair_color": self.hair_color,
            "skin_color": self.skin_color,
            "eye_color": self.eye_color,
            "birth_year": self.birth_year,
            "gender": self.gender,
            "homeworld": self.homeworld,
            "url": self.url,
            "movies": self.movies,
            "favorite": self.favorite,
        }

class Movies(Base):
    __tablename__ = 'Movies'
    id = Column(Integer, primary_key = True)
    title = Column(String, nullable=False)
    year  = Column(Integer, nullable=False)

    def __repr__(self):
        return '<Movies %r>' % self.title

    def serialize(self):
        return {
            'title': self.title,
            'year': self.year,
        }

class Favorites(Base):
    __tablename__ = 'Favorites'
    id = Column(Integer, primary_key = True)
    people = Column(String, nullable=False)
    planet = Column(String, nullable=False)
    movie =  Column(String, nullable=False)
    favorite = Column(Boolean, nullable=False)

    def __repr__(self):
        return '<Favorites %r>' % self.id

    def serialize(self):
        return {
            'people': self.people,
            'planet': self.planet,
            'movie': self.movie,
            'favorite': self.favorite,
        }


# class Address(Base):
#     __tablename__ = 'address'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(250))
#     street_number = Column(String(250))
#     post_code = Column(String(250), nullable=False)
#     person_id = Column(Integer, ForeignKey('person.id'))
#     person = relationship(Person)

#     def to_dict(self):
#         return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')