

import numpy as np

print("1차원 배열의 partition", "-"*10)
a1 = np.random.randint(1, 10, size=10)
print(a1)
print(np.partition(a1, 2)) # a1에서 작은 값 3개만 정렬


print("2차원 배열의 partition", "-"*10)
a2 = np.random.randint(1, 10, size=(5, 5))
print(np.partition(a2, 3), end="\n\n")
print(np.partition(a2, 3, axis=0), end="\n\n")
print(np.partition(a2, 3, axis=1), end="\n\n")