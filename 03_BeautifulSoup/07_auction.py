import re
import string
import requests
from bs4 import BeautifulSoup

url = "http://browse.auction.co.kr/search?keyword=%eb%85%b8%ed%8a%b8%eb%b6%81&itemno=&nickname=&frm=hometab&dom=auction&isSuggestion=No&retry=&Fwk=%eb%85%b8%ed%8a%b8%eb%b6%81&acode=SRP_SU_0100&arraycategory=&encKeyword=%eb%85%b8%ed%8a%b8%eb%b6%81&k=32&p=1"
headers = {"User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"}
res = requests.get(url, headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")
items = soup.find_all("div", attrs={"class" : re.compile("^component component--item_card type--")}) 

# 옥션 스크래핑 
    # 리뷰 100개 이상, 평점 4.0 이상인 제품 중 삼성 제품은 제외

for item in items :
    name = item.find("span", attrs={"class":"text--title"}).get_text()
    price = item.find("strong", attrs={"class":"text--price_seller"}).get_text()
    brand = item.find("span", attrs={"class" : "text--brand"})
    review_cnt = item.find("span", attrs= {"class" : "text--reviewcnt"})
    rate = item.find("div", attrs={"class":"seller_awards"})

    # 브랜드명이 없는 상품은 continue, 있다면 삼성 제품은 제외
    if brand : 
        if "삼성" in brand.get_text() :
            print(" <삼성 제품은 제외> ")
            continue
    else : 
        print(" <브랜드명이 없는 제품은 제외> ")
        continue
    # 제목에 "삼성" 있으면 제외
    if "삼성" in name :
        print(" <삼성 제품은 제외> ")
        continue

    # 후기 정보가 없는 상품은 continue, 있다면 정수값만 Parsing
    if review_cnt :
        review_cnt = review_cnt.get_text()
        review_cnt = review_cnt.replace(',' , '') # 후기 123,000 -> 후기 123000
        review_cnt = review_cnt[3 : ] # 후기 100 -> 100
    else :
        print(" <리뷰 없는 제품은 제외> ")
        continue
    # 평점 정보가 없는 상품은 continue, 있다면 실수값으로 Parsing
    if rate :
        rate = rate.get("title")
        rate = rate[5:-1] # 후기평점 4.7 -> 4.7 
    else :
        print(" <평점 없는 제품은 제외> ")
        continue
    
    # 조건에 맞는지 확인하여, 맞다면 출력
    if int(review_cnt) >= 100 and float(rate) >= 4.0 :
        print(name + " / " + price + " / " + review_cnt + " / " +rate)