# 다중 인덱스 재정렬

import numpy as np
import pandas as pd

idx = pd.MultiIndex.from_product(
    [['a', 'b', 'c'], [1, 2]],
    names=['name1', 'name2']
)
print(idx, end='\n\n')

idx_tuples = [
    ('서울특별시', 2010), ('서울특별시', 2020),
    ('부산광역시', 2010), ('부산광역시', 2020),
    ('인천광역시', 2010), ('인천광역시', 2020),
    ('대구광역시', 2010), ('대구광역시', 2020),
    ('대전광역시', 2010), ('대전광역시', 2020),
    ('광주광역시', 2010), ('광주광역시', 2020)
]
pop_tuples = [
    10312545, 9720846, 
    2567910, 3404423,
    2758296, 2947217,
    2511878, 2427954,
    1503664, 1471040,
    1454636, 1455048
]
midx = pd.MultiIndex.from_tuples(idx_tuples)
population = pd.Series(pop_tuples, index=idx_tuples)
population = population.reindex(midx)
population.index.names = ['행정구역', '년도']

male_tuples = [
    5111259, 4732275,
    1773170, 1668618,
    1390356, 1476813,
    1255245, 1198815,
    753648, 734441,
    721780, 720060
]
female_tuples = [
    5201286, 4988571,
    1794749, 1735805,
    1367940, 1479404,
    1256431, 1229139,
    750016, 736599,
    732856, 734988,
]
korea_mdf = pd.DataFrame(
    {
        '총인구수' : population,
        '남자인구수' : male_tuples,
        '여자인구수' : female_tuples
    }
)
ratio = korea_mdf['남자인구수'] * 100 / korea_mdf['여자인구수']
korea_mdf = pd.DataFrame(
    {
        '총인구수' : population,
        '남자인구수' : male_tuples,
        '여자인구수' : female_tuples,
        '남여비율' : ratio
    }
)

print(korea_mdf, end='\n\n')

# print(korea_mdf['서울특별시' : '인청광역시']) # 정렬이 안되어있기 떄문에 오류 발생
print("sort_index() : ",'-'*50)
korea_mdf = korea_mdf.sort_index()
print(korea_mdf, end='\n\n')
print(korea_mdf['서울특별시' : '인천광역시'], end='\n\n')

# unstack(level = 0) : 인덱스 값을 컬럼으로 올려주기
print("unstack(level = 0)","-"*20)
print(korea_mdf.unstack(level=0), end='\n\n')

# unstack(level = 1)
print("unstack(level = 1)","-"*20)
print(korea_mdf.unstack(level=1), end='\n\n')

# stack : 컬럼 값을 인덱스 값으로 올려주기
print("stack : 컬럼 값을 인덱스 값으로 올려주기","-"*20)
korea_mdf.stack()
print(korea_mdf, end='\n\n')

idx_flat = korea_mdf.reset_index(level = 0)
print(idx_flat)

idx_flat = korea_mdf.reset_index(level = (0, 1))
print(idx_flat)

print(idx_flat.set_index(['행정구역', '년도']))