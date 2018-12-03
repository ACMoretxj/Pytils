import socket
from functools import lru_cache

from aiohttp import ClientSession

from .exception import IPTransformException
from ..oop import readonly


@lru_cache()
def localhost():
    """
    Get the ipv4 address (dot-decimal format) of current machine.
    :return: local ip
    """
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as skt:
        skt.connect(('8.8.8.8', 80))
        ip = skt.getsockname()[0]
        return ip


class IPLocation:

    def __init__(self, ip: str):
        self.__country = None
        self.__province = None
        self.__city = None
        # properties
        readonly(self, 'UNDEFINED', lambda: 'XX')
        readonly(self, 'ip', lambda: ip)
        readonly(self, 'country', lambda: '中国' if self.__country is None else self.__country)
        readonly(self, 'province', lambda: '北京市' if self.__city is None else self.__city)
        readonly(self, 'city', lambda: '海淀区' if self.__city is None else self.__city)

    def __repr__(self):
        return 'Country: %s, Province: %s, City: %s' % (self.country, self.province, self.city)

    def __extract(self, field):
        return None if field == self.UNDEFINED else field

    async def transform(self):
        if self.country or self.province or self.city:
            return
        async with ClientSession() as session:
            async with session.get('http://ip.taobao.com//service/getIpInfo.php?ip=%s' % self.ip) as resp:
                if resp.status != 200:
                    return
                desc = await resp.json()
                if desc['code'] != 0:
                    raise IPTransformException(ip=self.ip)
                self.__country = self.__extract(desc['data']['country'])
                self.__province = self.__extract(desc['data']['region'])
                self.__city = self.__extract(desc['data']['city'])
