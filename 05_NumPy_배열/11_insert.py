import numpy as np

# insert() : 배열의 특치에 값 삽입
# axis를 지정하지 않으면 1차원 배열로 반환
# 추가할 방향을 axis로 지정
# 원본 배열 변경 없이 새로운 배열 반환

# 1차원 배열에 삽입
print("1차원 배열에 삽입", "-"*20)
a1 = np.array([1, 2, 3, 4, 5])
print(a1)

b1 = np.insert(a1, 0, 10) # a1[0] = 10
print(b1)
print(a1) # 원본은 변경되지 않는다.

c1 = np.insert(a1, 2, 10)
print(c1)

# 2차원 배열에 삽입 (2차원 배열이니까 axis = 0, 1 속성 지정 가능)
print("2차원 배열에 삽입", "-"*20)
a2 = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
print(a2)
b2 = np.insert(a2, 1, 10, axis=0) 
print(b2)

c2 = np.insert(a2, 1, 10, axis=1)
print(c2)