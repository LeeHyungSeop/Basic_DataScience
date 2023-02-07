import numpy as np
import pandas as pd

'''
read_csv        : 기분 구분자 ','
read_table      : 기분 구분자 '\t'
read_fwf        : 구분자 없는 데이터
read_clipboard  : 클립보드에 있는 데이터 읽기. 웹페이지에 있는 표 읽어올 때 유용
read_excel      : 엑셀 파일에서 표 형식 데이터 읽기
read_hdf        : Pandas에서 저장한 HDFS 파일의 데이터 읽기
read_html
read_json
read_msgpack    : 메시지팩 바이너리 포맷으로 인코딩된 pandas 데이터 읽기
read_pickle     : 파이썬 피클 포맷으로 저장된 객체 읽기
read_sas        : SAS 시스템의 사용자 정의 저장 포맷 데이터 읽기
read_sql
read_stata      : Stata 파일에서 데이터 읽기
read_feather    : Feather 바이너리 파일 포맷의 데이터 읽기
'''

# read_csv() : csv 파일 읽기
print("read_csv() : csv 파일 읽기", "-"*20)
print(pd.read_csv('07_Pandas/31_example1.csv'), end='\n\n')

# read_csv(header=None) : csv 파일 읽기
print("read_csv(header=None) : header 정보가 없는 csv 파일 읽기", "-"*20)
print(pd.read_csv('07_Pandas/31_example2.csv', header=None), end='\n\n')

# read_csv(name=[]) : csv 파일 읽기
print("read_csv(names=['a', 'b', 'c', 'd', 'e', 'text']) : column명 부여하기", "-"*20)
print(pd.read_csv('07_Pandas/31_example2.csv', names=['a', 'b', 'c', 'd', 'e', 'text']), end='\n\n')

# read_csv(index_col='text') : csv 파일 읽기
print("read_csv(names=['a', 'b', 'c', 'd', 'e', 'text']) : index_col 부여하기", "-"*20)
print(pd.read_csv('07_Pandas/31_example2.csv', names=['a', 'b', 'c', 'd', 'e', 'text'],index_col='text'), end='\n\n')

# read_csv(skiprows=[]) : 해당 행 skip하여 가져오기
print("read_csv('07_Pandas/31_example4.csv', skiprows=[0, 2])", "-"*20)
print(pd.read_csv('07_Pandas/31_example4.csv', skiprows=[0, 2]), end='\n\n')

# read_csv(nrows=3) : 3개 행만 가져오기
print("read_csv('07_Pandas/31_example6.csv'), nrows=3", "-"*20)
print(pd.read_csv('07_Pandas/31_example6.csv', nrows=3), end='\n\n')

# read_csv() : 누락값이 있는 csv 파일 가져오기
print("read_csv('07_Pandas/31_example5.csv')", "-"*20)
print(pd.read_csv('07_Pandas/31_example5.csv'), end='\n\n')

# to_csv() : csv file로 저장하기
print("to_csv() : csv file로 저장하기", "-"*20)
df = pd.read_csv('07_Pandas/31_example5.csv')
df.to_csv('07_Pandas/31_output.csv')

# date가 포함된 data csv file로 저장하기
print("to_csv() : date가 포함된 data csv file로 저장하기", "-"*20)
dr = pd.date_range('2020-01-01', periods=10)
ts = pd.Series(np.arange(10), index=dr)
print(ts)
ts.to_csv('07_Pandas/31_ts.csv', header=['value'])

# read_table(sep='\s+') 
print("read_table(sep='\s+') : space만 있는 경우, \s+ 를 통해 data를 가져온다", "-"*20)
print(pd.read_table('07_Pandas/31_example3.txt', sep='\s+'), end='\n\n') 

# read_json() : json 파일 가져오기
print("read_json('07_Pandas/31_example.json')", "-"*20)
print(pd.read_json('07_Pandas/31_example.json'), end='\n\n')

# to_json() : date형식 data json file로 저장하기
print("to_json() : json file로 저장하기", "-"*20)
ts.to_json('07_Pandas/31_output_date.json')

# to_json() : DataFrame형식 data json file로 저장하기
print("to_json() : json file로 저장하기", "-"*20)
df.to_json('07_Pandas/31_output_df.json')