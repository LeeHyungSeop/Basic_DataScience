import numpy as np
import pandas as pd

'''
누락값 처리
대부분의 실제 데이터들은 정제되지 않고 누락값들이 존재
서로 다른 데이터들은 다른 형태의 결측을 가짐
결측 데이터는 null, NaN, NA로 표기
'''

# None : 파이썬 누락 데이터
print("None : 파이썬 누락 데이터", "-"*20)
a = np.array([1, 2, None, 4, 5])
print(a)

# print(a.sum()) # 누락값이 있으면 다음과 같은 연산 불가능

# np.nan : 누락된 수치 데이터
print("np.nan : 누락된 수치 데이터", "-"*20)
a = np.array([1, 2, np.nan, 4, 5])
print(a.dtype)

print("0 + np.nan", "-"*20)
print(0 + np.nan, end='\n\n')
print("np.nan + np.nan", "-"*20)
print(np.nan + np.nan, end='\n\n')
print("a.sum(), a.min(), a.max()", "-"*20)
print(a.sum(), a.min(), a.max(), end='\n\n')

print("np.nansum(a), np.nanmin(a), np.nanmax(a) : np.nan 값이 있는 것을 고려하여 계산하도록 하는 method", "-"*10)
print(np.nansum(a), np.nanmin(a), np.nanmax(a), end='\n\n')

# pandas에서 None을 np.nan으로 변환해준다 (1)
print("pandas에서 None을 np.nan으로 변환해준다 (1)", "-"*20)
print(pd.Series([1, 2, np.nan, 4, None]), end='\n\n')

# pandas에서 None을 np.nan으로 변환해준다 (2)
print("pandas에서 None을 np.nan으로 변환해준다 (2)", "-"*20)
s = pd.Series(range(5), dtype=int)
print(s, end='\n\n')
s[0] = None
s[3] = np.nan
print(s, end='\n\n')  # None을 넣어도 NaN으로 바뀐다

