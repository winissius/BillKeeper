from pymongo import MongoClient

client = MongoClient('localhost', 27017)

db = client['test']
collections = db['bills']


def show_all_db():
    query = collections.find()
    for document in query:
        print(document)


def add_bill(json_bill):
    collections.insert_one(json_bill)


def delete_bill(json_bill):
    collections.delete_one(json_bill)


def update_bill(json_reference, json_new):
    collections.update_one(json_reference, json_new)
