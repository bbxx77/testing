from cache_strategy_interface import CacheStrategy
from collections import OrderedDict

class LRUCacheStrategy(CacheStrategy):
    def __init__(self, max_size):
        self.max_size = max_size
        self.cache = OrderedDict()

    def store(self, key, value):
        if key in self.cache:
            self.cache.move_to_end(key)
        elif len(self.cache) >= self.max_size:
            self.cache.popitem(last=False)
        self.cache[key] = value

    def retrieve(self, key):
        if key in self.cache:
            self.cache.move_to_end(key)
            return self.cache[key]
        else:
            return None

class FIFOCacheStrategy(CacheStrategy):
    def __init__(self, max_size):
        self.max_size = max_size
        self.cache = OrderedDict()

    def store(self, key, value):
        if len(self.cache) >= self.max_size:
            self.cache.popitem(last=False)
        self.cache[key] = value

    def retrieve(self, key):
        return self.cache.get(key, None)

