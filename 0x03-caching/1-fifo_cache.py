#!/usr/bin/env python3
""" Contains a FIFOCache class that inherits from basecaching """
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """ Basic definition of the class """

    def __init__(self):
        """ Init method to initialize FIFOCache """
        self.keysIndex = []
        super().__init__()

    def put(self, key, item):
        """ assign to the dictionary self.cache_data
        the item value for the key """
        if key and item:
            if self.cache_data.get(key):
                self.keysIndex.remove(key)
            self.keysIndex.append(key)
            self.cache_data[key] = item
            if len(self.keysIndex) > self.MAX_ITEMS:
                deleted = self.keysIndex.pop(0)
                self.cache_data.pop(deleted)
                print("DISCARD: {}".format(deleted))

    def get(self, key):
        """ return the value in self.cache_data linked to key """
        if key in self.cache_data:
            return self.cache_data[key]
        return None
