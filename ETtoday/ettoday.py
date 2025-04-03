import requests
from bs4 import BeautifulSoup

from ettoday_db import drop_and_create, insert_data, show_news_data

# 抓到HTML
url = 'https://travel.ettoday.net/category/%E5%8F%B0%E5%8C%97/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

art = soup.find_all('div', class_ = "box_0 clearfix")

# 儲存到資料庫
news_data = []
drop_and_create()

# 處理資料
for obj in art:
    title = obj.find('h3', itemprop= "headline")
    if title and title.a:
        title = title.a.text
        print(title)
        
    else:
        continue

    summary = obj.find('p', class_='summary')
    summ = summary.text
    print(summ)
    
    new_item ={
    'title':title,
    'content':summ
    }
    news_data.append(new_item)

# 插入資料
insert_data(news_data)
show_news_data()
