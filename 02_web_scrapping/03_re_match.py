# regular expression 정규식

# 1) p = re.compile("원하는 형태")
# 2) m = p.match("비교할 문자열") : 주어진 문자열의 처음부터 일치하는지 확인
# 3) m = p.search("비교할 문자열") : 주어진 문자열 중에 일치하는게 있는지 확인
# 4) m = p.findall("비교할 문자열") : 일치하는 모든 것을 "리스트" 형태로 반환

# 원하는 형태 
# . (ca.e) : 하나의 문자를 의미 -> care, cafe, case | caffe (X)
# ^ (^de)  : 문자열의 시작 -> desk, destination (O) | fade (X)
# $ (se$)  : 문자열의 끝  -> case, base (O) | face (X)

import re

p = re.compile("ca.e")

def print_match(m) : 
    if m : 
        print(m.group())
    else :
        print("매칭되지 않았습니다")

m = p.match("case") 
print_match(m)

m = p.match("case asdfasdfadsfaf") # match : 주어진 문자열의 처음부터 일치하는지 확인. "ca.e" 까지는 모두 일치하니까 일치한다고 판단
print_match(m)

m = p.match("good care") # match : 주어진 문자열의 처음부터 일치하는지 확인. "ca.e"와 "good" 은 일치하지 않으니까 일치하지 않는다고 판단
print_match(m)




