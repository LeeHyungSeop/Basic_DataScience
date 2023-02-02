'''
bool_
int_ : 기본 integer type
intc : C언어에서 사용되는 int와 동일(일반적으로 int32 또는 int64)
intp : C언어에서 사용되는 ssize_t와 동일, 일반적으로 int32 또는 int64

int8
int16
int32
int64

uint8
uint16
uint32
uint64

float16
float32
float64
float_ : float64를 줄여서 표현

complex64 : 복소수(Complex Number), 두 개의 32비트 부동 소수점으로 표현
complex128 : 복소수, 두 개의 64비트 부동 소수점으로 표현
complex_ : complex128을 줄여서 표현
'''

import numpy as np


print(np.zeros(20, dtype=int))
print(np.ones(20, dtype=bool))
print(np.full((3, 3), 1.0, dtype=float))