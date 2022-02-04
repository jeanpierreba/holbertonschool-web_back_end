#!/usr/bin/env python3
""" Contains a FIFOCache class """
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """ definition of the class """

    def __init__(self):
        self.keysIndex = []
        super().__init__()

    def put(self, key, item):
        if key and item:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                discardedItem = self.keysIndex.pop(0)
                del self.cache_data[discardedItem]
                print("DISCARD: {}".format(discardedItem))
            self.cache_cata[key] = item
            self.keysIndex.append(key)

    def get(self, key):
        if key in self.cache_data:
            return self.cache_data[key]
        return None
