from bson import ObjectId
from pymongo.collection import Collection
from app.mongo_repository import MongoRepository



class BaseModel(object):
    _id: ObjectId
    _collection: Collection

    @property
    def id(self):
        return str(self._id)
    

    def __init__(self, data=None):
        if data:
            self.__dict__.update(data)
        

    def __repr__(self):
        return str(self.__dict__)


    def save(self):
        query = MongoRepository.save(self)
        return query

    @classmethod
    def retrieve(cls, id: str):
        query = MongoRepository


    @classmethod
    def find_one(cls, search):
        query = MongoRepository.find_one(cls, search)
        return cls(data=query)
