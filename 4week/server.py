import requests
from bs4 import BeautifulSoup
import re
url = 'https://www.genie.co.kr/chart/top200?ditc=D&rtm=N&ymd=20190715'

from pymongo import MongoClient
client = MongoClient('localhost',27017)
db = client.dbUser

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get(url,headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')
ranks = soup.select('#body-content > div.newest-list > div > table > tbody > tr')

for rank in ranks:
    if not rank.a == None:
        title = rank.select('a.title.ellipsis')[0].text
        artist = rank.select('a.artist.ellipsis')[0].text
        rank = rank.select('td.number')[0].text
        # print(rank[0:2].strip(), title.strip(), artist.strip())

    # DB에 저장
        doc = {}
        doc['rank'] = rank[0:2].strip()
        doc['title'] = title.strip()
        doc['artist'] = artist.strip()
        db.ranks.insert_one(doc)