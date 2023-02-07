import numpy as np
import pandas as pd

'''
add_categories          : 기존 카테고리에 새로운 카테고리 추가
as_ordered              : 카테고리에 순서 지정
as_unordered            : 카테고리에 순서 미지정
remove_categories       : 카테고리 제거
remove_unused_categories: 사용 안하는 카테고리 제거
rename_categories       : 카테고리 이름 변경
reorder_categories      : 새로운 카테고리에 순서 지정
set_categories          : 새로운 카테고리로 변경
'''

# s
s = pd.Series(['c1', 'c2', 'c1', 'c2', 'c1'] * 2)
print("s","-"*20)
print(s, end='\n\n')
print(s.unique(), end='\n\n') # 사실 쓰이는 값은 c1, c2 뿐이다.
print(s.value_counts(), end='\n\n')

# code
print("code","-"*20)
code = pd.Series([0, 1, 0, 1, 0] * 2)
print(code, end='\n\n')

# d
print("d","-"*20)
d = pd.Series(['c1', 'c2'])
print(d, end='\n\n')

# take() : 0은 c1, 1은 c2로 붙여줄 수 있다.
print("take() : 0은 c1, 1은 c2로 붙여줄 수 있다.", "-"*20)
print(d.take(code))


print("df", "-"*20)
df = pd.DataFrame(
    {
        'id' : np.arange(len(s)),
        'c' : s,
        'v' : np.random.randint(1000, 5000, size=len(s))
    }
)
print(df, end='\n\n')

# astype() : category data type 만드는 방법 1
print("astype() : data type 바꾸기","-"*20)
c = df['c'].astype('category')
print(c, end='\n\n')
print(c.values.categories, end='\n\n')

print(c.values.codes, end='\n\n') # c1, c2를 모두 저장하는 것 보다 (c1, c2)를 저장하고 그것을 표현하는 (0, 1)의 codes로 나타내면 더욱 효율적이다

df['c'] = c # data type을 category로 바꾼 것을 반영하기
print(df.c, end='\n\n')

# Categorical() : category data type 만드는 방법 2
print("Categorical() : category data type 만드는 방법 2", "-"*10)
c = pd.Categorical(['c1', 'c2', 'c3', 'c1', 'c2'])
print(c, end='\n\n')

# Categorical.from_codes() : category data type 만드는 방법 3
print("Categorical.from_codes() : category data type 만드는 방법 3", "-"*10)
categories = ['c1', 'c2', 'c3']
codes = [0, 1, 2, 0, 1]
c = pd.Categorical.from_codes(codes, categories)
print(c, end='\n\n')

# Categorical.from_codes(ordered=True) : category data type 만드는 방법 3 (순서 지정)
print("Categorical.from_codes(ordered=True) : category data type 만드는 방법 3(순서 지정)", "-"*10)
c = pd.Categorical.from_codes(codes, categories, ordered=True)
print(c, end='\n\n')

# as_ordered : category data type 만드는 방법 3 (순서 지정)
print("as_ordered : category data type 만드는 방법 4(순서 지정)", "-"*10)
print(c.as_ordered(), end='\n\n')
print(c.codes, end='\n\n')
print(c.categories, end='\n\n')

# set_categories : 새로운 카테고리 적용
print("set_categories : 새로운 카테고리 적용", "-"*20)
c = c.set_categories(['c1', 'c2', 'c3', 'c4', 'c5'])
print(c.categories, end='\n\n') 
print(c.value_counts(), end='\n\n') # 기존의 c1, c2, c3는 값이 있지만 새로 추가된 c4, c5는 값이 없다.
print(c[c.isin(['c1', 'c3'])], end='\n\n') 

# remove_unused_categories : 사용하지 않는 카테고리 삭제
print("remove_unused_categories : 사용하지 않는 카테고리 삭제", "-"*20)
c = c.remove_unused_categories()
print(c.categories, end='\n\n') # 값을 사용하고 있던 c1, c2, c3만 남고 값이 없던 c4, c5는 삭제되었다.


