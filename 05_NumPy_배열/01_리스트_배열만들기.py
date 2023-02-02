import numpy as np

print(np.__version__)

# 리스트로 배열 만들기

# 1차원 배열 만들기 & 다루기
print("\n1차원 배열 만들기 & 다루기", "-"*20)
a1 = np.array([1, 2, 3, 4, 5])

print(a1)
print(type(a1)) # ndarray : n-dimension array
print(a1.shape) # shape(5,) : 5개의 element들이 있고, 1차원 배열이다.

print(a1[0], a1[1], a1[2], a1[3], a1[4])
a1[0] = 4
a1[1] = 5
a1[2] = 6
print(a1)

# 2차원 배열 만들기 & 다루기
print("\n2차원 배열 만들기 & 다루기", "-"*20)
a2 = np.array([ [1, 2, 3], [4, 5, 6], [7, 8, 9] ])
print(a2)
print(a2.shape) # (3,3) : 3 by 3 
print(a2[0, 0], a2[1, 1], a2[2, 2])

# 3차원 배열 만들기 & 다루기
print("\n3차원 배열 만들기 & 다루기", "-"*20)
a3 = np.array([
    [ [1, 2, 3], [4, 5, 6], [7, 8, 9]  ],
    [ [1, 2, 3], [4, 5, 6], [7, 8, 9]  ],
    [ [1, 2, 3], [4, 5, 6], [7, 8, 9]  ]
])
print(a3)
print(a3.shape) # (3, 3, 3) :  3 by 3 by 3