#!/usr/bin/env python3
""" MongoDB Ops with Python via pymongo """

def update_topics(mongo_collection, name, topics):
    """changes all topics of a school doc based on the name """
    query = {"name": name}
    new_values = {"$set": {"topics": topics}}

    mongo_collection.update_many(query, new_values)
