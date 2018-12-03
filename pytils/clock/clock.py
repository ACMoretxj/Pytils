import time

from datetime import datetime

from ..oop import readonly


def now():
    """
    获取当前时间
    :return: 当前TimeZone的时间
    """
    return datetime.now()


def today():
    """
    获取今天的日期
    :return: 当前TimeZone的日期
    """
    return now().date()


class Stopwatch:

    def __init__(self):
        self.__start_time = None
        # milliseconds
        readonly(self, 'start_time', lambda: int(self.__start_time * 1000))

    def start(self):
        self.__start_time = time.time()
        return self

    @property
    def elapsed_time(self):
        if not self.__start_time:
            return 0
        return int((time.time() - self.__start_time) * 1000)


class TimeFormat:

    @staticmethod
    def from_millisecond(milli, fmt='%Y-%m-%d %H:%M:%S'):
        if milli is None:
            return None
        stamp = time.localtime(milli / 1000)
        return time.strftime(fmt, stamp)

    @staticmethod
    def from_datetime(dtm, fmt='%Y-%m-%d %H:%M:%S'):
        if dtm is None:
            return None
        dtm.strftime(fmt)
