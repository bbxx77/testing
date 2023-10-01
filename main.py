from cache_strategy import LRUCacheStrategy, FIFOCacheStrategy
from cache_manager import CacheManager
lru_cache = LRUCacheStrategy(max_size=3)
fifo_cache = FIFOCacheStrategy(max_size=2)

cache_manager = CacheManager(lru_cache)

cache_manager.store("key1", "value1")
cache_manager.store("key2", "value2")
cache_manager.store("key3", "value3")

print(cache_manager.retrieve("key2"))

cache_manager.set_strategy(fifo_cache)

cache_manager.store("key4", "value4")

print(cache_manager.retrieve("key1"))
print(cache_manager.retrieve("key4"))