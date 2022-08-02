#!/usr/bin/python3
"""Defines base class for other classes"""
import uuid
from datetime import datetime
import time

class BaseModel:
    """
    Defines all common attributes/ methods for other classes
    """
    def __init__(self, *args, **kwargs):
        """
        initializes instance attributes

        Args:
            args: NOT USED
            kwargs: contains attributes to be added to instance
        """
        fmt = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs is None or kwargs == {}:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        else:
            for k, v in kwargs.items():
                if k != "__class__":
                    if k == "created_at" or k == "updated_at":
                        strptime_v = datetime.strptime(v, fmt)
                        setattr(self, k, strptime_v)
                    else:
                        setattr(self, k, v)

    def save(self):
        """
        updates the public instance attribute update_at with the current datetime
        """
        setattr(self, "updated_at", datetime.now())

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values of __dict__ of instance
        """
        self.save()
        dict_tmp = self.__dict__.copy()
        dict_tmp["updated_at"] = self.updated_at.isoformat()
        dict_tmp["created_at"] = self.created_at.isoformat()
        dict_tmp["__class__"] = self.__class__.__name__
        return dict_tmp

    def __str__(self):
        """
        returns the string format of base class
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"