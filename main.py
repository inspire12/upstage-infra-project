import pymysql
from pymysql import cursors

from connection_pool import PymysqlConnectionPool

pool = PymysqlConnectionPool(
  maxsize=5,
  host="localhost",
  port=3306,
  user="root",
  password="password",
  database="llmagent",
)


def connection():
    conn = pool.get_conn()
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT 1")
            row = cursor.fetchone()
            print(row)
    finally:
        pool.release_connection(conn)


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


if __name__ == '__main__':
    # connection()
    # create_user('hak', 'ox4443@naver.com')
    for i in range(100):
        print(get_user_by_email('ox4443@naver.com'))

