# CGV 영화 리뷰 스크래핑

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time
import pandas as pd

def get_movie_review(url, page_num = 10) : 
    browser = webdriver.Chrome("/Users/ihyeongseob/Desktop/chromedriver_mac_arm64/chromedriver")
    # 1. CGV로 이동
    browser.get(url)

    writer_list = []
    review_list = []
    date_list = []
    # 2. 1~page_num 페이지까지 이동하며 scrap
    for page in range(1, page_num + 1) :
        try : 
            page_ul = browser.find_element_by_id("paging_point")
            page_a = page_ul.find_element_by_link_text(str(page))
            page_a.click()
            time.sleep(0.5)
            # 3. 페이지마다 글쓴이 정보, 리뷰 정보, 작성일 획득
            writers = browser.find_elements_by_class_name("writer-name")
            writer_list += [writer.text for writer in writers]
            reviews = browser.find_elements_by_class_name("box-comment")
            review_list += [review.text for review in reviews]
            dates = browser.find_elements_by_class_name("day")
            date_list += [date.text for date in dates]

            # 4. 10단위로 page가 나뉘어지기 때문에 다음 10개 page로 이동해야 한다.
            if page % 10 == 0 : 
                next_button = page_ul.find_element_by_class_name("btn-paging next")
                next_button.click()
                time.sleep(0.5)
        # 5. 다음 페이지가 없으면 종료
        except NoSuchElementException :
            break
    
    moview_review_df = pd.DataFrame({"Writer" : writer_list, "Review" : review_list, "Date" : date_list})
    return moview_review_df

url = "http://www.cgv.co.kr/movies/detail-view/?midx=86756"
moview_review_df = get_movie_review(url, )
moview_review_df