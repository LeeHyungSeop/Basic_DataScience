# arithmetic operator : 산술 연산자
# 두개의 2차원 배열에 대한 테스트
import numpy as np

a2 = np.arange(1, 10).reshape(3, 3)
print(a2)
b2 = np.random.randint(1, 10, size=(3, 3))
print(b2)

# add
print("add()" , '-'*20)
print(a2 + b2)

# substract
print("substract()" , '-'*20)
print(a2 - b2)

# negative
print("negative()" , '-'*20)
print(a2 * b2)

# multiply
print("multiply()" , '-'*20)
print(a2 * b2)

# divide
print("divide()" , '-'*20)
print(a2 / b2)

# floor_divide : 나눗셈 내림
print("floor_divide()" , '-'*20)
print(a2 // b2)

# power
print("power()" , '-'*20)
print(a2 ** b2)

# mod
print("mod()" , '-'*20)
print(a2 % b2)