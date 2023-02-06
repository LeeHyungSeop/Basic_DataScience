import numpy as np
import pandas as pd

s = pd.Series(
    [1., 2., -999., 3., -1000., 4.]
)
print("s", "-"*20)
print(s, end='\n\n')

print("replace(-999, np.nan) : -999를 np.nan으로 치환", "-"*20)
print(s.replace(-999, np.nan), end='\n\n')
print(s.replace([-999, -1000], np.nan), end='\n\n')
print(s.replace([-999, -1000], [np.nan, 0]), end='\n\n') # 이렇게 mapping하여 처리도 가능