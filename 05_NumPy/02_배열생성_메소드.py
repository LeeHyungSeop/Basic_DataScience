import numpy as np

# zeros() : 모든 요소를 0으로 초기화
print("zeros()", "-"*20)
print(np.zeros(10))

# ones() : 모든 요소를 1로 초기화
print("ones()", "-"*20)
print(np.ones(10))
print(np.ones((3, 3)))

# full() : 모든 요소를 지정한 값으로 초기화
print("full()", "-"*20)
print(np.full((3, 3), 1.23)) # 3 by 3 행렬에 1.23으로 초기화

# eye() : Identity Matrix 생성 --> 단위행렬의 특징 : 정사각행렬 & 주대각이 모두 1--> 
print("eye()", "-"*20)
print(np.eye(3))

# tri() : Lower Triangle Matrix 생성
print("tri()", "-"*20)
print(np.tri(3)) 

# empty() : 초기화되지 않은 배열 생성 --> 초기화가 없어서 배열 생성이 매우 빠름.
# 하지만 기존 메모리 위치에 이미 존재하는 값이 있음. 따라서 초기화하지 않았는데도 어떠한 값이 출력된다.
print("empty()", "-"*20)
print(np.empty(10)) 

# _like() : 지정된 배열과 shape가 같은 행렬 생성
print("_like()", "-"*20)
a1 = np.array([1, 2, 3, 4, 5])
print(np.zeros_like(a1)) # a1과 shape이 같은 행렬을 만들되, 0으로 초기화

a2 = np.array([ [1, 2, 3], [4, 5, 6], [7, 8, 9] ])
print(np.ones_like(a2)) # a2과 shape이 같은 행렬을 만들되, 1으로 초기화

a3 = np.array([
    [ [1, 2, 3], [4, 5, 6], [7, 8, 9]  ],
    [ [1, 2, 3], [4, 5, 6], [7, 8, 9]  ],
    [ [1, 2, 3], [4, 5, 6], [7, 8, 9]  ]
])
print(np.full_like(a3, 10)) # a3과 shape이 같은 행렬을 만들되, 10으로 초기화

# arange() : 정수 범위로 배열 생성
print("arange()", "-"*20)
print(np.arange(0, 30, 2)) # 0 ~ 30까지 step : 2 --> 0 2 4 ... 30

#linspace() : 범위 내에서 균등 간격의 배열 생성
print("linspace()", "-"*20)
print(np.linspace(0, 1, 5)) # 0 ~ 1까지 5등분

#logspace() : 범위 내에서 균등 간격으로 로그 스케일로 배열 생성
print("logspace()", "-"*20)
print(np.logspace(0.1, 1, 20)) 














