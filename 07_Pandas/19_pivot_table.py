import numpy as np
import pandas as pd

'''
values   : 집계하려는 컬럼 이름 혹은 이름의 리스트
index    : 피벗테이블의 로우를 그룹으로 묶을 컬럽 이름이나 그룹 키
columns  : 피벗테이블의 컬럼를 그룹으로 묶을 컬럽 이름이나 그룹 키
aggfunc  : 집계 함수나 함수 리스트. 기본값으로 mean 사용
fill_value : 결과 테이블에서 누락된 값 대체를 위한 값
dropna : True인 경우 모든 항목이 NA인 컬럼은 포함하지 않음
margins : 부분합이나 총계를 담기 위한 로우/컬럼 추가 여부. default : False
'''

df = pd.DataFrame({ 
    'c1' : ['a', 'a', 'b', 'b', 'c', 'd', 'b'],
    'c2' : ['A', 'B', 'B', 'A', 'D', 'C', 'C'],
    'c3' : np.random.randint(7),
    'c4' : np.random.random(7)
})
print("df",'-'*20)
print(df, end='\n\n')

# pivot_table
print("pivot_table", "-"*20)
pt = df.pivot_table(
    ['c3', 'c4'],
    index=['c1'],
    columns=['c2']
)
print(pt, end='\n\n')

# margins=True
print("margins=True : 부분합이나 총계 포함.", "-"*20)
pt = df.pivot_table(
    ['c3', 'c4'],
    index=['c1'],
    columns=['c2'],
    margins=True 
)
print(pt, end='\n\n') # All index(부분합/총계) 추가됨.

#  aggfunc=sum
print("aggfunc=sum : 원하는 aggregate function 지정", "-"*20)
pt = df.pivot_table(
    ['c3', 'c4'],
    index=['c1'],
    columns=['c2'],
    margins=True,
    aggfunc=sum
)
print(pt, end='\n\n') 

#  fill_value=0
print("fill_value=0 : NaN값 대신 0 지정", "-"*20)
pt = df.pivot_table(
    ['c3', 'c4'],
    index=['c1'],
    columns=['c2'],
    margins=True,
    aggfunc=sum,
    fill_value=0
)
print(pt, end='\n\n') 

#  crosstab : 그룹의 빈도를 계산하기 위한 피벗테이블의 한 유형
print("crosstab : 그룹의 빈도를 계산하기 위한 피벗테이블의 한 유형", "-"*20)
print(pd.crosstab(df.c1, df.c2))

#  crosstab : 그룹의 빈도를 계산하기 위한 피벗테이블의 한 유형
print("crosstab : 그룹의 빈도를 계산하기 위한 피벗테이블의 한 유형", "-"*20)
print(pd.crosstab(df.c1, df.c2, values=df.c3, margins=True, aggfunc=sum, fill_value=0))