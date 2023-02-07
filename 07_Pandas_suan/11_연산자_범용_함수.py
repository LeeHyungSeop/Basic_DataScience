import numpy as np
import pandas as pd

# NumPy로 랜덤 행렬 생성하기
a = np.random.randint(1, 10, size=(3, 3))
print(a)

# NumPy의 broadcasting (+)
print("NumPy의 broadcasting", "-"* 20)
print(a + a[0])

# np에 대한 DataFrame 생성
df = pd.DataFrame(a, columns=list('ABC'))
print(df)

# DataFrame의 broadcasting (+)
print("DataFrame의 broadcasting", "-"* 20)
print(df, end='\n\n')
print(df + df.iloc[0])

# add
print("add()", "-"* 20)
print(df, end='\n\n')
print(df.add(df.iloc[0]))

# sub / subtract
print("sub()", "-"* 20)
print(df, end='\n\n')
print(df.sub(df['A'], axis=0))
print(df.subtract(df.iloc[0]))

# mul / multiply
print("mul() / multiply", "-"* 20)
print(df, end='\n\n')
print(df.mul(df['A'], axis=0))
print(df.multiply(df.iloc[0]))

# truediv() / div() / divide() / floordiv()
print("truediv() / div() / divide() / floordiv()", "-"* 20)
print(df, end='\n\n')

print(df / df.iloc[0])
print(df.truediv(df.iloc[0]))
print(df.div(df.iloc[0]))
print(df.divide(df.iloc[0]), end='\n\n')

print(df // df.iloc[0])
print(df.floordiv(df.iloc[0]))

# mod()
print("mod()", "-"* 20)
print(df, end='\n\n')
print(df % df.iloc[0])
print(df.mod(df.iloc[0]))

# pow()
print("pow()", "-"* 20)
print(df, end='\n\n')
print(df ** df.iloc[0])
print(df.pow(df.iloc[0]), end='\n\n')

row = df.iloc[0, ::2] # 0행의 처음부터 끝까지 2단위로 --> (0, A), (0, C)
print(df)
print(row)
print(df - row) # (0,A), (0,C)을 0만들기 --> 원하는 부분 0만들기