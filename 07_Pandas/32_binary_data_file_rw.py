import numpy as np
import pandas as pd

print("df", "-"*20)
df = pd.read_csv('./07_Pandas/31_example1.csv')
print(df, end='\n\n')

print("read_pickle()", "-"*20)
df.to_pickle('07_Pandas/32_df_pickle')
print(pd.read_pickle('07_Pandas/32_df_pickle'), end='\n\n')


print("new df", "-"*20)
df = pd.DataFrame({
    'a' : np.random.randn(100), 
    'b' : np.random.randn(100), 
    'c' : np.random.randn(100)
})
print(df, end='\n\n')

# excel 파일로 저장하기
print('excel 파일 읽기/쓰기', "-"*20)
df.to_excel('07_Pandas/32_example.xlsx', 'Sheet1') # 쓰기
print(pd.read_excel('07_Pandas/32_example.xlsx', 'Sheet1')) # 읽기