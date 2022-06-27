from bson import ObjectId
from pymongo.collection import Collection


class MongoRepository:
    @staticmethod
    def retrieve(model: any, id: str):
        collection: Collection = model._collection
        return collection.find_one({'_id': ObjectId(id)})
    
    
    @staticmethod
    def save(model: any):
        collection: Collection = model._collection
        return collection.insert_one(model.__dict__)
    
    
    @staticmethod
    def find_one(model: any, query):
        collection: Collection = model._collection
        return collection.find_one(query)
    
    
    