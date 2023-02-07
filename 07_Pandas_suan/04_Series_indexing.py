# Series Indexing

import numpy as np
import pandas as pd

s = pd.Series(
    [0, 0.25, 0.5, 0.75, 1.0],
    index=['a', 'b', 'c', 'd', 'e']
)

print(s, end='\n\n')
print(s['b'], end='\n\n')
print('b' in s, end='\n\n')
print(s.keys())
# items()는 zip형태로 오기 때문에 list형으로 받아서 출력한다.
print(list(s.items()), end='\n\n')

# dictionary 자료형처럼 값 추가 가능
print("dictionary 자료형처럼 값 추가 가능", "-" * 10)
s['f'] = 1.25
print(s, end='\n\n')

print("slicing 가능", "-" * 10)
print(s['a':'c'], end='\n\n')
print(s[0:3], end='\n\n')

print("slicing에 조건 부여 가능", "-" * 10)
print(s[(s > 0.4) & (s < 0.8)])

s = pd.Series(
    ['a', 'b', 'c', 'd' , 'e'],
    index=[1, 3, 5, 7, 9]
)

print(s)
print(s[1])

print('loc() : 찾는 정수 정수값 ', '-'*20)
print(s.loc[0:2]) # --> 0 ~ 2 사이의 정수를 찾아서 출력
print('iloc() : 찾는 index값', '-'*20)
print(s.iloc[0:2]) # --> 0 ~ 1 사이의 index를 찾아서 출력

# reindex() : 기존에 있던 index를 조건에 맞게 reindexing
print('reindex() : 기존에 있던 index를 조건에 맞게 reindexing', '-'*20)
print(s.reindex(range(10))) # 10개의 index로 reindexing (중간에 없는 값들은 NaN으로 자동 할당)

# reindex(, method="bifill") : 기존에 있던 index를 조건에 맞게 reindexing
print('reindex(, method="bifill") : 기존에 있던 index를 조건에 맞게 reindexing', '-'*20)
print(s.reindex(range(10), method='bfill')) # 10개의 index로 reindexing (중간에 없는 값들은 바로 직전의 있는 값으로 할당)

