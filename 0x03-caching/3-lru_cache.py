#!/usr/bin/env python3
""" Contains a LRUCache class that inherits from basecaching """
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """ Basic Definition of the class """

    def __init__(self):
        """ Init method to initialize LRUCache """
        self.order = []
        super().__init__()

    def put(self, key, item):
        """ assign to the dictionary self.cache_data
        the item value for the key """
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
        """ return the value in self.cache_data linked to key """
        if self.cache_data.get(key):
            self.order.remove(key)
            self.order.append(key)
        return self.cache_data.get(key)
