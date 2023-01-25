import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

# print(soup.find("a", attrs={"class":"Nbtn_upload"})) # class명이 "Nbtn_upload"인 a tag에 해당하는 첫번째 element만 가져온다.
# print(soup.find(attrs={"class":"Nbtn_upload"})) # class명이 "Nbtn_upload"인 a tag에 해당하는 첫번째 element만 가져온다.

# rank1 = (soup.find("li", attrs={"class" : "rank01"}))
# print(rank1.a.get_text()) # rank1의 자식 중 a tag의 내용을 출력

# rank2 = rank1.next_sibling.next_sibling # next_sibling : 같은 형제 관계인 다음 Element를 반환
# print(rank2.a.get_text()) # rank2의 자식 중 a tag의 내용을 출력

# rank1 = rank2.previous_sibling.previous_sibling # previous_sibling : 같은 형제 관계인 이전 Element를 반환
# print(rank1.a.get_text()) # rank1의 자식 중 a tag의 내용을 출력

# print(rank1.parent) # rank1의 부모 출력

# rank1 = (soup.find("li", attrs={"class" : "rank01"}))
# print(rank1.a.get_text()) # rank1의 자식 중 a tag의 내용을 출력
# rank2 = rank1.find_next_sibling("li") # find_next_sibling() :  개행이 있는지 없는지 알 필요 없이 li tag인 다음 형제 Element 정보를 얻을 수 있다
# print(rank2.a.get_text())
# rank3 = rank2.find_next_sibling("li") # find_next_sibling() :  개행이 있는지 없는지 알 필요 없이 li tag인 다음 형제 Element 정보를 얻을 수 있다
# print(rank3.a.get_text())
# rank2 = rank3.find_previous_sibling("li") # find_previous_sibling() :  개행이 있는지 없는지 알 필요 없이 li tag인 이전 형제 Element 정보를 얻을 수 있다
# print(rank2.a.get_text())
# rank1 = rank2.find_previous_sibling("li") # find_previous_sibling() :  개행이 있는지 없는지 알 필요 없이 li tag인 이전 형제 Element 정보를 얻을 수 있다
# print(rank1.a.get_text())


rank1 = (soup.find("li", attrs={"class" : "rank01"}))
siblings = rank1.find_next_siblings("li")
for sibling in siblings :
    print(sibling.a.get_text()) 
