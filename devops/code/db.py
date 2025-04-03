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

    cur.execute("drop database if exists devops")
    cur.execute("create database devops")
    conn.commit()
    conn.close()

def insert_data(report):
    conn = conn_db()
    cur = conn.cursor()
    cur.execute("""
        create table if not exists report (
            item VARCHAR(10),
            response TEXT,
			screenshot LONGBLOB
        )
    """)

    for obj in report:
        # 讀取截圖文件並轉換為二進制格式
        screenshot_data = None
        if obj['screenshot']:  # 假設 'screenshot' 是檔案路徑
            with open(obj['screenshot'], "rb") as f:
                screenshot_data = f.read()  # 讀取檔案的二進制資料
        sql = """
            insert into report (item, response, screenshot)
            values (%s, %s, %s)
        """
        cur.execute(sql,(
            obj['item'],
            obj['response'],
			screenshot_data
        ))
    
    conn.commit()
    conn.close()
