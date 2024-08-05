#!/usr/bin/python3
"""City Module for HBNB project."""
import os
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship

from models.base_model import BaseModel, Base

class City(BaseModel, Base):
    """The city class, containing state ID and name."""
    __tablename__ = 'cities'
    name = Column(String(128), nullable=False) if os.getenv('HBNB_TYPE_STORAGE') == 'db' else ''
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False) if os.getenv('HBNB_TYPE_STORAGE') == 'db' else ''
    places = relationship(
        'Place',
        cascade='all, delete, delete-orphan',
        backref='cities'
    ) if os.getenv('HBNB_TYPE_STORAGE') == 'db' else None

class Place(BaseModel, Base):
    """Representation of a place"""
    __tablename__ = 'places'
    id = Column(String(60), primary_key=True, nullable=False)
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
