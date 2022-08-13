#!/usr/bin/python3
"""class for file storage"""
import json
from models.base_model import BaseModel


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
        """Deserialize the JSON file __file_path to __objects, if it exists."""
        try:
            with open(FileStorage.__file_path) as f:
                objdict = json.load(f)
            for o in objdict.values():
                cls_name = o["__class__"]
                del o["__class__"]
                self.new(eval(cls_name)(**o))
        except FileNotFoundError:
            return
