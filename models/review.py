#!/usr/bin/python3
"""class for Review"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Review inherits from BaseModel"""
    place_id = ""
    user_id = ""
    text = ""
