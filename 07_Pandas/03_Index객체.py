import numpy as np
import pandas as pd

idx = pd.Index([2, 4, 6, 8, 10])
print("idx", '-'*20)
print(idx, end='\n\n')

print("idx[1]", '-'*20)
print(idx[1], end='\n\n')

print("idx[1:2:2]", '-'*20)
print(idx[1:2:2], end='\n\n')

print("idx[-1::]", '-'*20)
print(idx[-1::], end='\n\n')

print("idx[::2]", '-'*20)
print([idx[::2]], end='\n\n')


idx1 = pd.Index([1, 2, 4, 6, 8])
idx2 = pd.Index([2, 4, 5, 6, 7])
print(idx1)
print(idx2)

# Index 객체의 다양한 method
print("size",'-'*10)
print(idx1.size, end='\n\n')

print("shape",'-'*10)
print(idx1.shape, end='\n\n')

print("ndim",'-'*10)
print(idx1.ndim, end='\n\n')

print("dtype",'-'*10)
print(idx1.dtype, end='\n\n')

print("append() : ", '-'*10)
print(idx1.append(idx2), end='\n\n')

# 차집합
print("difference() : 차집합", '-'*10) 
print(idx1.difference(idx2), end='\n\n')

# 교집합
print("intersection() : 교집합", '-'*10)
print(idx1.intersection(idx2), end='\n\n')

# 합집합 (중복 허용 X)
print("union() : 합집합(중복 허용 X)", '-'*10)
print(idx1.union(idx2), end='\n\n')

# 여집합
print("symmetric_difference(): 여집합", '-'*10)
print(idx1.symmetric_difference(idx2), end='\n\n')

# 해당 인덱스의 값 삭제
print("delete() : 해당 인덱스의 값 삭제", '-'*10)
print(idx1.delete(0), end='\n\n')

# 해당값 삭제
print("drop() : 해당 값 삭제", '-'*10)
print(idx1.drop(2), end='\n\n')

