from pydantic import BaseModel


class UserModel(BaseModel):
    username: str = None
    password: str = None
