import numpy as np

# 1차원 배열에 대한 값 수정
print("1차원 배열에 대한 값 수정", "-"*20)
a1 = np.array([1, 2, 3, 4, 5])
a1[0] = 0
a1[1] = 1
a1[2] = 2
print(a1)

a1[:1] = 9
print(a1)

i = np.array([1, 3, 4])
a1[i] = 0
print(a1)

a1[i] += 4
print(a1)

# 2차원 배열에 대한 값 수정
print("2차원 배열에 대한 값 수정", "-"*20)
a2 = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
print(a2, end="\n\n")

a2[0, 0] = 1
a2[1, 1] = 2
a2[2, 2] = 3
print(a2, end="\n\n")

a2[0] = 1
print(a2, end="\n\n")

a2[1:, 2] = 9
print(a2, end="\n\n")

row = np.array([0, 1])
col = np.array([1, 2])
a2[row, col] = 0
print(a2, end="\n\n")