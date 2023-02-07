import numpy as np
import pandas as pd

df1 = pd.DataFrame({
    '학생':['홍길동','이순신','임꺽정','김유신'],
    '학과':['경영학과','교육학과','컴퓨터학과','통계학과']
})
print(df1)
df2 = pd.DataFrame({
    '학생' : ['홍길동','이순신','임꺽정','김유신'],
    '입학년도' : [2012, 2016, 2019, 2020]
})
print(df2)
df4 = pd.DataFrame({
    '학과':['경영학과','교육학과','컴퓨터학과','통계학과'],
    '학과장' : ['황희', '장영실', '안창호', '정약용']
})
print(df4)

# merge() : DataFrame을 병합
print("merge() : DataFrame을 병합", '-'*20)
df3 = pd.merge(df1, df2)
print(df3, end='\n\n')

print(pd.merge(df3, df4), end='\n\n')

df5 = pd.DataFrame(
    {
        '학과' : ['경영학과','교육학과','교육학과','컴퓨터학과','컴퓨터학과','통계학과'],
        '과목' : ['경영개론','기초수학','물리학','프로그래밍','운영체제','확률론']
    }
)
print(pd.merge(df1, df5), end='\n\n') # '학과'가 공통되므로 '학과'기준으로 merge --> 학생이 중복되어 나타나는 경우 존재

# merge(on='')
print("merge(on='학과') : '학생'을 기준으로 merge", '-'*20)
print(pd.merge(df1, df2, on='학생'),end='\n\n') # '학생'을 기준으로 merge --> 학생이 중복되어 나타나는 경우 없음

df6 = pd.DataFrame({
    '이름' : ['홍길동', '이순신', '임꺽정', '김유신'],
    '성적' : ['A','A+',"B",'A+']
})
print(df6, end='\n\n')

# merge(left_on="학생", right_on="이름") : df1의 '학생'과 df6의 '이름'은 column명이 다른데 값들은 똑같은 경우, merge하는 방법
print("merge(left_on='학생', right_on='이름') : df1의 '학생'과 df6의 '이름'은 column명이 다른데 값들은 똑같은 경우, merge하는 방법")
print(pd.merge(df1, df6, left_on='학생', right_on='이름'), end='\n\n')

print(pd.merge(df1, df6, left_on='학생', right_on='이름').drop('이름', axis=1), end='\n\n') # '이름'이라는 column명은 삭제 --> '학생'과 값이 중복되니까

mdf1 = df1.set_index('학생')
mdf2 = df2.set_index('학생')

print("mdf1",'-'*20)
print(mdf1)
print("mdf2",'-'*20)
print(mdf2, end='\n\n')

print(pd.merge(mdf1, mdf2, left_index=True, right_index=True))

# join
print("join", '-'*20)
print(mdf1.join(mdf2), end='\n\n')
print(pd.merge(mdf1, df6, left_index=True, right_on='이름'), end='\n\n')

print("df7", '-'*20)
df7 = pd.DataFrame({
    '이름' : ['홍길동', '이순신', '임꺽정'],
    '주문음식' : ['햄버거', '피자', '짜장면']
})
print(df7)

print("df8", '-'*20)
df8 = pd.DataFrame({
    '이름' : ['홍길동', '이순신', '김유신'],
    '주문음료' : ['콜라', '사이다', '커피']
})
print(df8)

# merge(how='outer')
print("merge(how='outer')", '-'*20)
print(pd.merge(df7, df8), end='\n\n') # '주문음식'과 '주문음료' column 값이 있는 '홍길동'과 '이순신'만 merge가 된다. --> default / how : inner
print(pd.merge(df7, df8, how='inner'), end='\n\n') # default / how : inner
print(pd.merge(df7, df8, how='outer'), end='\n\n') # '주문음식'과 '주문음료' column이 없어도 merge --> 누락된 값은 NaN으로 할당

# merge(how='left')
print("merge(how='left')", '-'*20) 
print(pd.merge(df7, df8, how='left'), end='\n\n') # left는 df7. df7의 column은 '이름'과 '주문음식'이므로 해당 column이 있는 값들만 출력
# merge(how='right')
print("merge(how='right')", '-'*20) 
print(pd.merge(df7, df8, how='right'), end='\n\n') # right는 df8. df8의 column은 '이름'과 '주문음료'이므로 해당 column이 있는 값들만 출력

print("df9",'-'*20)
df9 = pd.DataFrame({
    '이름' : ['홍길동', '이순신', '임꺽정', '김유신'],
    '순위' : [3, 2, 4, 1]
})
print(df9)

print("df10",'-'*20)
df10 = pd.DataFrame({
    '이름' : ['홍길동', '이순신', '임꺽정', '김유신'],
    '순위' : [4, 1, 3, 2]
})
print(df10, end='\n\n')

# pd.merge(on="이름", suffixes=["_인기", "_성적"])
print("pd.merge(on='이름', suffixes=['_인기', '_성적'])", '-'*10)
print(pd.merge(df9, df10, on='이름')) # df9와 df10에서 똑같은 '순위'라는 colum이 존재하기 떄문에, '순위_x', '순위_y'로 default로 지정해줌print(pd.merge(df9, df10, on='이름')) # df9와 df10에서 똑같은 '순위'라는 colum이 존재하기 떄문에, '순위_x', '순위_y'로 default로 지정해줌
print(pd.merge(df9, df10, on='이름', suffixes=["_인기", "_성적"]), end='\n\n') # suffixes를 통해 동일한 column명에 대해서 naming 가능

