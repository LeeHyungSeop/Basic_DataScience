import numpy as np

# split() : 배열 분할
print("split() : 배열 분할", '-'*20)
a1 = np.arange(0, 10)
print(a1)

b1, c1 = np.split(a1, [5])
print(b1, c1)

b1, c1, d1, e1, f1 = np.split(a1, [2, 4, 6, 8])
print(b1, c1, d1, e1, f1)

# vsplit() : 수직 분할, 1차원으로 분할
print("vsplit() : 수직 분할, 1차원으로 분할", '-'*20)
a2 = np.arange(1, 10).reshape(3, 3)
print(a2)

b2, c2= np.vsplit(a2, [2])
print(b2)
print(c2)

# hsplit() : 수평 분할, 2차원으로 분할
print("hsplit() : 수평 분할, 1차원으로 분할", '-'*20)
a2 = np.arange(1, 10).reshape(3, 3)
print(a2)

b2, c2= np.hsplit(a2, [2])
print(b2)
print(c2)

# dsplit() : 깊이 분할, 3차원으로 분할 (axis = 2 축 기준으로 분할)
print("dsplit() : 깊이 분할, 3차원으로 분할", '-'*20)
a3 = np.arange(1, 28).reshape(3, 3, 3)
print(a3)

b3, c3 = np.dsplit(a3, [2])
print(b3)
print(c3)