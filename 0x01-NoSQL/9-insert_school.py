#!/usr/bin/env python3
""" MongoDB operations with python using pymongo """

def insert_school(mongo_collection, **kwargs):
    """ inserts a new document in a collection based on kwargs """
    document_id = mongo_collection.insert(kwargs)
    return document_id
