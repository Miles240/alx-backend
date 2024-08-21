#!/usr/bin/env python3

"""BasicCache Module"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    Contains the implementation of the caching methods
    """

    def put(self, key, item):
        """Adds an item to the cache"""
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """Gets an item by key"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data.get(key)
