import numpy as np
import pandas as pd

df = pd.DataFrame(
    np.random.rand(6, 3),
    index=[['a', 'a', 'b', 'b', 'c', 'c'],[1, 2, 1, 2, 1, 2]],
    columns=['c1', 'c2', 'c3']
)
print(df, end='\n\n')

# from_arrays() : multi indexing할 대상이 array일 때
print("from_arrays() : multi indexing할 대상이 array일 때", '-'*20)
mi_from_arr = pd.MultiIndex.from_arrays([['a', 'a', 'b', 'b', 'c', 'c'],[1, 2, 1, 2, 1, 2]])
print(mi_from_arr, end='\n\n')

# from_tuples() : multi indexing할 대상이 tuple일 때
print("from_tuples() : multi indexing할 대상이 tuple일 때", '-'*20)
mi_from_tuple = pd.MultiIndex.from_tuples([('a', 1), ('a', 2),('b', 1), ('b', 2),('c', 1), ('c', 2)])
print(mi_from_tuple, end='\n\n')

# from_product() : multi indexing할 대상이 product일 때
print("from_product() : multi indexing할 대상이 product일 때", '-'*20)
mi_from_product = pd.MultiIndex.from_product([['a', 'b', 'c'],[1, 2]])
print(mi_from_product, end='\n\n')

# levels, codes 사용하기 : levels, codes에 따라서 multi indexing
print("levels, codes 사용하기 : levels, codes에 따라서 multi indexing", '-'*20)
mi_levels_codes = pd.MultiIndex(
    levels=[['a', 'b', 'c'], [1, 2]],
    codes=[[0, 0, 1, 1, 2, 2,], [0, 1, 0, 1, 0, 1]] # --> codes값에 따라서 a, a, b, b, c, c 가 각각 0, 1, 0, 1, 0, 1
)
print(mi_levels_codes)

# 인덱스에 이름 붙이기
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
print(population)

# multi indexing을 이용하여 계층 생성하기
print("\nmulti indexing을 이용하여 계층 생성하기", '-'*20)
idx = pd.MultiIndex.from_product(
    [['a', 'b', 'c'], [1, 2]],
    names=['name1', 'name2']
)
cols = pd.MultiIndex.from_product(
    [['c1', 'c2', 'c3'], [1, 2]],
    names=['col_name1', 'col_name2']
)
data = np.round(np.random.randn(6, 6), 2)
mdf = pd.DataFrame(data, index=idx, columns=cols)
print(mdf, end='\n\n')
print(mdf['c2'], end='\n\n')