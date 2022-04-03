from pymongo import MongoClient
from config import MONGO_CONFIG


class MongoHelper(object):
    def __init__(self):
        self.client = MongoClient(
            host=MONGO_CONFIG.get('ip', '127.0.0.1'), port=MONGO_CONFIG.get('port', 27017), authSource=MONGO_CONFIG.get('db', 'proxy')
        )
        self.init_db()

    def serializer(self, proxys):
        for p in proxys:
            p['_id'] = str(p.get('_id'))

    def init_db(self):
        self.db = self.client[MONGO_CONFIG.get('db', 'proxy')]
        self.collection = self.db[MONGO_CONFIG.get('collection', 'proxys')]

    def insert_one(self, obj):
        if obj:
            self.collection.insert_one(obj)

    def insert_many(self, objs):
        if objs:
            self.collection.insert_many(objs)

    def update(self, condition, attr):
        if condition and attr:
            self.collection.update_one(condition, {'$set': attr})

    def find_all(self, condition=None):
        result = list(self.collection.find(condition))
        self.serializer(result)
        return result

    def find_one(self, condition):
        result = self.collection.find_one(condition)
        if not result:
            return
        return self.serializer(result)
