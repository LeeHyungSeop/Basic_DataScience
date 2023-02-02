import numpy as np

'''
a[start : stop : step]
default -> start = 0, stop = ndim, step = 1
'''

print("\n1차원 배열의 slicing", "-"*20)
a1 = np.array([1, 2, 3, 4, 5])
print(a1)
print(a1[0 : 2])
print(a1[0 : ])
print(a1[: 1])
print(a1[::2])
print(a1[::-1]) # step이 음수면 역으로 접근 -> 5 4 3 2 1
print(a1[::-2]) 

print("\n2차원 배열의 indexing", "-"*20)
a2 = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
print(a2, end="\n\n")
print(a2[1], end="\n\n")
print(a2[1, :], end="\n\n")
print(a2[:2, :2], end="\n\n")
print(a2[1:, ::-1], end="\n\n")
print(a2[::-1, ::-1], end="\n\n")

