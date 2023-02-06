import numpy as np
import pandas as pd

idx = pd.DatetimeIndex(['2019-01-01', '2020-01-01', '2020-02-01', '2020-02-02', '2020-03-01'])
s = pd.Series([0, 1, 2, 3, 4], index=idx)
print("s","-"*20)
print(s, end='\n\n')

print("2020-02-01 이후 데이터 조회","-"*20)
print(s['2020-02-01' : ], end='\n\n')

print("2020-02-01 이전 데이터 조회","-"*20)
print(s[ : '2020-02-01'], end='\n\n')

print("2019년 데이터만 조회","-"*20)
print(s['2019'], end='\n\n')
