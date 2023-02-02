import numpy as np

a1 = np.random.randint(-10, 10, size=5)
print(a1)

# absolute() : 절대값 반환
print("absolute()" , '-'*20)
print(np.absolute(a1))

# abs() : 절대값 반환(absolute의 준말)
print("abs()" , '-'*20)
print(np.abs(a1))

# square() : 제곱 반환
print("\nsquare()", "-"*20)
print(np.square(a1))

# sqrt() : square root --> 제곱근 반환
print("sqrt()", "-"*20)
print(np.sqrt(a1))

# exp() : exponential == 지수 함수
print("\nexp()", "-"*20)
print(np.exp(a1))

# exp2() == power() 
print("exp2()", "-"*20)
print(np.exp2(a1)) # a1 ** 2
print(np.power(a1, 2)) # a1 ** 2
print(a1 ** 2)

a1 = np.random.randint(1, 10, size=5)
print('\n', a1)
# log() : 로그 함수
print("\nlog()", "-"*20)
print(np.log(a1))

# log2() : 로그 함수
print("log2()", "-"*20)
print(np.log2(a1))

# log10() : 로그 함수
print("log10()", "-"*20)
print(np.log10(a1))