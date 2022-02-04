#!/usr/bin/env python3
""" Contains clase BasicCache """
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """ Definition of the class """

    def put(self, key, item):
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        return self.cache_data.get(key)
