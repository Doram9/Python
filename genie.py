import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient #pymongo를 쓰겠습니다.
client = MongoClient('localhost', 27017) #내 컴퓨터에서 돌아가고있는 MongoDB에 접속할것입니다.
db = client.dbsparta #dbsparta라는 이름의 데이터베이스에 접속할겁니다. 없으면 해당 db를 만듭니다.

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&ymd=20200403&hh=23&rtm=N&pg=1',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

music_list = soup.select('#body-content > div.newest-list > div > table > tbody > tr')
for music in music_list:
    rank = music.select_one('td.number').text[0:2].strip()
    title = music.select_one('td.info > a.title.ellipsis').text.strip()
    artist = music.select_one('td.info > a.artist.ellipsis').text
    print(rank, title, artist)