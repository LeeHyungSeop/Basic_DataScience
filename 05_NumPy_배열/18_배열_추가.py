import numpy as np

a2 = np.arange(1, 10).reshape(3, 3)
print(a2)

b2 = np.arange(10, 19).reshape(3, 3)
print(b2)

# append()
print("append()", '-'*20)
a2b2 = np.append(a2, b2)
print(a2b2) # append는 axis지정이 따로 없으면 1차원 형태로 반환된다.

a2b2 = np.append(a2, b2, axis=0) # axis = 0 -> column으로 append
print(a2b2)

a2b2 = np.append(a2, b2, axis=1) # axis = 1 -> row로 append
print(a2b2)