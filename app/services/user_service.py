
from app.interfaces.user_service_interface import UserServiceInterface
from app.interfaces.user_repository_interface import UserRepositoryInterface

class UserService(UserServiceInterface):

    def __init__(self, repository: UserRepositoryInterface):
        self.repository = repository

    def create_user(self, user_data: dict) -> dict:
        return self.repository.create(user_data)

    def get_users(self):
        return self.repository.get_all()

    def update_user(self, user_id: int, user_data: dict):
        return self.repository.update(user_id, user_data)

    def delete_user(self, user_id: int):
        return self.repository.delete(user_id)
