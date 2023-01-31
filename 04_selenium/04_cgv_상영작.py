# CGV 무비차트와 해당 무비의 리뷰 Scrapping

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time
import pandas as pd

# 0 : cgv 무비차트 페이지로 이동하기
browser = webdriver.Chrome("/Users/ihyeongseob/Desktop/chromedriver_mac_arm64/chromedriver")
url = "http://www.cgv.co.kr/movies/?lt=1&ft=0" 
browser.get(url)

def get_movie_review(url, page_num = 10) : 
    browser = webdriver.Chrome("/Users/ihyeongseob/Desktop/chromedriver_mac_arm64/chromedriver")
    # 4_1) 해당 영화 페이지로 이동
    browser.get(url)

    writer_list = []
    review_list = []
    date_list = []
    # 4_2) 1~page_num 페이지까지 이동하며 scrap
    for page in range(1, page_num + 1) :
        try : 
            page_ul = browser.find_element_by_id("paging_point")
            page_a = page_ul.find_element_by_link_text(str(page))
            page_a.click()
            time.sleep(0.5)
            # 4_3) 페이지마다 글쓴이 정보, 리뷰 정보, 작성일 획득
            writers = browser.find_elements_by_class_name("writer-name")
            writer_list += [writer.text for writer in writers]
            reviews = browser.find_elements_by_class_name("box-comment")
            review_list += [review.text for review in reviews]
            dates = browser.find_elements_by_class_name("day")
            date_list += [date.text for date in dates]

            # 4_4) 10단위로 page가 나뉘어지기 때문에 다음 10개 page로 이동해야 한다.
            if page % 10 == 0 : 
                next_button = page_ul.find_element_by_class_name("btn-paging next")
                next_button.click()
                time.sleep(0.5)
        # 4_5) 다음 페이지가 없으면 종료
        except NoSuchElementException :
            break
    
    moview_review_df = pd.DataFrame({"Writer" : writer_list, "Review" : review_list, "Date" : date_list})
    return moview_review_df

# 1. 무비차트 Element 정보 가져오기
movie_chart = browser.find_element_by_class_name("sect-movie-chart")
# 2. 무비차트에 있는 내용 정보 가져오기
contents = movie_chart.find_elements_by_class_name("box-contents")
for content in contents :
    print("-"*100)
    # 3. 영화마다 링크 정보, 제목, 예매율, 개봉일
    link = content.find_element_by_tag_name('a').get_attribute('href')
    title = content.find_element_by_class_name('title').text
    percent = content.find_element_by_class_name("percent").text
    date = content.find_element_by_class_name("txt-info").text
    print(title, percent, date, link)

    # 4. 각 영화마다 리뷰 정보 (1페이지만) 가져오기
    print(get_movie_review(link, 1))