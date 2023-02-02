import numpy as np

# concatenate() : 튜플이나 배열의 리스트를 인수로 사용해 배열 연결
print("1차원 배열의 concatenate()", '-'*20)
a1 = np.array([1, 3, 5])
b1 = np.array([2, 4, 6])
c1 = np.array([7, 8, 9])

print(np.concatenate([a1, b1, c1]))

print("2차원 배열의 concatenate()", '-'*20)
a2 = np.array([[1, 2, 3], 
               [4, 5, 6]])

print(np.concatenate([a2, a2]))
print(np.concatenate([a2, a2], axis = 0)) # default는 axis = 0로 concatenate
print(np.concatenate([a2, a2], axis = 1)) 

# vstack() : vertical stack, 1차원으로 연결
print("vstack() : vertical stack, 1차원으로 연결", '-'*20)
print(np.vstack([a2, a2]))

# hstack() : horizontal stack, 2차원으로 연결
print("hstack() : horizontal stack, 2차원으로 연결", '-'*20)
print(np.hstack([a2, a2]))

# dstack() : depth stack, 3차원으로 연결
print("dstack() : depth stack, 3차원으로 연결", '-'*20)
print(np.dstack([a2, a2]))

# stack() : 차원 하나 증가하여 연결 (2차원 -> 3차원)
print("stack() : 차원 하나 증가하여 연결(2차원이라면 3차원으로)", '-'*20)
a2 = np.array([[1, 2, 3], 
               [4, 5, 6]])
print(np.stack([a2, a2]))
