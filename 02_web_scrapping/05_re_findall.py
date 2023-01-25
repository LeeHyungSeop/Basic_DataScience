# regular expression 정규식

# 1) p = re.compile("원하는 형태")
# 2) m = p.match("비교할 문자열") : 주어진 문자열의 처음부터 일치하는지 확인
# 3) m = p.search("비교할 문자열") : 주어진 문자열 중에 일치하는게 있는지 확인
# 4) m = p.findall("비교할 문자열") : 일치하는 모든 것을 "리스트" 형태로 반환

# "원하는 형태"
# . (ca.e) : 하나의 문자를 의미 -> care, cafe, case | caffe (X)
# ^ (^de)  : 문자열의 시작 -> desk, destination (O) | fade (X)
# $ (se$)  : 문자열의 끝  -> case, base (O) | face (X)

import re

p = re.compile("ca.e")

def print_findall(m) : 
    if m : 
        print("m.group() : ", m.group()) # 일치하는 문자열만 반환
        print("m.string", m.string) # 입력받은 문자열
        print("m.start", m.start()) # 일치하는 문자열의 시작 index 반환
        print("m.end", m.end()) # 일치하는 문자열의 끝 index 반환
        print("m.span", m.span()) # 일치하는 문자열의 시작/끝 index 반환
        print("-----------------")
        
    else :
        print("매칭되지 않았습니다")

m = p.findall("good care cafe") # findall : 일치하는 모든 것을 리스트 형태로 반환
print(m)

