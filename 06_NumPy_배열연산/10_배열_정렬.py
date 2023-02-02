import numpy as np

a1 = np.random.randint(1, 10, size=10)
print(a1)

# np.sort() : 원본 배열은 정렬되지 않는다.
print("np.sort(a1)", '-'*20)
print(np.sort(a1))
print(a1) # 원본 배열은 정렬되지 않는다

# argsort() : 정렬되는 index 위치값 출력
print("np.argsort(a1)", '-'*20)
print(np.argsort(a1))
print(a1) # 원본 배열은 정렬되지 않는다

# a1.sort() : 원본 배열이 정렬
print("a1.sort()", '-'*20)
print(a1.sort()) # return되늰 것이 없기 때문에 None 출력
print(a1) # 원본 배열이 정렬된다.


a2 = np.random.randint(1, 10, size=(3, 3))
print(a2)
# np.sort() : 원본 배열은 정렬되지 않는다.
print("np.sort(a2)", '-'*20)
print(np.sort(a2))
print(np.sort(a2, axis=0))
print(np.sort(a2, axis=1))
print(a2) # 원본 배열은 정렬되지 않는다

# argsort() : 정렬되는 index 위치값 출력
print("np.argsort(a2)", '-'*20)
print(np.argsort(a2))
print(a2) # 원본 배열은 정렬되지 않는다

# a2.sort() : 원본 배열이 정렬
print("a2.sort()", '-'*20)
print(a2.sort()) # return되늰 것이 없기 때문에 None 출력
print(a2) # 원본 배열이 정렬된다.

