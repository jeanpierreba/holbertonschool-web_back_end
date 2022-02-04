#!/usr/bin/env python3
""" Contains a LIFOCache class that inherits from basecaching """
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """ Basic definition of the class """

    def __init__(self):
        """ Init method to initialize LIFOCache """
        self.keysIndex = []
        super().__init__()

    def put(self, key, item):
        """ assign to the dictionary self.cache_data
        the item value for the key """
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
        """ return the value in self.cache_data linked to key """
        if key in self.cache_data:
            return self.cache_data[key]
        return None
