import numpy as np
import pandas as pd

'''
count
head, tail
describe
min, max
cummin, cummax : 누적 최소값, 누적 최대값
argmin, argmax : 최소값과 최대값의 index 위치
idxmin, idxmax : 최소값과 최대값의 index값
mean, median
std, var
skew : 왜도(skewness)
kurt : 첨도(kurtosis)
mad
sum, cumsum
prod, cumprod
quantile : 0부터 1까지 분위수
diff
pct_change 
corr, cov : 상관관계, 공분산 
'''

print("df", '-'*20)
df = pd.DataFrame(
    [
        [1, 1.2, np.nan],
        [2.5, 5.5, 4.2],
        [np.nan, np.nan ,np.nan],
        [0.44, -3.1, -4.1]
    ],
    index=[1, 2, 3, 4],
    columns=['A','B','C']
)
print(df, end='\n\n')

# head() : 지정한 숫자만큼의 앞부분만 
print("head()", '-'*20)
print(df.head(2), end='\n\n')

# tail() : 지정한 숫자만큼의 앞부분만 
print("tail()", '-'*20)
print(df.tail(2), end='\n\n')

# describe() : 요약된 통계값 모두 출력
print("describe()", '-'*20)
print(df.describe(), end='\n\n')

# argmin(), argmax()
print("argmin(), argmax()", "-"*20)
print(df,end='\n\n')
print(np.argmin(df), end='\n\n')
print(np.argmax(df),end='\n\n')

# idxmin(). idxmax()
print("idxmin(), idxmax()", "-"*20)
print(df,end='\n\n')
print(df.idxmin(), end='\n\n') 
print(df.idxmax(), end='\n\n')

# std(), var()
print("std(), var()", "-"*20)
print(df,end='\n\n')
print(df.std(), end='\n\n') 
print(df.var(), end='\n\n')

# skew() / kurt() : 왜도 / 첨도
print("skew() / kurt() : 왜도 / 첨도", "-"*20)
print(df,end='\n\n')
print(df.skew(), end='\n\n') 
print(df.kurt(), end='\n\n')

# sum / cumsum() : 합 / 누적합
print("sum / cumsum() : 합 / 누적합", "-"*20)
print(df,end='\n\n')
print(df.sum(), end='\n\n') 
print(df.cumsum(), end='\n\n') 

# prod / cumprod() : 곱 / 누적곱
print("prod / cumprod() : 곱 / 누적곱", "-"*20)
print(df,end='\n\n')
print(df.prod(), end='\n\n') 
print(df.cumprod(), end='\n\n') 

# diff()
print("diff() : 차", "-"*20)
print(df,end='\n\n')
print(df.diff(), end='\n\n') 

# quantile()
print(df.quantile(q=0), end='\n\n') 
print("quantile() : 0.5분위수인 중앙값 출력", "-"*20)
print(df,end='\n\n')
print(df.quantile(), end='\n\n') 
# quantile(q=1)
print("quantile(q=1) : 1분위수인 가장 큰 값 출력", "-"*20)
print(df,end='\n\n')
print(df.quantile(q=1), end='\n\n') 
# quantile(q=0)
print("quantile(q=0) : 0분위수인 가장 작은 값 출력", "-"*20)
print(df,end='\n\n')

# corr() : 상관관계
print("corr() : 상관관계", "-"*20)
print(df.corr(),end='\n\n')

# corrwith(df.B) : B값을 기준으로 상관관계
print("corrwith(df.B) : 상관관계", "-"*20)
print(df.corrwith(df.B),end='\n\n')

# cov() : 공분산
print("cov() : 공분산", "-"*20)
print(df.cov(),end='\n\n')

# unique() : unique한 값들만 출력
print("unique() : unique한 값들만 출력", "-"*20)
print(df['A'].unique(),end='\n\n')

# value_count()
print("value_count() : 값들이 각각 몇 개 있는지 출력", "-"*20)
print(df['A'].value_counts())