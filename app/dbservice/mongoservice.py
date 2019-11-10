import json
from pymongo import MongoClient
from bson.json_util import dumps


class MongoService(object):
    def __init__(self, database, host='localhost', port=27017):
        self.client = MongoClient(host, port)
        self.db = self.client[database]

    def create(self, obj):
        pass

    def findall(self):
        pass

    def find(self,selector):
        pass

    def delete(self,obj):
        pass

    def update(self,obj,update):
        pass

    def deleteFromCollection(self,collection,obj):
        pass

    def findInCollection(self,collection,selector):
        mcollection = self.db[collection]
        record = self.db[collection].find_one(selector)

        return record

    def findAllCollection(self, collection):
        records = []
        cursor = self.db[collection].find()

        for record in cursor:
            records.append(dumps(record))

        return records
        
    def addToCollection(self, collection, obj):
        mcollection = self.db[collection]
        post_id = mcollection.insert_one(obj).inserted_id

        return post_id

def main():
    ms = MongoService('testdb')

    with open('host.json') as fd:
        data = json.load(fd)
        #print(ms.addToCollection('hosts',data))
        print(json.dumps(ms.findAllCollection('hosts')))
        #print(ms.findInCollection('hosts',json.loads('{\"hostname\":\"unassigned-hostname\"}')))


if __name__ == "__main__":
    main()
