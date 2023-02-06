import numpy as np
import pandas as pd
from datetime import datetime

'''
타임스탬프  : Timestamp 타입 제공 
기간      : Period 타입 제공
지속 시간  : Timedelta 타입 제공
'''

# to_datetime() : 다양한 날짜표현을 DateTimeIndex로 변환해주는 method
print("to_datetime() : 다양한 날짜표현을 DateTimeIndex로 변환해주는 method", "-"*10)
dates = pd.to_datetime(['12-12-2019', datetime(2020, 1, 1), '2nd of Feb, 2020', '2020-Mar-4', '20200701'])
print(dates, end='\n\n')

# to_period('D') : Period index로 변환
print("to_period('D') : Period index로 변환", "-"*20)
print(dates.to_period('D'), end='\n\n')

#  TimedeltaInex로 변환
print("dates - dates[0] : TimedeltaInex로 변환", "-"*20)
print(dates - dates[0], end='\n\n')

# date_range() : 
print("date_range() : default freq='D'", "-"*20)
print(pd.date_range('2019-01-01', '2019-12-31'), end='\n\n')

# date_range(periods=7) : 
print("date_range(periods=7) :", "-"*20)
print(pd.date_range('2019-01-01', periods=7), end='\n\n')

# date_range(periods=7, freq='M') : 
print("date_range(periods=7, freq='M') :", "-"*20)
print(pd.date_range('2019-01-01', periods=7, freq='M'), end='\n\n')

# date_range(periods=7, freq='H') : 
print("date_range(periods=7, freq='H') :", "-"*20)
print(pd.date_range('2019-01-01', periods=7, freq='H'), end='\n\n')

# NaT : Not a Time
print("NaT : Not a Time", "-"*20)
idx = pd.to_datetime(['2020-01-01 12:00:00', '2020-01-02 00:00:00'] + [None])
print(idx)
print(idx[2], end='\n\n')

# isnull() : null값이 어딨는지
print("isnull() : null값이 어딨는지", "-"*20)
idx = pd.to_datetime(['2020-01-01 12:00:00', '2020-01-02 00:00:00'] + [None])
print(pd.isnull(idx), end='\n\n')