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
print(pd.read_csv('07_Pandas/31_example1.csv'))

# read_csv(header=None) : csv 파일 읽기
print("read_csv(header=None) : header 정보가 없는 csv 파일 읽기", "-"*20)
print(pd.read_csv('07_Pandas/31_example2.csv', header=None))
