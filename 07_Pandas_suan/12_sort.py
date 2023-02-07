import numpy as np
import pandas as pd

s = pd.Series(range(5), index=['E', 'D', "C", "B", "A"])
df = pd.DataFrame(
    np.random.randint(1, 10, size=(4, 4)),
    index=[2, 4, 1, 3],
    columns=list('BDAC')
)

# sort_index() :
print("sort_index() :", "-"*20)
print(s)
print(s.sort_index(), end='\n\n')
print(df)
print(df.sort_index()) # default --> axis = 0 기준 정렬
print(df.sort_index(axis=1), end='\n\n') # --> axis = 1 기준 정렬

# sort_values() :
print("sort_values() :", "-"*20)
print(s)
print(s.sort_values(), end='\n\n')
print(df)
print(df.sort_values(by=['B', 'C']), end='\n\n') # 2차원이니까 기준(by)을 정해줘야 한다. --> B 기준 우선, 그다음 C 기준 우선 정렬

