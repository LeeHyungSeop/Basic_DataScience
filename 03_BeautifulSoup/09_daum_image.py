import requests
from bs4 import BeautifulSoup

# 최근 5개 년도별 상위 5개 영화 포스터 스크랩 (2018 ~ 2022)
for year in range(2018, 2023) :
    url = "https://search.daum.net/search?w=tot&q={}%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR".format(year)
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")
    images = soup.find_all("img", attrs={"class" : "thumb_img"})

    for idx, image in enumerate(images):
        image_url = image["src"]
        if image_url.startswith("//") : # "//" 로 시작하는 것들은 https: 를 붙여준다
            image_url = "https:" + image_url

        print(image_url)

        # 링크 페이지에 접속하여 페이지에 있는 정보를 파일로 저장하기 위해서 새롭게 접속한다
        image_res = requests.get(image_url)
        image_res.raise_for_status()
        
        with open("./03_BeautifulSoup/09_images/movie_{}_{}.jpg".format(year, idx + 1), "wb") as f : # movie_2018_1, movie_2018_2, ... , write binary
            f.write(image_res.content)
        
        if idx >= 4 : # 상위 5개 이미지까지만 다운로드
            break
