import numpy as np
import pandas as pd

df = pd.DataFrame({ 
    'c1' : ['a', 'a', 'b', 'b', 'c', 'd', 'b'],
    'c2' : ['A', 'B', 'B', 'A', 'D', 'C', 'C'],
    'c3' : np.random.randint(7),
    'c4' : np.random.random(7)
})
print("df",'-'*20)
print(df)
print(df.dtypes, end='\n\n')

# groupby
print("groupby",'-'*20)
print(df['c3'].groupby(df['c1']), end='\n\n') # --> 객체가 반환되기 때문에 aggregate function을 사용해야 한다.
print(df['c3'].groupby(df['c1']).mean(), end='\n\n') # --> 'c1'에 대해 groupby한 후, mean값을 c3에 저장
print(df['c4'].groupby(df['c2']).std(), end='\n\n') # 'c2'에 대해 groupby를 한 후, std값을 c4에 저장
print(df['c4'].groupby([df['c1'],df['c2']]).mean(), end='\n\n') # 'c1', 'c2'에 대해 groupby 한 후, 
print(df['c4'].groupby([df['c1'],df['c2']]).mean().unstack(), end='\n\n') # unstack() : DataFrame으로 변환

print(df.groupby('c1').mean(), end='\n\n')
print(df.groupby(['c1', 'c2']).mean(), end='\n\n')
print(df.groupby(['c1', 'c2']).size(), end='\n\n')

# groupby 객체에 for문으로 접근
print("groupby 객체에 for문으로 접근",'-'*20)
for c1, group in df.groupby('c1') :
    print(c1)
    print(group)
print(end='\n\n')
for (c1, c2), group in df.groupby(['c1', 'c2']) :
    print(c1, c2)
    print(group)

# groupby 후, 특정 column의 값에만 접근
print("groupby 후, 특정 column의 값에만 접근", "-"*20)
print(df.groupby(['c1', 'c2'])['c4'].mean(), end='\n\n')
print(df.groupby('c1')['c3'].quantile(), end='\n\n')
print(df.groupby('c1')['c3'].count(), end='\n\n')
print(df.groupby('c1')['c4'].median(), end='\n\n')

# agg([method1], [method2], ..) : groupby 후, 특정 column의 여러 method 사용
print("agg([method1], [method2], ..) : groupby 후, 특정 column의 여러 method 사용", "-"*20)
print(df.groupby(['c1', 'c2'])['c4'].agg(['mean', 'min', 'max']))

# groupby(as_index=False) : group index를 하지 않는다
print("groupby(as_index=False) : group index를 하지 않는다", "-"*20)
print(df.groupby(['c1', 'c2'], as_index=False)['c4'].mean())

# groupby(group_keys=False) : group으로 지정이 됐던게 없어진다
print("groupby(group_keys=False) : group으로 지정이 됐던게 없어진다", "-"*20)
print(df.groupby(['c1', 'c2'], group_keys=False)['c4'].mean())

# 직접 만든 top() 함수 
print("직접 만든 top() 함수 ", '-'*20)
def top(df, n=3, column='c1') :
    return df.sort_values(by=column)[-n:]

print(top(df, n=5))

# apply() : 직접 작성한 함수를 aggregate function으로 사용할 수 있다.
print("apply() : 직접 작성한 함수를 aggregate function으로 사용할 수 있다.",'-'*20)
print(df.groupby('c1', group_keys=True).apply(top))