import numpy as np


print("1차원 배열의 Boolean Indexing", "-"*20)
a1 = np.array([1, 2, 3, 4, 5])
print(a1)
bi = [True, False, True, False, True]
print(a1[bi]) # a1의 bi에서 True인 index만 출력


print("2차원 배열의 Boolean Indexing", "-"*20)
a2 = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
bi = np.random.randint(0, 2, a2.shape, dtype=bool) # 랜덤하게 3*3 배열을 만듦
print(bi)
print(a2[bi])