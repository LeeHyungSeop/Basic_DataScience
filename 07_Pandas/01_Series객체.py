# Series 객체 살펴보기

import numpy as np
import pandas as pd

print(pd.__version__)


# Series : 여러 type의 데이터에 대해 Series 객체로 반환해준다. 
s = pd.Series([0, 0.25, 0.5, 0.75, 1.0])
print(s)

# value : s Series의 value만 
print("\nvalue", "-"*20)
print(s.values)
# index : s Series의 index만 
print("\nindex", "-"*20)
print(s.index)

# Series 객체 생성의 옵션으로, index 지정이 가능 
print("\nSeries 객체 생성의 옵션으로, index 지정이 가능 ", "-"*10)
s = pd.Series([0, 0.25, 0.5, 0.75, 1.0], index=['a','b','c','d','e'])
print(s)

# 지정했던 index로 값 출력 가능
print("\n지정했던 index로 값 출력 가능", "-"*10)
print(s['b'], s['e'])
print(s[['b', 'c', 'd']])

# s Series에 지정한 index의 유무 판단
print("\n지정한 index의 유무 판단", "-"*10)
print('a' in s)
print('z' in s)


s = pd.Series([0, 0.25, 0.5, 0.75, 1.0], index=[2,4,6,8,10])
print(s)

# iloc : 행 단위 slicing
print("\niloc : 행 단위 slicing", "-"*20)
print(s.iloc[2:])

# unique : unique한 값만 출력
s = pd.Series([0, 0, 1, 2, 2], index=[1, 2, 3, 4, 5])
print("\nunique : unique한 값만 출력", "-"*20)
print(s.unique())

# value_counts : 값이 몇개인지 출력
print("\nvalue_counts : 값이 몇개인지 출력", "-"*20)
print(s.value_counts())

# isin : 해당 값들이 어느 인덱스에 있는지 bool type으로 반환
s = pd.Series([0, 0.25, 0.5, 0.75, 1.0], index=[1, 2, 3, 4, 5])
print("\nisin : 해당 값들이 어느 인덱스에 있는지 bool type으로 반환", "-"*20)
print(s.isin([0, 0.5, 1]))

# tuple형 변수로 Series 객체 생성 가능.
print("tuple형 변수로 Series 객체 생성 가능", "-"*10)
pop_tuple = {
    "서울특별시" : 9720846,
    "부산광역시" : 3404423,
    "인천광역시" : 2947217,
    "대구광역시" : 2427954,
    "대전광역시" : 1471040,
    "광주광역시" : 1455048
}

population = pd.Series(pop_tuple)
print(population, end='\n\n')
print(population.keys(), end='\n\n')
print(population.sort_values(), end='\n\n')
print(population["서울특별시" : "인천광역시"], end='\n\n')
