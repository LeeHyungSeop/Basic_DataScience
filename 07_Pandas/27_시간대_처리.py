import numpy as np
import pandas as pd
from datetime import datetime
import pytz 

'''
국제표준시(Corrdinated Universal Time, UTC)를 기준으로 떨어진 거리만큼 offset으로 시간대 처리
전 세계의 시간대 정보를 모아놓은 올슨 데이터베이스를 활용한 라이브러리인 pytz 사용
'''

print("coommon_timezones", "-"*20)
print(pytz.common_timezones, end='\n\n')

print("timezone을 Asia/Seoul로 세팅", "-"*20)
tz = pytz.timezone('Asia/Seoul')
print(tz, end='\n\n')

dinx = pd.date_range('2020-01-01 09:00', periods=7, freq='B')
ts = pd.Series(
    np.random.randn(len(dinx)),
    index=dinx
)
print("ts", "-"*20)
print(ts, end='\n\n')

print(pd.date_range('2020-01-01 09:00', periods=7, freq='B', tz='UTC')) # 표준시는 기준이기 때문에 +0시간

# timezone을 UTC로 맞춤
print("timezone을 UTC로 맞춤", "-"*20)
ts_utc = ts.tz_localize('UTC')
print(ts_utc, end='\n\n')
print(ts_utc.index, end='\n\n')

# timezone을 Asia/Seoul로 바꿈
print("timezone을 Asia/Seoul로 바꿈", "-"*20)
ts_utc = ts_utc.tz_convert('Asia/Seoul')
print(ts_utc, end='\n\n') # 기준에서 +9시간 (-> 표준시에서 +9시 된게 서울의 time zone이기 떄문)

# timezone을 Asia/Seoul로 맞춤
print("timezone을 Asia/Seoul로 맞춤", "-"*20)
ts_seoul = ts.tz_localize('Asia/Seoul')
print(ts_seoul, end='\n\n')

# timezone을 UTC로 바꿈
print("timezone을 UTC로 바꿈", "-"*20)
print(ts_seoul.tz_convert('UTC'), end='\n\n')

# timezone을 Europe/Berlin으로 바꿈
print("timezone을 Europe/Berlin으로 바꿈", "-"*20)
print(ts_seoul.tz_convert('Europe/Berlin'), end='\n\n')

# Timestamp를 UTC로 바꾸기
print("Timestamp를 UTC로 바꾸기", "-"*20)
stamp = pd.Timestamp('2020-01-01 12:00')
stamp_utc = stamp.tz_localize('UTC')
print(stamp_utc, end='\n\n')
print(stamp_utc.value, end='\n\n')

# Timestamp를 Asia/Seoul로 바꾸기
print("Timestamp를 Asia/Seoul로 바꾸기", "-"*20)
stamp = pd.Timestamp('2020-01-01 12:00')
stamp_utc = stamp_utc.tz_convert('Asia/Seoul')
print(stamp_utc, end='\n\n')
print(stamp_utc.tz_convert('Asia/Seoul').value, end='\n\n') # UTC에서 Asia/Seoul로 conver했기 때문에 동일한 값이 출력된다.

# Timestamp를 New_York으로 만들기
print("Timestamp를 New_York으로 만들기", "-"*20)
stamp_ny = pd.Timestamp('2020-01-01 12:00', tz='America/New_York')
print(stamp_ny, end='\n\n')
print(stamp_utc.value, end='\n\n')
print(stamp_ny.value, end='\n\n') # timezone이 다르니까 값이 다르게 나온다.
print(stamp_utc.tz_convert('Asia/Shanghai'), end='\n\n')

# offset 지정
print("offset 지정", "-"*20)
from pandas.tseries.offsets import Hour
stamp = pd.Timestamp('2020-01-01 12:00', tz='Asia/Seoul')
print(stamp)
print(stamp + Hour()) # +1시간
print(stamp + 3*Hour(), end='\n\n') # +3시간

print("서로 다른 timezone이 연산될 때, 자동으로 UTC로 변환되어 계산된다.", "-"*10)
print(ts_utc, end='\n\n')
ts1 = ts_utc[ : 5].tz_convert('Europe/Berlin')
ts2 = ts_utc[2 : ].tz_convert('America/New_York')
ts = ts1 + ts2 
print(ts.index, end='\n\n')