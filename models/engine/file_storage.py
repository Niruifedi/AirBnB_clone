#!/usr/bin/python3
"""class for file storage"""


class FileStorage:
    """
        this class serializes instances to json file
        and also deserializes json files to instances
    """
    __file_path = ""
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        pass

    def save(self):
        pass

    def reload(self):
        pass