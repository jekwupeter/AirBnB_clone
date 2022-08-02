#!/usr/bin/python3
"""Defines base class for other classes"""
import uuid
from datetime import datetime
import time

class BaseModel:
    """
    Defines all common attributes/ methods for other classes
    """
    def __init__(self):
        """
        initializes instance attributes
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def save(self):
        """
        updates the public instance attribute update_at with the current datetime
        """
        setattr(self, "updated_at", datetime.now())
        print("=====>>>>>",self.updated_at)

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values of __dict__ of instance
        """
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