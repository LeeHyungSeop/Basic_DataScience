import requests

url = "https://www.naver.com/"
# User Agent 정보를 복붙한다.
headers = {"User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"}

res = requests.get(url, headers=headers) # User Agent 정보를 넘긴다

# 예외처리
res.raise_for_status() 

with open("naver.html", "w", encoding="utf-8") as f :
    f.write(res.text)