# 다중 인덱싱(Multi Indexing)
# 고차원 데이터 처리

import numpy as np
import pandas as pd

pop_tuple = {
    "서울특별시" : 9720846,
    "부산광역시" : 3404423,
    "인천광역시" : 2947217,
    "대구광역시" : 2427954,
    "대전광역시" : 1471040,
    "광주광역시" : 1455048
}
population = pd.Series(pop_tuple)
male_tuple = {
    "서울특별시" : 4732275,
    "부산광역시" : 1668618,
    "인천광역시" : 1476813,
    "대구광역시" : 1198815,
    "대전광역시" : 734441,
    "광주광역시" : 720060
}
male = pd.Series(male_tuple)
female_tuple = {
    "서울특별시" : 4988571,
    "부산광역시" : 1735805,
    "인천광역시" : 1470404,
    "대구광역시" : 1229139,
    "대전광역시" : 736599,
    "광주광역시" : 734988
}
female = pd.Series(female_tuple)

korea_df = pd.DataFrame({
    '인구수' : population,
    '남자인구수' : male,
    '여자인구수' : female
})
print(korea_df, end='\n\n')

# 원하는 multi index 생성
print("원하는 index 생성", '-'*20)
idx_tuples = [
    ('서울특별시', 2010), ('서울특별시', 2020),
    ('부산광역시', 2010), ('부산광역시', 2020),
    ('인천광역시', 2010), ('인천광역시', 2020),
    ('대구광역시', 2010), ('대구광역시', 2020),
    ('대전광역시', 2010), ('대전광역시', 2020),
    ('광주광역시', 2010), ('광주광역시', 2020)
]
print(idx_tuples)

# 생성했던 index와 실제 값들 matching (방법 1 : 직접)
print("생성했던 index와 실제 값들 matching", '-'*20)
pop_tuples = [
    10312545, 9720846, 
    2567910, 3404423,
    2758296, 2947217,
    2511878, 2427954,
    1503664, 1471040,
    1454636, 1455048
]
population = pd.Series(pop_tuples, index=idx_tuples)
print(population, end='\n\n')

# 생성했던 index와 실제 값들 matching (방법 2 : from_tuples() method 이용)
print("생성했던 index와 실제 값들 matching (방법 2 : from_tuples() method 이용)", '-'*20)
midx = pd.MultiIndex.from_tuples(idx_tuples)
population = population.reindex(midx)
print(population, end='\n\n')
print(population[:, 2010], end='\n\n')
print(population['대전광역시', :], end='\n\n')

# unstack() : multi indexing으로 만들어놨던 Series 객체를 DataFrame 객체로 변환해준다.
print("unstack() : multi indexing으로 만들어놨던 Series 객체를 DataFrame 객체로 변환", '-'*10)
korea_mdf = population.unstack()
print(korea_mdf, end='\n\n')

# stack () : DataFrame을 다중 indexing을 가진 Series로 변환
print("stack () : DataFrame을 다중 indexing을 가진 Series로 변환", '-'*10)
population = korea_mdf.stack()
print(population, end='\n\n')

# 남자, 여자인구수도 다중인덱스에 대응하는 값들로 만들어서 추가하기
print("남자, 여자인구수도 다중인덱스에 대응하는 값들로 만들어서 추가하기", "-"*10)
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
print(korea_mdf, end='\n\n')

# 남여비율 계산하여 추가하기
print("남여비율 계산하여 추가하기", '-'*20)
ratio = korea_mdf['남자인구수'] * 100 / korea_mdf['여자인구수']
korea_mdf = pd.DataFrame(
    {
        '총인구수' : population,
        '남자인구수' : male_tuples,
        '여자인구수' : female_tuples,
        '남여비율' : ratio
    }
)
print(korea_mdf)