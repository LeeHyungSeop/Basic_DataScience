import numpy as np
import pandas as pd

s = pd.Series(np.random.randint(0, 10, 5))
print(s)

df = pd.DataFrame(
    np.random.randint(0, 10), (3, 3),
    columns=['A', 'B', 'C']
)
print(df)

# np.exp()
print("np.exp()", '-'*20)
print(np.exp(s))

# np.cos()
print("np.cos()", '-'*20)
print(np.cos(df * np.pi / 4))

s1 = pd.Series([1, 3, 5, 7, 9], index=[0, 1, 2, 3, 4])
s2 = pd.Series([2, 4, 6, 8, 10], index=[1, 2, 3, 4, 5])

# + : index를 기준으로 연산한다. 따라서 matching이 안되는 index는 NaN
print("s1 + s2", '-'*20)
print(s1 + s2, end='\n\n')

# s1.add(s2, fill_value=0) : matching되지 않는 value들을 0으로 판단하고 계산하라
print("s1.add(s2, fill_value=0)", '-'*20)
print(s1.add(s2, fill_value=0), end='\n\n')

# df1 DataFrame 생성
print("df1 DataFrame 생성", '-'*20 )
df1 = pd.DataFrame(
    np.random.randint(0, 20, (3, 3)),
    columns=list('ABC')
)
print(df1)

# df2 DataFrame 생성
print("df2 DataFrame 생성", '-'*20 )
df2 = pd.DataFrame(
    np.random.randint(0, 20, (5, 5)),
    columns=list('BAECD')
)
print(df2)

# df1 + df2
print("df1 + df2", '-'*20)
print(df1 + df2, end='\n\n')

# df1.stack().mean() : NaN대신 df1의 평균값들로 더하기
print(".stack().mean() : ", "-"*20)
fvalue = df1.stack().mean() # 평균 구하기 위해 stack()
print(fvalue) # 평균값 출력
print(df1.add(df2, fill_value=fvalue)) # NaN 대신 평균값을 더함