# 네이버 웹툰 스크래핑

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

browser = webdriver.Chrome("/Users/ihyeongseob/Desktop/chromedriver_mac_arm64/chromedriver")

# 1. 네이버 웹툰으로 이동
browser.get("https://comic.naver.com/index")

# 2. 탭에서 장르 선택하기 (class명 : tab_gr)
genre_ul = browser.find_element_by_class_name("tab_gr")
genre_list = genre_ul.find_elements_by_tag_name("a")

for genre in genre_list :
    # 3. 장르 클릭하기 & 로딩 기다리기
    genre.click()
    time.sleep(0.5)
    print("[", genre.text, "]")

    # 4. 장르별 웹툰정보 가져오기
    genre_recom_list = browser.find_elements_by_class_name("genreRecomInfo2")
    for genre_recom in genre_recom_list :
        # 5. title 정보 가져오기 (title + 컷툰 정보 있을 수도)
        title_class = genre_recom.find_element_by_class_name("title")
        # 6. 진짜 title 정보 가져오기 (컷툰 정보 제외)
        title = title_class.find_element_by_tag_name('a').text
        # 7. 작가 정보 가져오기
        user = genre_recom.find_element_by_class_name("user").text
        print("\t", title, " - ", user)


