import os

from app.core.connection_pool import PymysqlConnectionPool
from dotenv import load_dotenv

load_dotenv()

pool = PymysqlConnectionPool(
    maxsize=5,
    host="localhost",
    port=3306,
    user=os.getenv('db_user'),
    password=os.getenv('db_password'),
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


# app/core/db.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "mysql+pymysql://root:password@localhost:3306/llmagent?charset=utf8mb4"

engine = create_engine(
  DATABASE_URL,
  echo=False,      # 디버깅용으로 보고 싶으면 True
  pool_size=5,
  max_overflow=10,
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)



def get_conn():
  """
  기존에는 connection_pool.PymysqlConnectionPool 에서 커넥션을 가져왔지만,
  이제는 SQLAlchemy Session을 반환함.
  """
  return SessionLocal()


def release_conn(conn):
  """
  기존에는 pool.release_connection(conn)을 호출했지만,
  이제는 SQLAlchemy Session을 닫기만 하면 됨.
  """
  conn.close()
