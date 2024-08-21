#!/usr/bin/env python3

"""FIFOCache Module"""

from base_caching import BaseCaching
from collections import OrderedDict


class FIFOCache(BaseCaching):
    """
    Contains the implementation of the caching methods
    """

    def __init__(self):
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """adds an item the cache"""
        if key is not None:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                first_key, _ = self.cache_data.popitem(last=False)
                print(f"DISCARD: {first_key}")
        return

    def get(self, key):
        """Gets an item based off the key"""
        if key is None:
            return None
        return self.cache_data.get(key)
