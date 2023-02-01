import numpy as np

print("\n1차원 배열의 indexing", "-"*20)
a1 = np.array([1, 2, 3, 4, 5])
print(a1)
print(a1[0]) 
print(a1[2])
print(a1[-1]) # 끝에서 첫번째
print(a1[-2]) # 끝에서 두번쨰

print("\n2차원 배열의 indexing", "-"*20)
a2 = np.array([
    [1, 2, 3],
    [1, 2, 3],
    [1, 2, 3]
])
print(a2)
print(a2[0, 0]) # 0행 0열
print(a2[0, 2]) # 0행 2열
print(a2[1, -1]) # 1행 끝에서 1번째 열
print(a2[2, -2]) # 2행 끝에서 2번째 열
print(a2[2]) # 2행

print("\n3차원 배열의 indexing", "-"*20)
a3 = np.array([
    [ [1, 2, 3], [4, 5, 6], [7, 8, 9]  ],
    [ [1, 2, 3], [4, 5, 6], [7, 8, 9]  ],
    [ [1, 2, 3], [4, 5, 6], [7, 8, 9]  ]
])
print(a3)
print(a3[0, 0, 0]) # 0행렬 0행 0열
print(a3[1, 1, 1]) # 1행렬 1행 1열
print(a3[2, 2, 2]) # 2행렬 2행 2열
print(a3[0, -1, -2]) # 0행렬 뒤에서 1번째 행, 뒤에서 2번째 열


