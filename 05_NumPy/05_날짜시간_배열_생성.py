'''
Y : 연
M : 월
W : 주
D : 일
h : 시
m : 분
ms : 밀리초
us : 마이크로초
ns : 나노초
ps : 피코초
fs : 펨토초
as : 아토초
'''

import numpy as np

date = np.array('2023-01-02', dtype=np.datetime64) # datetime64 : 날짜, 시간을 나타내는 data type
print(date)

# datetime64 자료형에 대한 다음 method 사용가능
print(date + np.arange(3))

datetime = np.datetime64("2020-06-01 12:00")
print(datetime) # 2020-06-01T12:00 --> T : 시간 정보도 출력

datetime = np.datetime64("2020-06-01 12:00:12.123123", 'ns')
print(datetime) # 2020-06-01T12:00:12.340000000 --> nano second까지 출력