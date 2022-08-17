#!/usr/bin/python3
"""class for file storage"""
import json
from os.path import exists
from models import base_model, user, place, state, city, amenity, review


BaseModel = base_model.BaseModel
User = user.User
Place = place.Place
State = state.State
City = city.City
Amenity = amenity.Amenity
Review = review.Review
name_class = ["BaseModel", "City", "State",
              "Place", "Amenity", "Review", "User"]


class FileStorage:
    """
        this class serializes instances to json file
        and also deserializes json files to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Setin __object with key <obj_class_name>.id"""
        class_name = obj.__class__.__name__
        id = obj.id
        cls_id = class_name + "." + id
        FileStorage.__objects[cls_id] = obj

    def save(self):
        """Serialize __objects to the JSON file __file_path."""
        odict = FileStorage.__objects
        objdict = {obj: odict[obj].to_dict() for obj in odict.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(objdict, f)

    def reload(self):
        """ if (__file_path) exists deserializes JSON file to __objects
            elif , do nothing. If the file not exist,
        """
        dic_obj = {}
        FileStorage.__objects = {}
        if (exists(FileStorage.__file_path)):
            with open(FileStorage.__file_path, "r") as fil:
                dic_obj = json.load(fil)
                for key, value in dic_obj.items():
                    class_nam = key.split(".")[0]
                    if class_nam in name_class:
                        FileStorage.__objects[key] = eval(class_nam)(**value)
                    else:
                        pass
