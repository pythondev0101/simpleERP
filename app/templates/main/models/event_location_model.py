from datetime import datetime
from typing import Collection
from app import MONGO
from app.core.mongo_object import MongoObject



class EventLocation(MongoObject):
    _collection = MONGO.db.event_locations

    name: str
    description: str
    address: str
    date_start: datetime
    date_end: datetime


    def __init__(self, data=None):
        super(EventLocation, self).__init__(data=data)
        
        if data:
            self.__dict__.update(data)

