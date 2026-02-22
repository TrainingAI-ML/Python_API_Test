
from abc import ABC, abstractmethod
from typing import List

class UserServiceInterface(ABC):

    @abstractmethod
    def create_user(self, user_data: dict) -> dict:
        pass

    @abstractmethod
    def get_users(self) -> List[dict]:
        pass

    @abstractmethod
    def update_user(self, user_id: int, user_data: dict) -> dict:
        pass

    @abstractmethod
    def delete_user(self, user_id: int) -> bool:
        pass
