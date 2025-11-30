from app.core.db import get_conn, release_conn


def create_user(name: str, email: str):
    conn = get_conn()
    try:
        with conn.cursor() as cursor:
            sql = """
                  INSERT INTO users (name, email)
                  VALUES (%s, %s)
                  """
            cursor.execute(sql, (name, email))
        conn.commit()
    finally:
        release_conn(conn)


def get_user_by_email(email: str):
    conn = get_conn()
    try:
        with conn.cursor() as cursor:
            sql = """
                  SELECT id, name, email, created_at
                  FROM users
                  WHERE email = %s
                  """
            cursor.execute(sql, (email,))
            return cursor.fetchone()
    finally:
        release_conn(conn)


def update_user_name(user_id: int, new_name: str):
    conn = get_conn()
    try:
        with conn.cursor() as cursor:
            sql = """
                  UPDATE users
                  SET name = %s
                  WHERE id = %s
                  """
            cursor.execute(sql, (new_name, user_id))
        conn.commit()
    finally:
        release_conn(conn)


def delete_user_by_email(email: str):
    conn = get_conn()
    try:
        with conn.cursor() as cursor:
            sql = "DELETE FROM users WHERE email = %s"
            cursor.execute(sql, (email,))
        conn.commit()
    finally:
        release_conn(conn)

