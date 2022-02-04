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
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                discardedItem = self.keysIndex.pop(0)
                del self.cache_data[discardedItem]
                print("DISCARD: {}".format(discardedItem))
            self.cache_cata[key] = item
            self.keysIndex.append(key)

    def get(self, key):
        """ return the value in self.cache_data linked to key """
        if key in self.cache_data:
            return self.cache_data[key]
        return None
