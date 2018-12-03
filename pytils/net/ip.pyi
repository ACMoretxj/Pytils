from typing import Coroutine


def localhost() -> str: pass

class IPLocation:
    __country: str
    __province: str
    __city: str
    # properties
    UNDEFINED: str
    ip: str
    country: str
    province: str
    city: str
    def __init__(self, ip: str): pass
    def __repr__(self) -> str: pass
    def __extract(self, field: str) -> str: pass
    async def transform(self) -> Coroutine: pass
