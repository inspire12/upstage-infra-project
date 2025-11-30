# app/service/user_service.py
from app.repository import user_repository


def create_user(name: str, email: str):
  # 나중에 여기서 validation, 비즈니스 규칙 추가 가능
  user_repository.create_user(name, email)


def get_user_by_email(email: str):
  return user_repository.get_user_by_email(email)


def update_user_name(user_id: int, new_name: str):
  user_repository.update_user_name(user_id, new_name)


def delete_user_by_email(email: str):
  user_repository.delete_user_by_email(email)
