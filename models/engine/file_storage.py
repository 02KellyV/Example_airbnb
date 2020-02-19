
import json
import os.path
from models.base_model import BaseModel

class FileStorage:
    """Class for Serializes and Deserializes"""
    __file_path = "file.json" #is a file
    __objects = {} #is a dict

    def all(self):
        """returns the dict __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the key <obj class name>.id and assign obj entire"""
        key = obj.__class__.__name__ + "." + obj.id #class name of an obj + id
        self.__objects[key] = obj
        #self.__objects.update({key, obj})

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        newdict_objs = {} #to store the info that will save
        for key, val in self.__objects: #pass trought for each key/val
            newdict_objs[key] = val.to_dict()
        with open(self.__file_path, 'w') as json_f: #file handling
            json_f.write(json.dumps(newdict_objs)) #dumps: encode json data
            #converts dict object into JSON string data format and write to file

    def reload(self):
        """deserializes the JSON file to __objects"""
        if os.path.isfile(self.__file_path):
            with open(self.__file_path, 'r') as json_f:
                othrdict_objs = json.loads(json_f) #loads: decode json data
            for key, val in othrdict_objs.items():
                self.__objects[key] = BaseModel(**val)
