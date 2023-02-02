import numpy as np

# 리스트 자료형과 달리 "배열의 슬라이스는 복사본이 아니라 원본"이다
print("리스트 자료형과 달리 '배열의 슬라이스는 복사본이 아니라 원본'이다" , "-" * 10)
a2 = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
print(a2, end='\n\n')

print(a2[:2, :2], end='\n\n')
a2_sub = a2[:2, :2]
print(a2_sub, end='\n\n')

a2_sub[:, 1] = 0
print(a2_sub, end='\n\n')
print(a2) # 원본 배열도 0으로 바뀌었다.

# copy() : 배열이나 하위 배열 내의 값을 명시적으로 복사
print("copy() : 배열이나 하위 배열 내의 값을 명시적으로 복사" , "-" * 10)
a2 = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
print(a2, end='\n\n')

a2_sub_copy = a2[:2, :2].copy()   # 원본 내용이 슬라이싱되지 않도록, copy를 붙여준다
print(a2_sub_copy, end='\n\n')

a2_sub_copy[:, 1] = 0
print(a2_sub_copy, end='\n\n')
print(a2) # .copy()를 통해 복사본의 값을 변경하였기 때문에, 원본인 a2의 값은 바뀌지 않았다.