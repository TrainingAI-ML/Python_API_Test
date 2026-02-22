
from fastapi import APIRouter, Depends, HTTPException
from app.services.user_service import UserService
from app.repositories.user_repository import UserRepository
from app.models.user_model import UserCreate, UserUpdate

router = APIRouter()

def get_user_service():
    repository = UserRepository()
    return UserService(repository)

@router.post("/users")
def create_user(user: UserCreate, service: UserService = Depends(get_user_service)):
    return service.create_user(user.dict())

@router.get("/users")
def get_users(service: UserService = Depends(get_user_service)):
    return service.get_users()

@router.put("/users/{user_id}")
def update_user(user_id: int, user: UserUpdate, service: UserService = Depends(get_user_service)):
    updated = service.update_user(user_id, user.dict(exclude_unset=True))
    if not updated:
        raise HTTPException(status_code=404, detail="User not found")
    return updated

@router.delete("/users/{user_id}")
def delete_user(user_id: int, service: UserService = Depends(get_user_service)):
    deleted = service.delete_user(user_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User deleted"}
