#!/usr/bin/env python3
""" Contains a MRUCache class that inherits from basecaching """
BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """ Basic definition of the class """

    def __init__(self):
        """ Init method to initialize MRUCache """
        self.order = []
        super().__init__()

    def put(self, key, item):
        """ assign to the dictionary self.cache_data
        the item value for the key """
        if key and item:
            if self.cache_data.get(key):
                self.order.remove(key)
            while len(self.order) >= self.MAX_ITEMS:
                deleted = self.order.pop()
                self.cache_data.pop(deleted)
                print("DISCARD: {}".format(deleted))
            self.order.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """ return the value in self.cache_data linked to key """
        if self.cache_data.get(key):
            self.order.remove(key)
            self.order.append(key)
        return self.cache_data.get(key)
