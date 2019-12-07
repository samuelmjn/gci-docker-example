import pymongo


class ToDo(object):
    def __init__(self, title):
        self.title = title
    

class ToDoRepository(object):
    def __init__(self, mongo_client: pymongo.MongoClient, db_name: str, col_name: str):
        self.mongo_client = mongo_client
        self.collection = self.mongo_client[db_name][col_name]

    def create(self, req: ToDo):
        document = req.__dict__
        _ = self.collection.insert_one(document)

    def find_all(self):
        res = self.collection.find()
        return res