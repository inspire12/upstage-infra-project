from app.core.db import release_conn, get_conn
from app.models.conversation import Conversation
from app.models.role import Role


def add_conversation(user_id: int, role: str, message: str):
    conn = get_conn()
    try:
        role_enum = Role(role)  # 'user' -> Role.user
        conv = Conversation(
            user_id=user_id,
            role=role_enum,
            message=message,
        )
        conn.add(conv)
        conn.commit()
        conn.refresh(conv)
        return conv
    finally:
        release_conn(conn)


def get_recent_conversations(user_id: int, limit: int = 20):
    conn = get_conn()
    try:
        return (
            conn.query(Conversation)
            .filter(Conversation.user_id == user_id)
            .order_by(Conversation.created_at.desc())
            .limit(limit)
            .all()
        )
    finally:
        release_conn(conn)


def save_chat_transaction(user_id: int, user_msg: str, assistant_msg: str):
    conn = get_conn()
    try:
        user_conversation = Conversation(
            user_id=user_id,
            role=Role.user,
            message=user_msg,
        )
        assistant_conversation = Conversation(
            user_id=user_id,
            role=Role.assistant,
            message=assistant_msg,
        )

        conn.add(user_conversation)
        conn.add(assistant_conversation)

        conn.commit()
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        release_conn(conn)


def save_chat_transaction_fail(user_id: int, user_msg: str, assistant_msg: str):
    conn = get_conn()
    try:
        user_conversation = Conversation(
            user_id=user_id,
            role=Role.user,
            message=user_msg,
        )
        conn.add(user_conversation)

        # 일부러 잘못된 값으로 ENUM 오류 발생 유도
        broken_conversation = Conversation(
            user_id=user_id,
            role="wrong",  # Role enum에 없는 값
            message=assistant_msg,
        )
        conn.add(broken_conversation)

        conn.commit()
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        release_conn(conn)
