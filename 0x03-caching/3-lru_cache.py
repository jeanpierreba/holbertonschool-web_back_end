#!/usr/bin/env python3
""" Contains a LRUCache class """
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """ Definition of the class """

    def __init__(self):
        self.order = []
        super().__init__()

    def put(self, key, item):
        if key and item:
            if self.cache_data.get(key):
                self.order.remove(key)
            self.order.append(key)
            self.cache_data[key] = item
            if len(self.order) > self.MAX_ITEMS:
                deleted = self.order.pop(0)
                self.cache_data.pop(deleted)
                print("DISCARD: {}".format(deleted))

    def get(self, key):
        if self.cache_data.get(key):
            self.order.remove(key)
            self.order.append(key)
        return self.cache_data.get(key)
