from datetime import datetime
from bson import ObjectId
import pymongo
from pymongo.collection import Collection
from app.mongo_repository import MongoRepository



class MongoObject(object):
    _collection: Collection
    _filter: dict = {}

    _id: ObjectId
    date_created: datetime = None

    def __init__(self, data=None, **params):
        if data:
            self._id = data.get('_id')
            self.date_created = data.get('date_created')
            
        if 'filter' in params:
            self._filter = params['filter']

        
    @property
    def id(self):
        return str(self._id)


    @property
    def str_date_created(self):
        if self.date_created is None:
            return ''
        return str(self.date_created)
        

    def __repr__(self):
        return str(self.__dict__)


    def count(self, filter=None):
        if filter is None:
            query = MongoRepository.count(self._filter)
        else:
            query = MongoRepository.count(filter)
        return query


    @classmethod
    def create(cls, data):
        MongoRepository.create(cls, data)
        return cls(data)
        

    @classmethod
    def retrieve(cls, id: str):
        query = MongoRepository


    @classmethod
    def find_one(cls, filter):
        query = MongoRepository.find_one(cls, filter)
        return cls(data=query)


    @classmethod
    def find_many(cls, filter, **params):
        query = MongoRepository.\
            find_many(cls, filter).\
                sort('date_created', pymongo.DESCENDING)
        
        if 'skip' in params:
            query.skip(params['skip'])
        
        if 'limit' in params:
            query.limit(params['limit'])
        
        if query is None:
            return []
        
        arr = []
        for x in query:
            arr.append(cls(data=x))
            
        return arr
    
    # def _mongo_decorator():
        