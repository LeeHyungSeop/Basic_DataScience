# 랜덤값으로 배열 생성
'''
seed
permutation
shuffle
random
rand
randint
randn
binomial
normal
beta
chisquare
gamma
uniform
'''

import numpy as np

# random.random() : 랜덤한 수의 배열 생성
print("random.random()", "-"*20)
print(np.random.random((3, 3))) # 3 * 3 shape 행렬을 만들되, 랜덤한 값으로

# random.randint() : 일정 구간의 랜덤 정수의 배열 생성
print("random.randint()", "-"*20)
print(np.random.randint(0, 10, (3, 3)))  # 0~9의 값을 가지는 랜덤값으로, 3 * 3 행렬을 만들어라

# random.normal() : 정규분포(normal distribution)을 고려한 랜덤한 수의 배열 생성
print("random.normal()", "-"*20)
print(np.random.normal(0, 1, (3, 3))) # 평균 = 0, 표준편차 = 1인 3*3 Matrix를 만들어라

# random.rand() : 균등분포(uniform distribution)을 고려한 랜덤한 수의 배열 생성
print("random.rand()", "-"*20)
print(np.random.rand(3, 3))

# random.randn() : 표준 정규 분포(Standard normal distribute)를 고려한 랜덤한 수의 배열
# 표준 정규 분포 : 정규분포에서 평균이 0, 분산이 1인 경우
print("random.randn()", "-"*20)
print(np.random.randn(3, 3))
