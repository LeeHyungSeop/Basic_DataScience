import requests

res = requests.get("https://www.naver.com/") # status_code가 200이면 정상
res = requests.get("https://www.naverabc.com/") # status_code가 200이면 정상

# # 예외처리 방법 1
# if res.status_code == requests.codes.ok :
#     print("정상입니다")
# else :
#     print("문제가 생겼습니다. [에러코드 ", res.status_code, "]")

# # 예외처리 방법 2
# res.raise_for_status() # 문제가 생기면 바로 프로그램 종료된다
# print("웹 스크래핑을 진행합니다")