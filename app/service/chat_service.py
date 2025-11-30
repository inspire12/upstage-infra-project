# app/service/chat_service.py
from app.models.role import Role
from app.repository.chat_repository import (
  add_conversation,
  get_recent_conversations as repo_get_recent_conversations,
)
from app.repository.chat_repository import (
  save_chat_transaction as repo_save_chat_tx,
  save_chat_transaction_fail as repo_save_chat_tx_fail,
)


def add_user_message(user_id: int, message: str):
  add_conversation(user_id, Role.user.name, message)


def add_assistant_message(user_id: int, message: str):
  add_conversation(user_id, Role.assistant.name, message)


def get_recent_conversations(user_id: int, limit: int = 20):
  return repo_get_recent_conversations(user_id, limit).to_dict()


def save_chat_transaction(user_id: int, user_msg: str, assistant_msg: str):
  repo_save_chat_tx(user_id, user_msg, assistant_msg)


def save_chat_transaction_fail(user_id: int, user_msg: str, assistant_msg: str):
  repo_save_chat_tx_fail(user_id, user_msg, assistant_msg)
