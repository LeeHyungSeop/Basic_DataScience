import numpy as np
import pandas as pd
from datetime import datetime

print("dates", "-"*20)
dates = [
    datetime(2020, 1, 1), datetime(2020, 1, 2), datetime(2020, 1, 4), datetime(2020, 1, 7),
    datetime(2020, 1, 10), datetime(2020, 1, 11), datetime(2020, 1, 15)
]
print(dates, end='\n\n')

print("ts", "-"*20)
ts = pd.Series(np.random.randn(7), index=dates)
print(ts, end='\n\n')
print(ts.index[0], end='\n\n')
print(ts[ts.index[2]], end='\n\n')
print(ts['1/4/2020'], end='\n\n')

print("new ts","-"*20)
ts = pd.Series(
    np.random.random_integers(1000),
    index=pd.date_range('2017-10-01', periods=1000)
)
print(ts, end='\n\n')
print(ts['2020'], end='\n\n')
print(ts['2020-06'], end='\n\n')
print(ts[datetime(2020, 6, 20) : ], end='\n\n')
print(ts['2020-06-15' : '2020-06-18'], end='\n\n')

print("tdf", "-"*20)
tdf = pd.DataFrame(
    np.random.randn(1000,4),
    index=pd.date_range('2017-10-01', periods=1000),
    columns=['A', 'B', 'C', 'D']
)
print(tdf, end='\n\n')

print(tdf.loc['2020-06'], end='\n\n')
print(tdf.loc['2020-06-20' : ], end='\n\n')
print(tdf['C'], end='\n\n')

ts = pd.Series(
    np.random.randn(10),
    index=pd.DatetimeIndex([
        '2020-01-01', '2020-01-01', '2020-01-02', '2020-01-02', '2020-01-03',
        '2020-01-04', '2020-01-05', '2020-01-05', '2020-01-06', '2020-01-07',
    ])
)
print("ts","-"*20)
print(ts, end='\n\n')
print(ts.index.is_unique, end='\n\n') # 날짜가 unique하지 않다.
print(ts['2020-01-01'], end='\n\n')

# 중복되는 날짜에 대해서 groupby로 합친 후 집계값 출력
print("중복되는 날짜에 대해서 groupby로 합친 후 집계값 출력", "-"*10)
print(ts.groupby(level=0).mean(), end='\n\n') 

print(pd.date_range('2020-01-01','2020-07-01'), end='\n\n')
print(pd.date_range(start='2020-01-01', periods=10), end='\n\n')
print(pd.date_range(end='2020-07-01', periods=10), end='\n\n')

# date_range(freq='B') : 공휴일은 생략. Business(영업일)만 출력
print("date_range(freq='B') : 공휴일은 생략. Business(영업일)만 출력", "-"*20)
print(pd.date_range('2020-07-01', '2020-07-07', freq='B'), end='\n\n')