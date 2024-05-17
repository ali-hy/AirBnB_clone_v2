#!/usr/bin/python3
"""Defines the Amenity class."""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    """Represents an Amenity for a MySQL database."""

    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
    place = relationship(
        "Place",
        secondary='place_amenity',
        back_populates='amenities',
        viewonly=False
    )
