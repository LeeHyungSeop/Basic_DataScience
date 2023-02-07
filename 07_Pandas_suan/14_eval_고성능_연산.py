import numpy as np
import pandas as pd

nrows, ncols = 10000, 100

df1, df2, df3, df4 = (pd.DataFrame(np.random.rand(nrows, ncols)) for i in range(4))

# eval('string형 수식') :  계산량이 많거나 연산의 크기가 커서 오래걸리는 경우
print("eval('string형 수식') :  계산량이 많거나 연산의 크기가 커서 오래걸리는 경우 사용",'-'*20)
print(pd.eval('(df1 < df2) & (df2 <= df3) & (df3 != df4)'), end='\n\n')

df = pd.DataFrame(np.random.rand(100000, 5), columns=['A', 'B', 'C', 'D', 'E'])
# head() : 여러 데이터 중 가장 앞 5개만 출력
print("head() : 여러 데이터 중 가장 앞 5개만 출력", '-'*20)
print(df.head(), end='\n\n')

print(pd.eval("df['A'] + df['B'] / df['C'] - df['D'] * df['E']"))
print(df.eval("A + B / C - D * E"), end='\n\n') 

# eval(inplace=True) : 계산 결과를 해당 DataFrame에 저장, 반영
df.eval('R = A + B / C - D * E', inplace=True)
print(df.head(), end='\n\n')

# @외부변수명 : 외부변수명을 사용 가능
print('@외부변수명 : 외부변수명을 사용 가능', '-'*20)
col_mean = df.mean(1)
print(df.eval('A + @col_mean'), end='\n\n')

# pd.eval('조건 부여')
print("pd.eval('조건 부여')", '-'*20)
print(pd.eval('df[(df.A < 0.5) & (df.B < 0.5) & (df.C > 0.5)]'), end='\n\n')

# df.query('조건 부여') : DataFrame에 query를 날려서 조건에 맞는 데이터만 출력
print("df.query('조건 부여') : DataFrame에 query를 날려서 조건에 맞는 데이터만 출력", '-'*20)
print(df.query('(A < 0.5) and (B < 0.5) and (C > 0.5)'), end='\n\n')

# df.query('조건 부여' + @외부변수) : DataFrame에 query를 날려서 조건에 맞는 데이터만 출력
print("df.query('조건 부여' + @외부변수)", '-'*20)
col_mean = df['D'].mean()
print(df.query('(A < @col_mean) and (B < @col_mean)'))