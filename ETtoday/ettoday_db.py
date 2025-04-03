import pymysql
import os
from dotenv import load_dotenv

load_dotenv()

HOST = os.getenv("HOST")
USER = os.getenv("USER")
PASSWORD = os.getenv("PASSWORD")
DB = os.getenv("DB")

def conn_db():
    return pymysql.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        db=DB
    )

def drop_and_create():
    conn = pymysql.connect(
        host=HOST,
        user=USER,
        password=PASSWORD
    )
    cur = conn.cursor()

    cur.execute("drop database if exists HK_ettoday")
    cur.execute("create database HK_ettoday")
    conn.commit()
    conn.close()

def insert_data(new_data):
    conn = conn_db()
    cur = conn.cursor()
    cur.execute("""
        create table if not exists news (
            title varchar(225),
            content TEXT
        )
    """)

    for new in new_data:
        sql = """
            insert into news (title, content)
            values (%s, %s)
        """
        cur.execute(sql,(
            new['title'],
            new['content']
        ))
    
    conn.commit()
    conn.close()

def show_news_data():
    try:
        conn = pymysql.connect(
            host=HOST,
            user=USER,
            password=PASSWORD,
            db=DB
        )
        cur = conn.cursor()

        cur.execute("select * from news limit 5")
        results = cur.fetchall()

        for row in results:
            print(f"標題：{row[0]}")
            print(f"內容：{row[1]}")
    except Exception as e:
        print(f"Error:{e}")
    finally:
        if conn:
            conn.close()
