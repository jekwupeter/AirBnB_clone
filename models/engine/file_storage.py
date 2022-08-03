#!/usr/bin/python3
"""Defines an abstracted storage"""
from encodings import utf_8
#from pathlib import Path
import json
import os.path

class FileStorage:
    """
    serilaizes instances to a JSON file and deserializes JSON file to instances
    """
    __file_path = "file.json"
    #__file_path = str(Path.cwd()) + "file.json"
    __objects = {}
    def __init__(self):
        pass
    
    def all(self):
        """
        returns the dictionary __objects
        """
        return self.__objects
    
    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        """
        self.__objects[obj.id] = obj

    def save(self):
        """
        Serializes __objects to the JSON file
        """
        with open(self.__file_path, "w+", encoding="utf_8") as outputfile:
            json.dump(self.__objects, outputfile)

    def reload(self):
        """
        deserializing the JSON file to __objects only if it exist
        """
        if os.path.exists(self.__file_path):
            with open(self.__file_path, r) as inputobject:
                new_object= json.loads(inputobject)
            self.__objects.update(new_object)