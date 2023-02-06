import numpy as np
import pandas as pd
from datetime import datetime

'''
D   : Day
B   : BusinessDay 

W-MON, W-TUE, ... : Week
WON-MON, WON-TUE, .. : 월 별 주차와 요일

MS : 월 시작일
BMS : 영업일 기준 월 시작일

M : 월 마지막 일
BM : 영업일 기준 월 마지막 일

QS-JAN, QS-FEB, ... : 분기 시작
BQS-JAN, BQS_FEB, ... : 영업일 기준 분기 시작

Q-JAN, Q-FEB, ... : 분기 마지막
BQ-JAN, BQ-FEB, ... : 영업일 기준 분기 마지막

AS-JAN, AS-FEB, ... : 연초
BAS-JAN, BAS-FEB, ... : 영업일 기준 연초

A-JAN, A-FEB, : 연말
BA-JAN, BA-FEB, : 영업일 기준 연말

H   : 시간
BH  : 영업 시간
T 또는 min : 분
S   : 초
L 또는 ms   : 밀리초
U : 마이크로초
N : 나노초
'''

# timedelta_range(freq='H')
print("timedelta_range(freq='H') : 시간 단위", "-"*20)
print(pd.timedelta_range(0, periods=5, freq='H'), end='\n\n')

# timedelta_range(freq='T')
print("timedelta_range(freq='T') : 분 단위", "-"*20)
print(pd.timedelta_range(0, periods=5, freq='T'), end='\n\n')

# timedelta_range(freq='1H30T')
print("timedelta_range(freq='1H30T') : 1시간 30분 단위", "-"*20)
print(pd.timedelta_range(0, periods=5, freq='1H30T'), end='\n\n')

# date_range(freq='B')
print("date_range(freq='B') : 영업일 단위(주말 제외)", "-"*20)
print(pd.date_range(0, periods=5, freq='B'), end='\n\n')

# date_range(freq='2H')
print("date_range(freq='2H') : 2시간 단위", "-"*20)
print(pd.date_range('2020-01-01', periods=5, freq='2H'), end='\n\n')

# date_range(freq='S')
print("date_range(freq='S') : 초 단위", "-"*20)
print(pd.date_range('2020-01-01', periods=5, freq='S'), end='\n\n')
