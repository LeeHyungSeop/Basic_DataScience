import numpy as np
import pandas as pd

'''
isnull : 누락되거나 NA인 값을 boolean값으로 변환
notnull : isnull의 반대
dropna : 누락된 데이터가 있는 축 제외
fillna : 누락된 값을 대체하거나 ffill이나 bfill로 보간 method 적용
'''

s = pd.Series([1, 2, np.nan, 'String', None])
print("s", "-"*20)
print(s, end='\n\n')

print("s.isnull() : np.nan, None은 isnull()에서 True", "-"*20)
print(s.isnull(), end='\n\n')

print("s.notnull() : np.nan, None은 notnull()에서 False", "-"*20)
print(s.notnull(), end='\n\n')

print("s.dropna() : null인 축 제외", "-"*20)
print(s.dropna(), end='\n\n')

print("df", "-"*20)
df = pd.DataFrame({
    'a' : np.random.randn(100), 
    'b' : np.random.randn(100), 
    'c' : np.random.randn(100)
})
print(df, end='\n\n')

print("df[3] = np.nan : 3이라는 column 추가, 모두 np.nan으로 초기화", "-"*20)
df[3] = np.nan
print(df, end='\n\n')

print("dropna(axis='columns', how='all')  : columns축에서 nan 포함된 column '모두' 삭제", "-"*10)
print(df.dropna(axis='columns', how='all'), end='\n\n')

print("dropna(axis='rows', thresh=3) : ", "-"*20)
df = df.dropna(axis='rows', thresh=3)
print(df, end='\n\n')

print("dropna(axis='rows', thresh=3) : ", "-"*20)
print(df.dropna(axis='rows', thresh=3), end='\n\n')

# s.fillna()
print("s.fillna(0) : nan값을 0으로 채운다", "-"*20)
print(s.fillna(0), end='\n\n')

# s.fillna(method = 'ffill')
print("s.fillna(method='ffill') : front fill -> nan값을 이전의 값으로 채운다", "-"*20)
print(s.fillna(method='ffill'), end='\n\n')

# s.fillna(method = 'bfill')
print("s.fillna(method='bfill') : back fill -> nan값을 다음의 값으로 채운다", "-"*20)
print(s.fillna(method='bfill'), end='\n\n')

print("df.fillna(method='ffill', axis=1)", "-"*20) 
print(df.fillna(method='ffill', axis=1), end='\n\n')

print("df.fillna(method='bfill', axis=1)", "-"*20) 
print(df.fillna(method='bfill', axis=1), end='\n\n')