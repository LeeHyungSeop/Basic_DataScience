# aggregate function : 집계 함수
'''
(함수)           (NaN 안전 모드)   (설명)

sum             nansum          - 합
cumsum          nancumsum       - 누적 합
diff                            - 차분
prod            nanprd          - 곱 계산
cumprod         nancumprod      - 누적 곱
dot                             - 점 곱
matmul                          - 행렬 곱
tensordot                       - 텐서곱
cross                           - 벡터곱
inner                           - 내적
outer                           - 외적
mean            nanmean         - 평균
std             nanstd          - 표준 편차
var             nanvar          - 분산
min             nanmin          - 최소값
max             nanmax          - 최대값
argmin          nanargmin       - 최소값 인덱스
argmax          nanargmax       - 최대값 인덱스
median          nanmedian       - 중앙값
percentile      nanpercentile   - 순위 기반 백분위 계산
any                             - 요수 중 참이 있는지
all                             - 모든 요소가 참인지
'''

import numpy as np

# sum
print("sum", '-'*20)
a2 = np.random.randint(1, 10, size=(3, 3))
print(a2)
print(a2.sum(), np.sum(a2))
print(a2.sum(axis=0), np.sum(a2, axis=0)) # axis = 0 축을 기준으로 sum 
print(a2.sum(axis=1), np.sum(a2, axis=1)) # axis = 1 축을 기준으로 sum

# cumsum() : 누적합 --> 합 과정을 누적하여 출력해줌
print("cumsum", '-'*20)
print(a2, end="\n\n")
print(np.cumsum(a2), end="\n\n")
print(np.cumsum(a2, axis=0), end="\n\n") # axis = 0 축을 기준으로 cumsum 
print(np.cumsum(a2, axis=1), end="\n\n") # axis = 1 축을 기준으로 cumsum

# diff() : 차분 
print("diff", '-'*20)
print(a2, end="\n\n")
print(np.diff(a2), end="\n\n")
print(np.diff(a2, axis=0), end="\n\n") # axis = 0 축을 기준으로 diff 
print(np.diff(a2, axis=1), end="\n\n") # axis = 1 축을 기준으로 diff

# prod() : 차분 
print("prod", '-'*20)
print(a2, end="\n\n")
print(np.prod(a2), end="\n\n")
print(np.prod(a2, axis=0), end="\n\n") # axis = 0 축을 기준으로 prod 
print(np.prod(a2, axis=1), end="\n\n") # axis = 1 축을 기준으로 prod

# cumprod() : 차분 
print("cumprod", '-'*20)
print(a2, end="\n\n")
print(np.cumprod(a2), end="\n\n")
print(np.cumprod(a2, axis=0), end="\n\n") # axis = 0 축을 기준으로 cumprod 
print(np.cumprod(a2, axis=1), end="\n\n") # axis = 1 축을 기준으로 cumprod

# dot() / matmul() : 점곱 / 행렬곱 계산
print("dot() / matmul()", '-'*20)
print(a2)
b2 = np.ones_like(a2)
print(b2, end="\n\n")
print(np.dot(a2, b2), end="\n\n")
print(np.matmul(a2, b2), end="\n\n")

# tensordot() : 텐서곱 계산
print("tensordot()", '-'*20)
print(a2)
b2 = np.ones_like(a2)
print(b2, end="\n\n")
print(np.tensordot(a2, b2), end="\n\n")
print(np.tensordot(a2, b2, axes = 0), end="\n\n")
print(np.tensordot(a2, b2, axes = 1), end="\n\n") # dot()과 같은 결과

# cross() : 벡터곱
print("cross()", '-'*20)
x = [1, 2, 3]
y = [4, 5, 6]
print(np.cross(x, y)) # [12-15, -(6-12), 5-8]

# inner()/outer() : 내적/외적
print("inner()/outer()", '-'*20)
print(a2)
print(b2)
print(np.inner(a2 , b2), end='\n\n')
print(np.outer(a2 , b2), end='\n\n')

# mean() : 평균
print("mean", '-'*20)
print(a2)
print(np.mean(a2), end='\n\n')
print(np.mean(a2, axis=0), end='\n\n')
print(np.mean(a2, axis=1), end='\n\n')

# std() : 표준 편차
print("std", '-'*20)
print(a2)
print(np.std(a2), end='\n\n')
print(np.std(a2, axis=0), end='\n\n')
print(np.std(a2, axis=1), end='\n\n')

# var() : 분산
print("var", '-'*20)
print(a2)
print(np.var(a2), end='\n\n')
print(np.var(a2, axis=0), end='\n\n')
print(np.var(a2, axis=1), end='\n\n')

# min() : 최소값
print("min", '-'*20)
print(a2)
print(np.min(a2), end='\n\n')
print(np.min(a2, axis=0), end='\n\n')
print(np.min(a2, axis=1), end='\n\n')

# max() : 최대값
print("max", '-'*20)
print(a2)
print(np.max(a2), end='\n\n')
print(np.max(a2, axis=0), end='\n\n')
print(np.max(a2, axis=1), end='\n\n')

# argmin() : 최소값 인덱스
print("argmin", '-'*20)
print(a2)
print(np.argmin(a2), end='\n\n')
print(np.argmin(a2, axis=0), end='\n\n')
print(np.argmin(a2, axis=1), end='\n\n')

# argmax() : 최대값 인덱스
print("argmax", '-'*20)
print(a2)
print(np.argmax(a2), end='\n\n')
print(np.argmax(a2, axis=0), end='\n\n')
print(np.argmax(a2, axis=1), end='\n\n')

# median() : 중앙값
print("median", '-'*20)
print(a2)
print(np.median(a2), end='\n\n')
print(np.median(a2, axis=0), end='\n\n')
print(np.median(a2, axis=1), end='\n\n')

# percentile() : 백분위 수
print("percentile()", '-'*20)
a1 = np.array([0, 1, 2, 3])
print(a1)
print(np.percentile(a1, [0, 20, 40, 60, 80, 100], interpolation='linear'))
print(np.percentile(a1, [0, 20, 40, 60, 80, 100], interpolation='higher'))
print(np.percentile(a1, [0, 20, 40, 60, 80, 100], interpolation='lower'))
print(np.percentile(a1, [0, 20, 40, 60, 80, 100], interpolation='nearest'))
print(np.percentile(a1, [0, 20, 40, 60, 80, 100], interpolation='midpoint'))

# any() : 하나라도 True면 True
print("any()", '-'*20)
a2 = np.array([
    [False, False, False],
    [True, True, True],
    [False, False, True]
])
print(a2)
print(np.any(a2))
print(np.any(a2, axis=0))
print(np.any(a2, axis=1))

# all() : 모든것이 True여야 True
print("all()", '-'*20)
a2 = np.array([
    [False, False, True],
    [True, True, True],
    [False, False, True]
])
print(a2)
print(np.all(a2))
print(np.all(a2, axis=0))
print(np.all(a2, axis=1))

