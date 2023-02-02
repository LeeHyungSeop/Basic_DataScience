# Comparison Operators : 비교 연산자
'''
(비교 연산자)
==
!=
<
<=
>
>=

(비교 범용 함수)
isclose() : 배열 두 개가 (z*1e + 02)% 내외로 가까우면 True, 아니면 False
isinf()   : 배열이 inf면 True, 아니면 False
isfinite  : 배열이 inf, nan이면 False, 아니면 True
isnan     : 배열이 nan면 True, 아니면 False
'''

import numpy as np

print("1차원 배열에 비교 연산자 사용", '-'*20)
a1 = np.arange(1, 10)
print(a1)
print(a1 == 5) # a1 배열에서 조건에 맞는 것은 True, 아닌 것은 False
print(a1 != 5)
print(a1 < 5)
print(a1 <= 5)
print(a1 > 5)
print(a1 >= 5)

print("2차원 배열에 비교 연산자 사용", '-'*20)
a2 = np.arange(1, 10).reshape(3, 3)
print(a2)
print(np.sum(a2))
print(np.count_nonzero(a2 > 5))
print(np.sum(a2 > 5)) # 5 초과인 element에 대해서 합
print(np.sum(a2 > 5, axis=0))
print(np.sum(a2 > 5, axis=1),end="\n\n")
print(np.any(a2 > 5)) # 5 초과인 element가 하나라도 있으면 True
print(np.any(a2 > 5, axis=0))
print(np.any(a2 > 5, axis=1),end="\n\n")
print(np.all(a2 > 5)) # 5 초과인 element가 하나라도 없으면 False
print(np.all(a2 > 5, axis=0))
print(np.all(a2 > 5, axis=1))

# 비교 범용 함수, isclose()
print("비교 범용 함수, isclose()", '-'*20)
a1 = np.array([1, 2, 3, 4, 5])
b1 = np.array([1, 2, 3, 5, 4])
print(a1)
print(b1)
print(np.isclose(a1, b1))


a1= np.array([np.nan, 2, np.inf, 4, np.NINF]) # NINF : -inf

print("비교 범용 함수, ", '-'*20)
print(a1)

print("비교 범용 함수, isnan()", '-'*20)
print(np.isnan(a1))

print("비교 범용 함수, isinf()", '-'*20)
print(np.isinf(a1))

print("비교 범용 함수, isfinite()", '-'*20)
print(np.isfinite(a1))

