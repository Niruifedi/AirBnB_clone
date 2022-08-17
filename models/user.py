#!/usr/bin/python3
"""class User"""
import uuid
from models.base_model import BaseModel


class User(BaseModel):
    """
        class User inherits from the basemodel
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
