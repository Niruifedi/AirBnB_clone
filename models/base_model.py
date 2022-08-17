#!/usr/bin/python3
"""basemodel class"""
import uuid
import models
from datetime import datetime


class BaseModel:
    """Class BaseModel
        This class defines all common attributes/methods
        for other classes
    """

    def __init__(self,  *args, **kwargs):
        """class constructor"""
        if len(kwargs) != 0:
            for key, val in kwargs.items():
                if key == '__class__':
                    pass
                elif key == "created_at":
                    self.created_at = datetime.strptime(val,
                                                        '%Y-%m-%dT%H:%M:%S.%f')
                elif key == "updated_at":
                    self.updated_at = datetime.strptime(val,
                                                        '%Y-%m-%dT%H:%M:%S.%f')
                else:
                    self.__setattr__(key, val)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def save(self):
        """save and update method"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """dictionary representaton of objects"""
        dict = {}
        for key, val in self.__dict__.items():
            if key in ['created_at', 'updated_at']:
                dict[key] = val
        dict["updated_at"] = self.updated_at.isoformat()
        dict["created_at"] = self.created_at.isoformat()
        dict["__class__"] = self.__class__.__name__
        return dict

    def __str__(self):
        """string representation"""
        return("[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__))
