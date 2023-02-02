# 하나의 1차원 배열에 대한 테스트
# arithmetic operator : 산술 연산자
import numpy as np

a1 = np.arange(1, 10)
print(a1)

# add
print("add()" , '-'*20)
print(a1 + 1)
print(np.add(a1, 1))

# substract
print("substract()" , '-'*20)
print(a1 - 1)
print(np.subtract(a1, 1))

# negative
print("negative()" , '-'*20)
print(-a1)
print(np.negative(a1))

# multiply
print("multiply()" , '-'*20)
print(a1 * 2)
print(np.multiply(a1, 2))

# divide
print("divide()" , '-'*20)
print(a1 / 2)
print(np.divide(a1, 2))

# floor_divide : 나눗셈 내림
print("floor_divide()" , '-'*20)
print(a1 // 2)
print(np.floor_divide(a1, 2))

# power
print("power()" , '-'*20)
print(a1 ** 2)
print(np.power(a1, 2))

# mod
print("mod()" , '-'*20)
print(a1 % 2)
print(np.mod(a1, 2))