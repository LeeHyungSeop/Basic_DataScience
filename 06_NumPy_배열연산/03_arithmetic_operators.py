# 두개의 1차원 배열에 대한 테스트
# arithmetic operator : 산술 연산자
import numpy as np

a1 = np.arange(1, 10)
print(a1)
b1 = np.random.randint(1, 10, size=9)
print(b1)

# add
print("add()" , '-'*20)
print(a1 + b1)

# substract
print("substract()" , '-'*20)
print(a1 - b1)

# negative
print("negative()" , '-'*20)
print(a1 * b1)

# multiply
print("multiply()" , '-'*20)
print(a1 * b1)

# divide
print("divide()" , '-'*20)
print(a1 / b1)

# floor_divide : 나눗셈 내림
print("floor_divide()" , '-'*20)
print(a1 // b1)

# power
print("power()" , '-'*20)
print(a1 ** b1)

# mod
print("mod()" , '-'*20)
print(a1 % b1)