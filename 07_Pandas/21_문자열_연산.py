import numpy as np
import pandas as pd

'''
<문자열 연사자> Python의 문자열 연산자를 거의 모두 반영
capitalize
casefold
count
find
rfind
index
rindex
isalnum
isalpha
isdecimal
isdigit
isnumeric
isidentifier
isspace
istitle
islower
isupper
join
center
ljust
rjust
lower
upper
title
swapcase
strip
lstrip
rstrip
partition
repartition
replace
split
rsplit
splitlines
startswith
endswith
zfill

<기타 연산자>
get
slice
slice_replace
cat
repeat
normalize
pad
wrap
join
get_dummies

<정규표현식>
match()
extract()
findall()
replace()
contains()
count()
split()
rsplit()
'''

print("name_tuple", "-"*20)
name_tuple = ['HyeongSeop Lee', 'Steven Jobs', "Larry Page", "Elon Musk", "Bill Gates", None, "Mark Zuckerberg", "Bill Gates", "Jeff Bezos"]
print(name_tuple)

print("names", "-"*20)
names = pd.Series(name_tuple)
print(names)

# str.lower()
print("str.lower()", "-"*20)
print(names.str.lower())

# str.len()
print("str.len()", "-"*20)
print(names.str.len())

# str.split()
print("str.split()", "-"*20)
print(names.str.split()) 

# str[slicing]
print("str[slicing]", "-"*20)
print(names.str[0:4]) 

# str.split().str.get(-1) : 이름의 성만 가져오기
print("str.split().str.get(-1)", "-"*20)
print(names.str.split().str.get(-1)) 

# str.repeat(2) : 반복하기
print("str.repeat(2)", "-"*20)
print(names.str.repeat(2)) 

# str.join() : 
print("str.join('*')", "-"*20)
print(names.str.join('*')) 

# 정규표현식, str.match('([A-Za-z]+)') 
print("str.match('([A-Za-z]+)') ", "-"*20)
print(names.str.match('([A-Za-z]+)')) 

# 정규표현식, str.findall('([A-Za-z]+)') 
print("str.findall('([A-Za-z]+)') ", "-"*20)
print(names.str.findall('([A-Za-z]+)')) 