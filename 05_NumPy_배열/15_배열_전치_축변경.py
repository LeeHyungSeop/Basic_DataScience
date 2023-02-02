import numpy as np

a1 = np.array([1, 2, 3, 4, 5])

# 2차원 배열 Transpose
print("2차원 배열의 전치", '-'*20)
a2 = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
print(a2)
print(a2.T, end="\n\n") # Transpose(전치)

print(a2.swapaxes(1, 0))

# 3차원 배열 Transpose
print("3차원 배열의 전치", '-'*20)
a3 = np.array([
    [ [1, 2, 3], [4, 5, 6], [7, 8, 9]  ],
    [ [1, 2, 3], [4, 5, 6], [7, 8, 9]  ],
    [ [1, 2, 3], [4, 5, 6], [7, 8, 9]  ]
])
print(a3)
print(a3.T, end="\n\n") # Transpose(전치)

# swapaxes() : 축 변경
print("swapaxes", '-'*20)

print(a3.swapaxes(0, 1), end="\n\n") # axes0과 axes1을 swap
print(a3.swapaxes(1, 2), end="\n\n") # axes1과 axes2을 swap