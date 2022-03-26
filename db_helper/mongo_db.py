from pymongo import MongoClient


class MongoHelper(object):
    def __init__(self):
        self.client = MongoClient(host='127.0.0.1', port=27017, username='root', password='admin', authSource='test')
        self.init_db()

    def init_db(self):
        self.db = self.client.test
        self.collection = self.db.proxys

    def insert_one(self, obj):
        if obj:
            self.collection.insert_one(obj)

    def insert_many(self, objs):
        if objs:
            self.collection.insert_many(objs)

    def update(self, condition, attr):
        if condition and attr:
            self.collection.update_one(condition, {'$set': attr})

    def find_all(self):
        return list(self.collection.find())

    def find_one(self, condition):
        return self.collection.find_one(condition)
