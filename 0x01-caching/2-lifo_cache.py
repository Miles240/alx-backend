#!/usr/bin/env python3

"""LIFOCache Module"""


from base_caching import BaseCaching
from collections import OrderedDict


class LIFOCache(BaseCaching):
    """
    Contains the implementation of the caching methods
    """

    def __init__(self):
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """adds an item the cache"""
        if key is not None and item is not None:
            if key in self.cache_data:
                del self.cache_data[key]
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                last_item, _ = self.cache_data.popitem(last=True)
                print(f"DISCARD: {last_item}")
        self.cache_data[key] = item

    def get(self, key):
        """Get an item by key"""
        if key is None:
            return None
        return self.cache_data.get(key)
