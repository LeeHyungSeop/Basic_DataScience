import numpy as np

# reshpae() : 배열의 shape을 변경
print("reshape()",'-'*20)
n1 = np.arange(1, 10)

print(n1)
print(n1.reshape(3,3)) # 1차원이었던 n1을 3*3으로 만들어라

# newaxis() : 새로운 축 추가
print("newaxis()",'-'*20)
print(n1)
print(n1[np.newaxis, :5]) # row쪽으로 추가하면 n1의 [:5]부분이 slicing되어 row로 만들어짐
print(n1[:5, np.newaxis]) # column쪽으로 추가하면 n1의 [:5]부분이 slicing되어 column으로 만들어짐
