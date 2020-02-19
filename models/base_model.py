import uuid
from datetime import datetime

class BaseModel:
    """Module BaseModel """
    id = str(uuid.uuid4()) #string assign with an uuid4() gen-uniq-id
    created_at = datetime.now() #datetime - assign current datetime when instance
    updated_at = datetime.now() #will be updated every time you change your obj

    def __init__(self, *args, **kwargs):
        """*args - Tuple: contains list anonymous arg, no names, just order"""
        """**kwargs - Dict: contains all args by key/value, named args"""
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at":
                    created_at = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "updated_at":
                    updated_at = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                elif key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """ print: [<class name>] (<self.id>) <self.__dict__>"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """ update public inst attr: updated_at, current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """returns dict containing keys/values __dict__ of the instance"""
        """Is the first piece of the serialization/deserialization process"""
        """create a dict representation with simple obj type of BaseModel"""
        newdict = self.__dict__.copy()
        newdict["__class__"] = self.__class__.__name__
        #newdict.update({'__class__': __class__.__name__}) another way to write
        newdict["created_at"] = self.created_at.isoformat()
        newdict["updated_at"] = self.updated_at.isoformat()
        return newdict
