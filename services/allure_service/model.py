from dataclasses import dataclass, asdict
from json import dumps
from typing import List


@dataclass
class ResultRequestFile:
    content_base64: str
    file_name: str


@dataclass
class AllureUser:
    username: str
    password: str


@dataclass
class PostSendResultRequest:
    results: List[ResultRequestFile] = None

    @property
    def __dict__(self):
        """
        get a python dictionary
        """
        return asdict(self)

    @property
    def json(self):
        """
        get the json formated string
        """
        return dumps(self.__dict__)
