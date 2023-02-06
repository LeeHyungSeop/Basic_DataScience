import numpy as np
import pandas as pd

df = pd.DataFrame({
    'c1' : ['a', 'b', 'c'] * 2 + ['b'] + ['c'],
    'c2' : [1, 2, 1, 1, 2, 3, 3, 4]
})
print("df", "-"*20)
print(df, end='\n\n')

# duplicated()
print("duplicated() : 현재 값이 앞서 있는 값에서 중복이 있으면 True : False", "-"*20)
print(df.duplicated(), end='\n\n') # 3행의 (a,1)은 0행에 이미 있으니까 True

# drop_duplicates()
print("drop_duplicates() : 중복이 있다면 제거.. unique하게 만든다", "-"*20)
print(df.drop_duplicates(), end='\n\n') # 3, 4행이 삭제됨
 