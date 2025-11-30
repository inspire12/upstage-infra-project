from app.core.db import pool

def create_user(name: str, email: str):
    conn = pool.get_conn()
    try:
        with conn.cursor() as cursor:
            sql = """
                  INSERT INTO users (name, email)
                  VALUES (%s, %s)
                  """
            cursor.execute(sql, (name, email))
        conn.commit()
    finally:
        pool.release_connection(conn)


def get_user_by_email(email: str):
    conn = pool.get_conn()
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
        pool.release_connection(conn)


def update_user_name(user_id: int, new_name: str):
    conn = pool.get_conn()
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
        pool.release_connection(conn)


def delete_user_by_email(email: str):
    conn = pool.get_conn()
    try:
        with conn.cursor() as cursor:
            sql = "DELETE FROM users WHERE email = %s"
            cursor.execute(sql, (email,))
        conn.commit()
    finally:
        pool.release_connection(conn)

