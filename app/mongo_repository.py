from gc import collect
from statistics import mode
from bson import ObjectId
from pymongo.collection import Collection



class MongoRepository(object):
    @staticmethod
    def retrieve(model: any, id: str):
        collection: Collection = model._collection
        return collection.find_one({'_id': ObjectId(id)})
    
    
    @staticmethod
    def save(model: any):
        collection: Collection = model._collection
        return collection.insert_one(model.__dict__)
    
    
    @staticmethod
    def create(model: any, data):
        collection: Collection = model._collection
        return collection.insert_one(data)
    
    
    @staticmethod
    def find_one(model: any, filter):
        collection: Collection = model._collection
        return collection.find_one(filter)
    
    
    @staticmethod
    def find_many(model: any, filter):
        collection: Collection = model._collection
        return collection.find(filter)
    
    @staticmethod
    def count(model: any, filter):
        collection: Collection = model._collection
        return collection.find(filter).count()