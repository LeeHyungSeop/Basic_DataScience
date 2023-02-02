import numpy as np

print("1",'-'*20)
a1 = np.array([1, 2, 3])
print(a1)
print(a1 + 5)

print("2",'-'*20)
a2 = np.arange(1, 10).reshape(3, 3)
print(a2)
print(a1 + a2)

print("3",'-'*20)
a3 = np.array([1, 2, 3]).reshape(3, 1)
b3 = a3.T
print(a3)
print(a3 + b3)