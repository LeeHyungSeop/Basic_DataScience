import numpy as np
import pandas as pd
from datetime import datetime

ts = pd.Series(
    np.random.randn(5),
    index=pd.date_range('2020-01-01', periods=5, freq='B')
)
print(ts)

# shift(2) : 지정한 숫자만큼 값 이동
print("shift() : 지정한 숫자만큼 값 아래로 이동", "-"*20)
print(ts.shift(2), end='\n\n')

# shift(-2) : 지정한 숫자만큼 값 이동
print("shift() : 지정한 숫자만큼 값 위로 이동", "-"*20)
print(ts.shift(-2), end='\n\n')

# shift(freq='B')
print("shift(freq='B') : 영업일 단위로 값 위로 이동 + 값 채워짐", "-"*20)
print(ts.shift(7, freq='B'), end='\n\n')

# shift(freq='W')
print("shift(freq='W') : 주 단위로 값 위로 이동 + 값 채워짐", "-"*20)
print(ts.shift(2, freq='W'), end='\n\n')