from cache_strategy_interface import CacheStrategy

class CacheManager:
    def __init__(self, strategy: CacheStrategy):
        self.strategy = strategy

    def set_strategy(self, strategy: CacheStrategy):
        self.strategy = strategy

    def store(self, key, value):
        self.strategy.store(key, value)

    def retrieve(self, key):
        return self.strategy.retrieve(key)
