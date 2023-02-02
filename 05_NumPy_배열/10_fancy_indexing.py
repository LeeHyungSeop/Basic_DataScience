import numpy as np

# 1차원 배열에 1차원 fancy indexing
print("1차원 배열에 1차원 fancy indexing", "-"*10)
a1 = np.array([1, 2, 3, 4, 5])
print(a1)
ind = [0, 2]
print(a1[ind])  

# 1차원 배열에 2차원 fancy indexing
print("1차원 배열에 2차원 fancy indexing", "-"*10)
ind = np.array([[0, 1],
                [2, 0]])
print(a1[ind])

# 2차원 배열에 fancy indexing
print("2차원 배열에 fancy indexing", "-"*10)
a2 = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
row = np.array([0, 2])
col = np.array([1, 2])
print("1\n", a2[row, col], end='\n\n') # (0, 1), (2,2)
print("2\n", a2[row, :], end='\n\n') # 0행, 2열만 indexing
print("3\n", a2[:, col], end='\n\n') # 1열, 2열만 indexing
print("4\n", a2[row, 1], end='\n\n') # 0행 1열, 2행 1열 --> [2, 8]
print("5\n", a2[2, col], end='\n\n') # 2행에 1, 2열만 indexing --> [8, 9]
print("6\n", a2[row, 1:], end='\n\n') # 0, 2행에 1열부터 끝열까지 indexing
print("7\n", a2[1:, col], end='\n\n') # 1행부터 끝행에 1, 2열만 indexing