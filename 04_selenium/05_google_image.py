# 구글에서 Image Scrapping

from selenium import webdriver
import time
import os
import socket

from urllib.request import urlretrieve
from urllib.error import HTTPError, URLError 
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException, ElementNotInteractableException
from PIL import Image

# 6
# 모든 이미지에 대해서 scrap을 완료하였는데, 외부 URL을 통해서 이미지를 다운로드하는 경우,
# 해당 웹사이트에서 이미지 해상도에 대한 제한을 걸어서 저해상도의 이미지를 획득한 경우가 존재할 것이다.
# 저해상도 이미지를 삭제하여 필터링하는 작업을 진행.
def filter_and_remove(dir_name, query, filter_size) :
    filtered_count = 0

    # dir_name 디렉터리에 있는 file들에 대해서 각각 접근
    for index, file_name in enumerate(os.listdir(dir_name)) :
        try : 
            # 파일 경로 : 디렉터리명/파일명 
            file_path = os.path.join(dir_name, file_name)
            # 이미지 open
            img = Image.open(file_path)

            # 마지노선 해상도 보다 낮은 경우, img 삭제
            if img.width < filter_size and img.height > filter_size :
                img.close()
                os.remove(file_path)
                print(f"{index} 이미지 제거")
                filtered_count += 1
        except OSError as e: 
            # 파일이 열리지 않는다면, 손상된 이미지이다 --> 이 파일도 제거
            print(e)
            os.remove(file_path)
            print(f"{index} 이미지 제거")
            filtered_count += 1
    
    print(f"[이미지 제거 개수 : {filtered_count}/{scrapped_count}]")
            
# 4
def click_and_save(dir_name, index, img, img_list_len) :
    global scrapped_count

    try : 
        img.click()
        # img를 click하였을 때, load되는 시간을 기다려준다
        browser.implicitly_wait(3)

        # img의 src 속성 값을 가져와서 img link를 획득 --> 진짜 이미지 원본 획득
        src = browser.find_element_by_xpath("//*[@id='Sva75c']/div[2]/div/div[2]/div[2]/div[2]/c-wiz/div[2]/div[1]/div[1]/div[2]/div/a/img").get_attribute("src")

        # 해당 이미지의 확장자 대로 이미지 저장
        if src.split('.')[-1] == "png" :
            urlretrieve(src, dir_name + '/' + str(scrapped_count + 1) + ".png")
            print(f" {index+1}/{img_list_len} PNG 이미지 저장")
        else :
            urlretrieve(src, dir_name + '/' + str(scrapped_count + 1) + ".jpg")
            print(f" {index+1}/{img_list_len} JPG 이미지 저장")
        scrapped_count += 1

    except HTTPError as e:
        # img link에 이상이 있는 경우 에외 처리
        print(e)
        pass # 건너 뜀
    except ElementClickInterceptedException as e: 
        # Click에 대한 error가 생길 때, 예외 처리
        print(e)
        pass


# 2
def scroll_down() :
    scroll_count = 0
    print("[scroll_down() : 스크롤 다운 시작]")
    # javascript를 call해서 scroll down하는 method
    last_height = browser.execute_script("return document.body.scrollHeight")
    after_click = False

    while True :
        print(f"[스크롤 다운 : {scroll_count}]")
        # 실제로 스크롤 다운 실행 ()
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);") 
        scroll_count += 1
        # 스크롤할 때 무언가 로드되는 시간을 기다리기 위해 
        time.sleep(1)

        # 스크롤 다운한 후, 새로운 scroll height값을 저장
        new_height = browser.execute_script("return document.body.scrollHeight")

        # 만약 스크롤 다운이 되지 않았다면, 페이지의 끝에 도달한 것임
        if last_height == new_height :
            # 결과 더보기 버튼을 클릭해서 스크롤 다운을 더 진행할 수 있는 경우
            if after_click is False :
                # 결과 더보기 버튼이 없는 검색어가 있을 수 있으니 예외 처리
                try :
                    more_button = browser.find_element_by_xpath('//*[@id="islmp"]/div/div/div/div[2]/div[1]/div[2]/div[2]/input')
                    if more_button.is_displayed() :
                        more_button.click()
                        after_click = True
                except NoSuchElementException as e:
                    print(e)
                    break

            # 결과 더보기 버튼도 눌러서 진짜 페이지의 끝에 도달했으면 더이상 내릴 수 없다
            else :
                break
        
        last_height = new_height


# scraping 함수 scraping(image를 저장할 디렉터리, 검색할 image) 
def scraping(dir_name, query) :
    global scrapped_count
    url = f"https://www.google.com/search?q={query}&tbm=isch&ved=2ahUKEwiT3umxnfH8AhWaBaYKHb3VBX4Q2-cCegQIABAA&oq={query}&gs_lcp=CgNpbWcQAzIECCMQJzIICAAQgAQQsQMyCAgAEIAEELEDMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDoGCAAQBxAeOggIABCxAxCDAVCSBlidCGD5CWgBcAB4AIABc4gBvwKSAQMwLjOYAQCgAQGqAQtnd3Mtd2l6LWltZ8ABAQ&sclient=img&ei=tbvYY9OvL5qLmAW9q5fwBw&bih=976&biw=1920&rlz=1C5CHFA_enKR1019KR1019"
    # 화면에 출력되는 이미지를 많게 하여 Scrap 속도를 높히기 위해 창화면 최대크기로 설정
    browser.get(url)
    browser.maximize_window()

    # 2. 페이지 가장 밑으로 scoll함으로써 모든 image를 Load 시키는 함수
    scroll_down() 

    # 3. loading된 이미지들을에 접근하기 위한 상위 Element 찾기 & 모든 image_list 가져오기
    div = browser.find_element_by_xpath('//*[@id="islrg"]/div[1]')
    img_list = div.find_elements_by_css_selector('div.bRMDJf.islir > img')
    img_list_len = len(img_list)
    for index, img in enumerate(img_list) : 
        try : 
            # 4. 썸네일 이미지 선택 후 원본 이미지 저장
            click_and_save(dir_name, index, img, img_list_len)
        except ElementClickInterceptedException as e: 
            # Click에 대한 error가 생길 때, 예외 처리
            print(e)
            browser.execute_script("window.scrollTo(0, window.scrollY + 100)") # 다시 윈도우 스크롤 진행
            time.sleep(1)
            click_and_save(dir_name, index, img, img_list_len) # 재시도
        except NoSuchElementException as e:
            # Element를 찾을 수 없을 때, 예외 처리
            print(e)
            browser.execute_script("window.scrollTo(0, window.scrollY + 100)") # 다시 윈도우 스크롤 진행
            time.sleep(1)
            click_and_save(dir_name, index, img, img_list_len) # 재시도
        except ConnectionResetError as e :
            # connection error --> 예외 처리(무시)
            print(e)
            pass
        except URLError as e :
            # URL error --> 예외 처리(무시)
            print(e)
            pass
        except socket.gaierror as e :
            # get address info(gai) : img에 대한 address를 얻는 데에 문제가 생길 경우 --> 무시
            print(e)
            pass
        except ElementNotInteractableException as e :
            # Element에 더이상 interactable하지 못한 때, 멈춘다
            print(e)
            break

    # scraping 성공률 출력 ((스크랩 개수 / 전체 이미지 개수) * 100)
    try : 
        print("[스크래핑 종료 (성공률 : %.2f%%)]" % (scrapped_count / img_list_len * 100.0))
    except ZeroDivisionError as e :
        # img_list_len가 0인 경우, 예외 처리
        print(e)
    
    # Web Driver 종료
    browser.quit()
            

# timeout 최대를 지정
socket.setdefaulttimeout(30)
# webdriver 지정
browser = webdriver.Chrome("/Users/ihyeongseob/Desktop/chromedriver_mac_arm64/chromedriver")
# 전체 이미지 개수 측정
scrapped_count = 0
path = "./"
query = input("검색어 입력 : ")

# ./(query) 라는 디렉터리명 생성
dir_name = path + query
os.makedirs(dir_name)
print(f"[{dir_name} 디렉터리 생성]")

# 1. scraping 진행
scraping(dir_name, query)

# 6. 저해상도, 손상된 이미지 제거 
# filter_size : 원하는 저해상도의 마지노선값
filter_and_remove(dir_name, query, 1000)