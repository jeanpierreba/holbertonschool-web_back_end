#!/usr/bin/env python3
""" Contains a LIFOCache class that inherits from basecaching """
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """ Basic definition of the class """

    def __init__(self):
        """ Init method to initialize LIFOCache """
        self.keysIndex = ""
        super().__init__()

    def put(self, key, item):
        """ assign to the dictionary self.cache_data
        the item value for the key """
        if key and item:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                print("DISCARD: {}".format(self.keysIndex))
                del(self.cache_data[self.keysIndex])
            self.keysIndex = key

    def get(self, key):
        """ return the value in self.cache_data linked to key """
        if key in self.cache_data:
            return self.cache_data[key]
        return None
