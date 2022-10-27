from pydantic import BaseModel


class Config(BaseModel):
    browser: str = None
    url: str = None
    headless: bool = None
    language: str = None
    localrun: str = None
