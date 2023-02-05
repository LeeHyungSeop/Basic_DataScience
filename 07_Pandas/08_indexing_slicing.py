import numpy as np
import pandas as pd

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
print(population, end='\n\n')
print(population['인천광역시', 2010], end='\n\n')
print(population[:, 2010], end='\n\n')
print(population[population > 3000000], end='\n\n')
print(population[['대구광역시', '대전광역시']], end='\n\n')

print("Multiple DataFrame Indexing", "-"*20)
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

# column명 지정 slicing
print(mdf['c2', 1], end='\n\n')
# 정수 index slicing
print(mdf.iloc[:3, :4], end='\n\n')


# IndexSlice 객체 이용
print("IndexSlice 객체 이용",'-'*20)
idx_slice = pd.IndexSlice
print(mdf.loc[idx_slice[:, 2], idx_slice[:, 2]])
