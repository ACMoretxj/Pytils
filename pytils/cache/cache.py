from abc import ABCMeta, abstractmethod
from enum import Enum

import redis

from ..oop import readonly
from ..decorator import singleton


class Cache(metaclass=ABCMeta):
    """
    TODO: add dict like behavior, like cache[...]
    """

    def __init__(self, *args, **kwargs):
        pass

    @abstractmethod
    def set(self, key, value):
        pass

    @abstractmethod
    def get(self, key, default=None):
        pass


class CacheKey(Enum, metaclass=ABCMeta):
    pass


@singleton
class RedisCache(Cache):
    """
    Cache mechanism based on redis.
    You shall not pass the instance between processes, instead, just instantiate a
    new instance because the class is singleton.
    """
    def __init__(self, host, port, password=None):
        super().__init__(host=host, port=port, password=password)
        self.__cache = redis.Redis(host=host, port=port, password=password,
                                   decode_responses=True)
        # properties
        readonly(self, 'host', lambda: host)
        readonly(self, 'port', lambda: port)
        readonly(self, 'password', lambda: port)

    def set(self, key, value, **kwargs):
        try:
            self.__cache.set(name=key, value=value, **kwargs)
            return True
        except (ConnectionError, TimeoutError):
            return False

    def get(self, key, default=None):
        value = default
        try:
            value = self.__cache.get(key)
        except (ConnectionError, TimeoutError):
            pass
        return value


@singleton
class LocalCache(Cache):

    def __init__(self):
        super().__init__()
        self.__cache = {}

    def set(self, key, value, **kwargs):
        self.__cache[key] = value
        self.__cache.update(**kwargs)
        return True

    def get(self, key, default=None):
        return self.__cache.get(key, default)
