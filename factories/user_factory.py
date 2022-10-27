from helper_enums.user_enum import UserEnum
from models.user_model import UserModel


class UserFactory:

    @staticmethod
    def get_user(user: UserEnum):
        if user == UserEnum.ADMIN:
            return UserModel(username="Admin", password="admin123")
        if user == UserEnum.COGNITO:
            return UserModel(username="random", password="random")
