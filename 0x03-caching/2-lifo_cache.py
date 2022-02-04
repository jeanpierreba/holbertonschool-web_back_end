#!/usr/bin/env python3
""" Contains a LIFOCache class """
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """ definition of the class """

    def __init__(self):
        self.keysIndex = []
        super().__init__()

    def put(self, key, item):
        if key and item:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                if key in self.cache_data:
                    del self.cache_data[key]
                    self.keysIndex.remove(key)
                else:
                    del self.cache_data[self.keysIndex[
                        BaseCaching.MAX_ITEMS - 1]]
                    discardedItem = self.keysIndex.pop(
                        BaseCaching.MAX_ITEMS - 1)
                    print("DISCARD: {}".format(discardedItem))
            self.cache_data[key] = item
            self.keysIndex.append(key)

    def get(self, key):
        if key in self.cache_data:
            return self.cache_data[key]
        return None
