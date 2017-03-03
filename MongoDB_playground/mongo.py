from pymongo import *
from pprint import pprint

client = MongoClient()
db = client.get_database('company')
collection = db.get_collection('company_profile')
cursor = collection.find({})
for document in cursor:
    pprint(document)
