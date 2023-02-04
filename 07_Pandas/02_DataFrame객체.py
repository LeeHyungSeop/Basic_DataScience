# DataFrame 객체 살펴보기

import numpy as np
import pandas as pd

# missing된 부분(누락값)들에 NaN값으로 대체된다.
print(pd.DataFrame([{'A':2, 'B':4, 'D':3}, {'A':4, 'B':5, 'C':7}]))

# DataFrame에 여러 option 부가 가능
print("DataFrame에 여러 option 부가 가능", "-"*10)
print(pd.DataFrame(np.random.rand(5,5),
        columns=['A','B','C','D','E'],
        index=[1, 2, 3, 4, 5]
    )
)

# tuple형 변수로 DataFame 객체 사용
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
print(population)

male_tuple = {
    "서울특별시" : 4732275,
    "부산광역시" : 1668618,
    "인천광역시" : 1476813,
    "대구광역시" : 1198815,
    "대전광역시" : 734441,
    "광주광역시" : 720060
}
male = pd.Series(male_tuple)
print(male)

female_tuple = {
    "서울특별시" : 4988571,
    "부산광역시" : 1735805,
    "인천광역시" : 1470404,
    "대구광역시" : 1229139,
    "대전광역시" : 736599,
    "광주광역시" : 734988
}
female = pd.Series(female_tuple)
print(female)

korea_df = pd.DataFrame({
    '인구수' : population,
    '남자인구수' : male,
    '여자인구수' : female
})
print(korea_df, end='\n\n')

print(korea_df.index, end='\n\n')
print(korea_df.columns, end='\n\n')

print(korea_df['여자인구수'])

