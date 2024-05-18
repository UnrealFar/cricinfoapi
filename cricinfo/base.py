from __future__ import annotations

from typing import Dict, Any, TYPE_CHECKING
from collections import OrderedDict

import requests


class ModelCache(OrderedDict):
    def __init__(self, maxsize: int):
        super().__init__()
        self.maxsize = maxsize

    def __setitem__(self, key: int, value: BaseModel):
        if len(self) >= self.maxsize:
            self.popitem(last=False)
        super().__setitem__(key, value)

class BaseModel:

    if TYPE_CHECKING:
        model_cache: ModelCache[int, 'BaseModel']
        headers: Dict[str, str]
        session: requests.Session
        id: int
        json_url: str
        json: Dict[str, Any]

    models = {}
    headers = {'user-agent': 'Mozilla/5.0'}
    session = requests.Session()

    def __init_subclass__(cls) -> None:
        cls.model_cache = ModelCache(100)
        cls.models[cls.__name__] = cls

    def __new__(cls, *args, **kwargs) -> BaseModel:
        obj = super().__new__(cls)
        obj.__init__(*args, **kwargs)
        cls.model_cache[obj.id] = obj
        return obj

    def __repr__(self) -> str:
        return f'<{self.__class__.__name__} {self.name}>'

    @classmethod
    def get(cls, id: int) -> BaseModel:
        if id in cls.model_cache:
            return cls.model_cache[id]
        else:
            obj = cls(id)
            return obj

    def get_json(self, url: str) -> Dict[str, Any]:
        r = self.session.get(url, headers=self.headers)
        if r.status_code == 404:
            raise Exception('404 not found')
        else:
            return r.json()

    def update(self) -> None:
        self.json = self.get_json(self.json_url)
