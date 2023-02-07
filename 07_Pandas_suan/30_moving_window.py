

import numpy as np
import pandas as pd
from datetime import datetime
import pytz 

print("df", "-"*20)
df = pd.DataFrame(
    np.random.randn(300, 4),
    index=pd.date_range('2020-01-01', periods=300, freq='D'),
    columns=['C1', 'C2', 'C3', 'C4']
)
print(df)

# rolling
print("rolling() : 지정한 값만큼 윈도우를 움직여서 window에 해당하는 곳만 처리", "-"*20)
print(df.rolling(3).mean(), end='\n\n') # window를 3만큼 움직여서 3행부터 처리
print(df.rolling(5).mean(), end='\n\n') # window를 5만큼 움직여서 5행부터 처리

print(df.C1.rolling(5, min_periods=3).std(), end='\n\n') # 원하는 column만 보기
print(df.rolling(5, min_periods=3).std()[:10], end='\n\n') # slicing하여 보기

# 확장 window
print("rolling().expanding()", "-"*20)
print(df.rolling(5, min_periods=3).std().expanding().mean(), end='\n\n')

# ewm : rolling + expanding
print("ewm : rolling + expanding", "-"*20)
print(df.C1.rolling(30, min_periods=20).mean().plot(style='--', label='Simple MA'))
print(df.C1.ewm(span=30).mean().plot(style='-', label='EWMA'))

# rolling().corr()
print("rolling().corr()", "-"*20)
print(df.C1.rolling(100, min_periods=50).corr(df.C3).plot())  # C1과 C3와 상관관계 분석 --> rand으로 값을 세팅했기 떄문에 상관이 없지만 이러한 기능이 있다는 것