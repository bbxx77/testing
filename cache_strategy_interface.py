from abc import ABC, abstractmethod

class CacheStrategy(ABC):
    @abstractmethod
    def store(self, key, value):
        pass

    @abstractmethod
    def retrieve(self, key):
        pass
