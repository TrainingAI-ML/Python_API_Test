
from abc import ABC, abstractmethod
from typing import List

class UserRepositoryInterface(ABC):

    @abstractmethod
    def create(self, user_data: dict) -> dict:
        pass

    @abstractmethod
    def get_all(self) -> List[dict]:
        pass

    @abstractmethod
    def get_by_id(self, user_id: int) -> dict:
        pass

    @abstractmethod
    def update(self, user_id: int, user_data: dict) -> dict:
        pass

    @abstractmethod
    def delete(self, user_id: int) -> bool:
        pass
