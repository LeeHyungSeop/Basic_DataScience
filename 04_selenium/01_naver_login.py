from selenium import webdriver
import time

browser = webdriver.Chrome("/Users/ihyeongseob/Desktop/chromedriver_mac_arm64/chromedriver")

# 1. 네이버로 이동
browser.get("http://naver.com")

# 2. 로그인 버튼 클릭
elem = browser.find_element_by_class_name("link_login")
elem.click()

# 3. 잘못된 ID, PW 입력
browser.find_element_by_id("id").send_keys("your naver id") 
browser.find_element_by_id("pw").send_keys("your naver pw") 

# 4. 진짜 로그인 버튼 클릭
browser.find_element_by_id("log.login").click()

# 5. ID, PW를 재입력
browser.find_element_by_id("id").clear() # 입력란 지우기
browser.find_element_by_id("id").send_keys("retry_id") 
browser.find_element_by_id("pw").send_keys("retry_pw") 

# 6. html 정보 출력
print(browser.page_source) # browser에 있는 모든 html 문서를 그대로 출력해준다.
time.sleep(2)

# 7. 브라우저 전체 종료
browser.quit()