import numpy as np
import pandas as pd
from datetime import datetime
import pytz 

'''
Resampling : 시계열의 빈도(freq) 변환
Down Sampling : 상위 빈도 데이터를 하위 빈도 데이터로 집계
Up Sampling : 하위 빈도 데이터를 상위 빈도 데이터로 집계

freq : 빈도
axis : 축
fill_method : upsampling시 보간 수행(None, ffill, bfill)
closed : down sampling시 각 간격의 포함 위치(right, left)
label : down smapling시 집계된 결과 라벨 결정(right, left)
loffset : 나뉜 그룹의 라벨을 맞추기 위한 오프셋
limit : 보간법을 사용할 때 보간을 적용할 최대 기간
kind : period 또는 timestamp 집계 구분
convention : 기간을 resampling할 때, 하위 빈도 기간에서 상위 빈도로 변환 시 방식(start, end)
'''

dr = pd.date_range('2020-01-01', periods=200, freq='D')
ts = pd.Series(
    np.random.randn(len(dr)),
    index=dr
)
print("ts" , "-"*20)
print(ts, end='\n\n')

print("ts.resample('M').mean()", "-"*10)
print(ts.resample('M').mean(), end='\n\n')

print("ts.resample('M', kind='period').mean()", "-"*10)
print(ts.resample('M', kind='period').mean(), end='\n\n')

print("new ts", "-"*20)
dr = pd.date_range('2020-01-01', periods=10, freq='T')
ts = pd.Series(np.arange(10), index=dr)
print(ts, end='\n\n')

# closed='left' or 'right'
print("closed='left' or 'right'", "-"*20)
print(ts.resample('2T', closed='left').sum(), end='\n\n') # 00:00:00 <= x < 00:00:02
print(ts.resample('2T', closed='right').sum(), end='\n\n') # 23:58:00 < x <= 00:00:00

# label
print("closed='right', label='right''", "-"*20)
print(ts.resample('2T', closed='right', label='right').sum(), end='\n\n') 

# offset
print("closed='right', label='right', loffset='-1s''", "-"*20)
print(ts.resample('2T', closed='right', label='right', loffset='-1s').sum(), end='\n\n') 

# ohlc : open(시가), high(고가), low(저가), close(종가)
print("ohlc : open(시가), high(고가), low(저가), close(종가)", "-"*10)
print(ts.resample('2T').ohlc(), end='\n\n')

print("df", "-"*20)
df = pd.DataFrame(
    np.random.randn(10, 4),
    index=pd.date_range('2019-10-01', periods=10, freq='M'),
    columns=(['C1', 'C2', 'C3', 'C4'])
)
print(df, end='\n\n')

# DataFrame에 대한 resampling

# resample('Y') : 년 단위 resampling
print("resample('Y') : 년 단위 resampling", '-'*20)
print(df.resample('Y').asfreq(), end='\n\n')

# 주, 금요일 단위 resampling
print("주, 금요일 단위 resampling", '-'*20)
print(df.resample('W-FRI').asfreq(), end='\n\n')

# ffill() : 누락값 채우기
print("ffill() : 누락값 채우기", '-'*20)
print(df.resample('W-FRI').ffill(), end='\n\n')

# ffill(limit=2) : 누락값 채우기 + 채우는 행 개수 제한
print("ffill() : 누락값 채우기 + 채우는 행 개수 제한", '-'*20)
print(df.resample('W-FRI').ffill(limit=3), end='\n\n')

# resample('Q-DEC').mean()
print("resample('Q-DEC').mean()", '-'*20)
print(df.resample('Q-DEC').mean(), end='\n\n')
