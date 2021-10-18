import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient #pymongo를 쓰겠습니다.
client = MongoClient('localhost', 27017) #내 컴퓨터에서 돌아가고있는 MongoDB에 접속할것입니다.
db = client.dbsparta #dbsparta라는 이름의 데이터베이스에 접속할겁니다. 없으면 해당 db를 만듭니다.

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20200303',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

# 코딩 시작
trs = soup.select('#old_content > table > tbody > tr')
for tr in trs:
    a_teg = tr.select_one('td.title > div > a')
    if a_teg is not None:
        rank = tr.select_one('td:nth-child(1) > img')['alt']
        title = a_teg.text
        star = tr.select_one('td.point').text
        doc = {
            'rank':rank,
            'title':title,
            'star':star
        }
        db.movies.insert_one(doc)
# 저장 - 예시

