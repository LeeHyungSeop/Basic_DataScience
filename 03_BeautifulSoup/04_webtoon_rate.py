import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/list?titleId=570503&weekday=thu"
res = requests.get(url)
res.raise_for_status()

# 연애혁명이라는 웹툰 페이지에서 평점 정보 가져와서 평균 평점 계산하기
soup = BeautifulSoup(res.text, "lxml")
cartoons = soup.find_all("div", attrs={"class" : "rating_type"})
total_rates = 0
for cartoon in cartoons :
    rate = cartoon.find("strong").get_text()
    print(rate)
    total_rates += float(rate)

print("전체 점수 : ", total_rates)
print("평균 점수 : ", total_rates / len(cartoons))