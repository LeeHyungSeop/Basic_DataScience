# 네이버 검색 API 예제 - 지식in 검색
import os
import sys
import urllib.request
import pandas as pd
import json
import re # regular expression (데이터를 받을 때 <b> tag도 같이 넘어오는 것을 지우기 위해서)

client_id = ""
client_secret = ""

query =  urllib.parse.quote(input("검색할 단어 : ")) # quote -> utf8로 인코딩해준다
idx = 0
display = 100 # 100개 단위로 가져올 것이다
start = 1 
end = 1000 # 1000개를 가져올 것이다
sort = "sim" # 기본값인 sim으로 두겠다. (유사도순으로 정렬)

# 받아온 데이터를 저장하기 위해 pandas의 DataFrame을 사용할 것이다.
kin_df = pd.DataFrame(columns=("Title", "Link", "Description"))

# 1~1000까지 100개씩 나누어 데이터를 가져온다
for start_index in range(start, end, display) :
  url = "https://openapi.naver.com/v1/search/kin?query=" + query \
        + "&display=" + str(display) \
        + "&start=" + str(start_index) \
        + "&sort=" + sort  # 원래 data type이 string이니까 casting할 필요 없음

  request = urllib.request.Request(url)
  request.add_header("X-Naver-Client-Id",client_id)
  request.add_header("X-Naver-Client-Secret",client_secret)
  response = urllib.request.urlopen(request)
  rescode = response.getcode()
  # 응답이 성공했다면 (json형식의 items 데이터를 parsing하여 DataFrame에 저장한다)
  if(rescode==200):
      response_body = response.read()
      response_dict = json.loads(response_body.decode('utf-8')) 
      items = response_dict['items'] # 'items' key에 해당하는 value들을 가져온다
      for item_index in range(0, len(items)) :
        remove_tag = re.compile('<.*?>') # data에서 tag를 모두 지우고 가져올 것이다
        title = re.sub(remove_tag, '', items[item_index]['title'])
        link = items[item_index]['link']
        description = re.sub(remove_tag, '', items[item_index]['description'])
        kin_df.loc[idx] = [title, link, description]
        idx += 1


  else:
      print("Error Code:" + rescode)

kin_df
