import numpy as np

# delete() : 배열의 특정 위치에 값 삭제
# axis를 지정하지 않으면 1차원 배열로 반환
# 삭제할 방향을 axis로 지정
# 원본 배열 변경 없이 새로운 배열 반환

# 1차원 배열의 값 삭제
print("1차원 배열의 값 삭제", "-"*20)
a1 = np.array([1, 2, 3, 4, 5])
b1 = np.delete(a1, 1)
print(b1)
print(a1)

# 2차원 배열의 값 삭제 (2차원 배열이니까 axis = 0, 1 속성 지정 가능)
print("2차원 배열의 값 삭제", "-"*20)
a2 = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
print(a2, end = "\n\n")
b2 = np.delete(a2, 1, axis=0)
print(b2, end = "\n\n")
c2 = np.delete(a2, 1, axis=1)
print(c2, end = "\n\n")