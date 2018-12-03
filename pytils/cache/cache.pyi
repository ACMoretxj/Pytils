from abc import ABCMeta, abstractmethod
from enum import Enum
from typing import Any, Dict

from redis import Redis

from ..decorator import singleton


class Cache(metaclass=ABCMeta):
    def __init__(self, *args, **kwargs): pass
    @abstractmethod
    def set(self, key: str, value: Any) -> bool: pass
    @abstractmethod
    def get(self, key: str, default: Any=None) -> Any: pass

class CacheKey(Enum, metaclass=ABCMeta):
    pass

# noinspection PyMissingConstructor
@singleton
class RedisCache(Cache):
    __cache: Redis

    host: str
    port: int
    password: str

    def __init__(self, host: str, port: int, password=None): pass
    def set(self, key: str, value: Any, **kwargs) -> bool: pass
    def get(self, key: str, default: Any=None) -> Any: pass


# noinspection PyMissingConstructor
@singleton
class LocalCache(Cache):
    __cache: Dict
    def __init__(self): pass
    def set(self, key: str, value: Any, **kwargs) -> bool: pass
    def get(self, key: str, default: Any=None) -> Any: pass
