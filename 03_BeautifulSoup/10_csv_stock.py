import csv
import requests
from bs4 import BeautifulSoup

url = "https://finance.naver.com/sise/sise_market_sum.nhn?&page="

# csv 파일 생성, 열기
filename = "./03_BeautifulSoup/10_시가총액1-200.csv"
f = open(filename, "w", encoding="utf-8-sig", newline="")  # utf-8-sig : excel 파일에서 한글이 깨지는 것을 방지
writer = csv.writer(f)

# 파일 상위에 category를 나타내기 위해 네이버 증권 사이트에서 복사 붙여넣기 --> tab으로 구분되어 있는데 writerow()에 list를 전달해줘야하기 때문에
# "\t"을 기준으로 split()하여 list형태로 만들어 준다.
# ["N","종목명","현재가", ...]
title = "N	종목명	현재가	전일비	등락률	액면가	시가총액	상장주식수	외국인비율	거래량	PER	ROE".split("\t")
print(type(title))
writer.writerow(title)

# 네이버 코스피 시가총액 순위를 csv 파일로 저장하기
# 1~4 page에 대한 순위를 scrap할 것이다
for page in range(1, 5) :
    res = requests.get(url + str(page))
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    # table 밑의 tbody 밑의 tr들을
    data_rows = soup.find("table", attrs={"class" : "type_2"}).find("tbody").find_all("tr")
    for row in data_rows :
        colums = row.find_all("td")

        # \n\n\t\t , '' 같은 의미 없는 data는 Skip한다
        if len(colums) <= 1 :
            continue

        data = [column.get_text().strip() for column in colums]
        print(data)
        writer.writerow(data) # writerow([list형태])