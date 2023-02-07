import numpy as np
import pandas as pd

s1 = pd.Series(['a', 'b'], index=[1, 2])
s2 = pd.Series(['c', 'd'], index=[1, 2])

print(pd.concat([s1, s2]))

# DataFrame 만드는 함수
def create_df(cols, idx) :
    data = {c: [str(c.lower()) + str(i) for i in idx] for c in cols}
    return pd.DataFrame(data, idx)


df1 = create_df('AB', [1, 2])
print(df1)
df2 = create_df('AB', [3, 4])
print(df2)
df3 = create_df('AB', [0, 1])
print(df3)
df4 = create_df('CD', [0, 1])
print(df4, end='\n\n')

print(pd.concat([df1, df2]), end='\n\n')
print(pd.concat([df3, df4]), end='\n\n') # 누락값은 NaN으로 채워짐
# pd.concat([], axis=1) : axis=1 축으로 결합
print("pd.concat([], axis=1) : axis=1 축으로 결합", "-"*20)
print(pd.concat([df3, df4], axis=1), end='\n\n') 

# pd.concat(verify_integrity=True) : 결합할 때, AB와 (1,2), (0,1)이 충돌하니까 에러를 호출할 수 있도록 세팅
print("pd.concat(verify_integrity=True) : 결합할 때, AB와 (1,2), (0,1)이 충돌하니까 에러를 호출할 수 있도록 세팅")
print(pd.concat([df1, df3]), end='\n\n')
# print(pd.concat([df1, df3], verify_integrity=True))

# pd.concat(ignore_index=True) : 결합할 때, AB와 (1,2), (0,1)이 충돌이 나도 강제로 합친다
print("pd.concat(ignore_index=True) : 결합할 때, AB와 (1,2), (0,1)이 충돌이 나도 강제로 합친다")
print(pd.concat([df1, df3], ignore_index=True), end='\n\n')

# pd.concat(keys=['X', 'Y']) : 결합할 때, 새로운 key를 부여하여 multi index 구조처럼 합칠 수 있다.
print("pd.concat(keys=['X', 'Y']) : 결합할 때, AB와 (1,2), (0,1)이 충돌이 나도 강제로 합친다")
print(pd.concat([df1, df3], keys=['X', 'Y']), end='\n\n')

df5 = create_df('ABC', [1, 2])
df6 = create_df('BCD', [3, 4])
print(pd.concat([df5, df6]))

# pd.concat(join='inner') : 결합할 때, 중복되는 부분의(B, C) data만 inner join
print("pd.concat(join='inner') : 결합할 때, 중복되는 부분의(B, C) data만 inner join", '-'*20)
print(pd.concat([df5, df6], join='inner'))

