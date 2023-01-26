import re
import requests
from bs4 import BeautifulSoup

url = "http://browse.auction.co.kr/search?keyword=%EB%85%B8%ED%8A%B8%EB%B6%81&itemno=&nickname=&frm=hometab&dom=auction&isSuggestion=No&retry=&Fwk=%EB%85%B8%ED%8A%B8%EB%B6%81&acode=SRP_SU_0100&arraycategory=&encKeyword=%EB%85%B8%ED%8A%B8%EB%B6%81"
headers = {"User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"}
res = requests.get(url, headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

# 옥션 스크래핑 
    # 무료배송과 사은품증정하는 상품만 수집할 것이다. 
    # span class = box__tag , get_text() : "무료배송"
    # span class = box__tag , get_text() : "사은품"
items = soup.find_all("div", attrs={"class" : re.compile("^component component--item_card type--")}) 

for item in items :
    # 무료배송과 사은품증정하는 제품만 수집
    free_delivery = item.find_all("span", attrs={"class" : "box__tag"})

    if len(free_delivery) != 2:
        print(" <무료배송, 사은품 증정하지 않은 제품> ")
        continue
    else :
        name = item.find("span", attrs={"class":"text--title"}).get_text()
        price = item.find("strong", attrs={"class":"text--price_seller"}).get_text()
        rate_cnt = item.find("div", attrs={"class":"seller_awards"})
        if rate_cnt :
            rate_cnt = rate_cnt.get("title")
        else :
            rate_cnt = "후기평점 없음"
        print(name + " / " + price + " / " + rate_cnt)
