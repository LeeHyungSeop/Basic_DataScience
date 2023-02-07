# DataFrame Indexing

import numpy as np
import pandas as pd

print("tuple형 변수로 DataFame 객체 사용", "-"*20)
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

print(korea_df['남자인구수'], end='\n\n')

print(korea_df.남자인구수, end='\n\n')
print(korea_df.여자인구수, end='\n\n')

korea_df['남여비율'] = (korea_df['남자인구수'] * 100 / korea_df['여자인구수'])
print(korea_df.남여비율, end='\n\n')

print(korea_df.values, end='\n\n')
print(korea_df.values[0], end='\n\n')
print(korea_df.T, end='\n\n')
print(korea_df['인구수'], end='\n\n')

# loc : 값으로 indexing
print('loc : 값으로 indexing', '-'*20)
print(korea_df.loc[:'인천광역시', :'남자인구수'], end='\n\n')
print(korea_df.loc[(korea_df.여자인구수 > 1000000)], end='\n\n') # 여자인구수가 100만명 초과인 데이터
print(korea_df.loc[(korea_df.인구수 < 2000000)], end='\n\n')    # 전체인구수가 200만명 미만인 데이터
print(korea_df.loc[korea_df.남여비율 > 100], end='\n\n')         # 남자의 비율이 더 많은 도시
print(korea_df.loc[(korea_df.인구수 > 2500000) & (korea_df.남여비율 < 100)]) # 인구수가 250만명 이상이고 남자비율이 더 적은 도시



# iloc : index로 indexing
print('\niloc : index으로 indexing', '-'*20)
print(korea_df.iloc[:3, :2])

# at
# iat
# reindex
# get_value
# set_value