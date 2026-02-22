
from typing import List
from app.interfaces.user_repository_interface import UserRepositoryInterface

class UserRepository(UserRepositoryInterface):

    def __init__(self):
        self.users = {}
        self.counter = 1

    def create(self, user_data: dict) -> dict:
        user_data["id"] = self.counter
        self.users[self.counter] = user_data
        self.counter += 1
        return user_data

    def get_all(self) -> List[dict]:
        return list(self.users.values())

    def get_by_id(self, user_id: int) -> dict:
        return self.users.get(user_id)

    def update(self, user_id: int, user_data: dict) -> dict:
        if user_id in self.users:
            self.users[user_id].update(user_data)
            return self.users[user_id]
        return None

    def delete(self, user_id: int) -> bool:
        if user_id in self.users:
            del self.users[user_id]
            return True
        return False
