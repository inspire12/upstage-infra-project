import pymysql
from pymysql import cursors

def connection():
    conn = pymysql.connect(
        host="localhost",
        port=3306,
        user="tester",
        password="tester",
        database="llmagent",
        charset="utf8mb4",
        cursorclass=pymysql.cursors.DictCursor,
    )

    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT 1")
            row = cursor.fetchone()
            print(row)
    finally:
        conn.close()


def create_user(name: str, email: str):
    conn = pymysql.connect(
        host="localhost",
        port=3306,
        user="root",
        password="password",
        database="llmagent",
        charset="utf8mb4",
        cursorclass=pymysql.cursors.DictCursor,
    )
    try:
        with conn.cursor() as cursor:
            sql = """
                  INSERT INTO users (name, email)
                  VALUES (%s, %s) \
                  """
            cursor.execute(sql, (name, email))
        conn.commit()
    finally:
        conn.close()


def get_user_by_email(email: str):
    conn = pymysql.connect(
        host="localhost",
        port=3306,
        user="root",
        password="password",
        database="llmagent",
        charset="utf8mb4",
        cursorclass=pymysql.cursors.DictCursor,
    )
    try:
        with conn.cursor() as cursor:
            sql = """
                  SELECT id, name, email, created_at
                  FROM users
                  WHERE email = %s \
                  """
            cursor.execute(sql, (email,))
            return cursor.fetchone()
    finally:
        conn.close()


if __name__ == '__main__':
    # connection()
    # create_user('hak', 'ox4443@naver.com')
    print(get_user_by_email('ox4443@naver.com'))

