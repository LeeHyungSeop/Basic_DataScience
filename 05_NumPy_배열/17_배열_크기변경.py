import numpy as np

n2 = np.random.randint(0, 10, (2, 5))
print(n2)

# 똑같은 size로 resize() 
print("똑같은 size로 resize()", '-'*20)
n2.resize((5, 2))
print(n2)

# 더 큰 size로 resize() : 추가 공간 zero padding
print("더 큰 size로 resize() : 추가 공간 zero padding", '-'*20)
n2.resize((5, 5)) # 나머지는 모두 Zero Padding
print(n2)

# 더 작은 size로 resize() : 잘린 공간은 삭제
print("더 작은 size로 resize() : 잘린 공간은 삭제", '-'*20)
n2.resize((3, 3))
print(n2) # 원래 10개의 size였는데 9개로 줄이니까 1개의 element가 삭제됨