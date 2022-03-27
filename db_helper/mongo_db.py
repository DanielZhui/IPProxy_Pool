from pymongo import MongoClient


class MongoHelper(object):
    def __init__(self):
        self.client = MongoClient(host='127.0.0.1', port=27017, username='root', password='admin', authSource='test')
        self.init_db()

    def serializer(self, proxys):
        for p in proxys:
            p['_id'] = str(p.get('_id'))

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
        result = list(self.collection.find())
        self.serializer(result)
        return result

    def find_one(self, condition):
        result = self.collection.find_one(condition)
        if not result:
            return
        return self.serializer(result)
