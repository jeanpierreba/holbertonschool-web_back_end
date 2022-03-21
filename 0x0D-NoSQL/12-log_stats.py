#!/usr/bin/env python3
""" Contains a python script that provides
some stats about Nginx logs stored in MongoDB """

from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017').logs.nginx
    print(f'{client.count_documents({})} logs')
    print('Methods:')
    print(f'\tmethod GET: {client.count_documents({"mehotd": "GET"})}')
    print(f'\tmethod POST: {client.count_documents({"mehotd": "POST"})}')
    print(f'\tmethod PUT: {client.count_documents({"mehotd": "PUT"})}')
    print(f'\tmethod PATCH: {client.count_documents({"mehotd": "PATCH"})}')
    print(f'\tmethod DELETE: {client.count_documents({"mehotd": "DELETE"})}')
    print(f'{client.count_documents({"path": "/status"})} status check')
