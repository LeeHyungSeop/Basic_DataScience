import numpy as np

def array_info(array) :
    print(array)
    print("ndim : ", array.ndim)
    print("shape: ", array.shape)
    print("dtype: ", array.dtype)
    print("size: ", array.size)
    print("itemsize: ", array.itemsize) # 하나의 element의 size --> int64 dtype을 가지니까 --> 8이 출력
    print("nbytes: ", array.nbytes) # 행렬의 크기 : 8bytes가 5개 있으니까 --> 40 출력
    print("strides: ", array.strides) # 다음 element로 넘어가기 위한 사이즈
                                      # 1차원 배열의 경우, (element 하나의 사이즈)
                                      # 2차원 배열의 경우, (행 하나의 사이즈, element 하나의 사이즈)
                                      # 3차원 배열의 경우, (행*열 하나의 사이즈, 행 하나의 사이즈, element 하나의 사이즈)

print("\n1차원 배열의 정보","-"*20)
a1 = np.array([1, 2, 3, 4, 5])
array_info(a1)

print("\n2차원 배열의 정보","-"*20)
a2 = np.array([
    [1, 2, 3],
    [1, 2, 3],
    [1, 2, 3]
])
array_info(a2)

print("\n3차원 배열의 정보","-"*20)
a3 = np.array([
    [ [1, 2, 3], [4, 5, 6], [7, 8, 9]  ],
    [ [1, 2, 3], [4, 5, 6], [7, 8, 9]  ],
    [ [1, 2, 3], [4, 5, 6], [7, 8, 9]  ]
])
array_info(a3)