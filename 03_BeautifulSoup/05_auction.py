import re
import requests
from bs4 import BeautifulSoup

url = "http://browse.auction.co.kr/search?keyword=%EB%85%B8%ED%8A%B8%EB%B6%81&itemno=&nickname=&frm=hometab&dom=auction&isSuggestion=No&retry=&Fwk=%EB%85%B8%ED%8A%B8%EB%B6%81&acode=SRP_SU_0100&arraycategory=&encKeyword=%EB%85%B8%ED%8A%B8%EB%B6%81"
headers = {"User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"}
res = requests.get(url, headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

# 옥션 스크래핑 
    # 정규식 표현을 사용하여 search_product로 시작하는 class명을 가진 li tag를 모두 가져온다
    # 광고가 붙은 상품들의 class명은 search-product search-product__ad-badge 이기 때문에 광고가 붙던 말던 모두 정보를 가져올 것이다.
items = soup.find_all("div", attrs={"class" : re.compile("^component component--item_card type--")}) 

for item in items :
    name = item.find("span", attrs={"class":"text--title"}).get_text()
    price = item.find("strong", attrs={"class":"text--price_seller"}).get_text()
    review_cnt = item.find("span", attrs= {"class" : "text--reviewcnt"})
    if review_cnt :
        review_cnt = review_cnt.get_text()
    else :
        print(" <리뷰 없는 제품은 제외> ")
        continue
    
    rate_cnt = item.find("div", attrs={"class":"seller_awards"})
    if rate_cnt :
        rate_cnt = rate_cnt.get("title")
    else :
        print(" <평점 없는 제품은 제외> ")
        continue

    print(name + " / " + price + " / " + review_cnt + " / " + rate_cnt )
