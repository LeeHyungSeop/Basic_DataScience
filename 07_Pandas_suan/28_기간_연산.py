import numpy as np
import pandas as pd
from datetime import datetime
import pytz 

p = pd.Period(2020, freq='A-JAN')
print(p, end='\n\n')
print(p+2, end='\n\n')
print(p-2, end='\n\n')

print("p2 - p1", "-"*20)
p1 =  pd.Period(2010, freq='A-JAN')
p2 =  pd.Period(2020, freq='A-JAN')
print(p2 - p1, end='\n\n')

print("pr", "-"*20)
pr = pd.period_range('2020-01-01', '2020-06-30', freq='M')
print(pr, end='\n\n')

print(pd.Series(np.random.randn(6), index=pr), end='\n\n')

print("pidx", "-"*20)
pidx = pd.PeriodIndex(['2020-1', '2020-2', '2020-4'], freq='M')
print(pidx, end='\n\n')

# freq='A-FEB'인 Period 객체 p 생성
print("freq='A-FEB'인 Period 객체 p 생성", "-"*20)
print("p", "-"*20)
p = pd.Period('2020', freq='A-FEB')
print(p, end='\n\n')

# asfreq('M', how='start')
print("asfreq('M', how='start')", "-"*20) # freq='A-FEB'이니까 start가 전 년도 3월(MAR)
print(p.asfreq('M', how='start'))

# asfreq('M', how='end')
print("asfreq('M', how='end')", "-"*20) # freq='A-FEB'이니까 end 이번 년도 2월(FEB)
print(p.asfreq('M', how='end'), end='\n\n')

# period_range(freq='A-JAN')
print("period_range(freq='A-JAN')", "-"*20)
pr = pd.period_range('2010', '2020', freq='A-JAN')
ts = pd.Series(
    np.random.randn(len(pr)),
    index=pr
)
print(ts, end='\n\n')
print(ts.asfreq('M', how='start'), end='\n\n')
print(ts.asfreq('M', how='end'), end='\n\n')
print(ts.asfreq('B', how='end'), end='\n\n') # 영업일 마지막 일 출력

# Period('2020Q2', freq='Q-JAN')
print("Period('2020Q2', freq='Q-JAN') : 2020년 2분기")
p = pd.Period('2020Q2', freq='Q-JAN')
print(p, end='\n\n')
print(p.asfreq('D', 'start'), end='\n\n')
print(p.asfreq('D', 'end'), end='\n\n')

# period_range('2019Q3', '2020Q3', freq='Q-JAN')
print("period_range('2019Q3', '2020Q3', freq='Q-JAN')", "-"*10) 
pr = pd.period_range('2019Q3', '2020Q3', freq='Q-JAN')
ts = pd.Series(np.arange(len(pr)), index=pr)
print(ts, end='\n\n')

# '2020-01-01', periods=5, freq='Q-JAN'
print("'2020-01-01', periods=5, freq='Q-JAN'", "-"*10)
pr = pd.date_range('2020-01-01', periods=5, freq='Q-JAN')
ts = pd.Series(np.arange(5), index=pr) 
print(ts, end='\n\n')
print(ts.to_period(), end='\n\n')
p = ts.to_period('M')
print(p, end='\n\n')
print(p.to_timestamp(how='start'), end='\n\n')

# '2020-01-01', periods=5, freq='D'
print("'2020-01-01', periods=5, freq='D'", "-"*5)
pr = pd.date_range('2020-01-01', periods=5, freq='D')
ts = pd.Series(np.arange(5), index=pr) 
print(ts, end='\n\n')
print(ts.to_period(), end='\n\n')

# to_period('M')
print("to_period('M')", "-"*20)
p = ts.to_period('M')
print(p, end='\n\n')
print(p.to_timestamp(how='start'), end='\n\n')