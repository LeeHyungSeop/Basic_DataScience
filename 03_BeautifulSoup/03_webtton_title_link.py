import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/list?titleId=570503&weekday=thu"
res = requests.get(url)
res.raise_for_status()

# 연애혁명이라는 웹툰 페이지에서 제목 페이지와 해당 링크 가져오기
soup = BeautifulSoup(res.text, "lxml")
cartoons = soup.find_all("td", attrs= {"class":"title"})

for cartoon in cartoons :
    title = cartoon.a.get_text()
    link = "https://comic.naver.com" + cartoon.a["href"]
    print(title, link)
