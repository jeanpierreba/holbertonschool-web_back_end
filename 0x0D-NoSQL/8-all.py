#!/usr/bin/env python3
""" Contains a python function that lists all documents in a collection """


def list_all(mongo_collection):
    """ Lists all documents in a collection """
    return mongo_collection.find()
