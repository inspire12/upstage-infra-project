
from app.service.user_service import (
  create_user,
  get_user_by_email,
  update_user_name,
  delete_user_by_email,
)
from app.service.chat_service import (
  add_conversation,
  get_recent_conversations,
  save_chat_transaction,
  save_chat_transaction_fail,
)
from app.models.role import Role


def run_user_crud_demo():
  # 1. 유저 생성
  # create_user("hak", "ox4443@naver.com")

  # 2. 조회
  user = get_user_by_email("ox4443@naver.com")
  print("created user:", user)
  #
  # # 3. 이름 변경
  # update_user_name(user["id"], "yeong")
  # replaced = get_user_by_email("ox4443@naver.com")
  # print("updated user:", replaced)
  #
  # # 4. 삭제
  # delete_user_by_email("ox4443@naver.com")
  # print("after delete:", get_user_by_email("ox4443@naver.com"))


def run_chat_demo():
  # 정상 트랜잭션
  save_chat_transaction(1, "뭐해?", "그냥 있어요")
  print("after success:", get_recent_conversations(1, 2))

  # 실패 트랜잭션 (롤백 확인)
  try:
    save_chat_transaction_fail(1, "뭐라고?", "그냥 있다고요")
  except Exception:
    print("save_chat_transaction_fail 에서 예외 발생 (롤백됨)")

  print("after fail:", get_recent_conversations(1, 2))

  # 단일 대화 추가 예제
  add_conversation(1, Role.user.name, "추가 질문?")
  print("after add_conversation:", get_recent_conversations(1, 3))