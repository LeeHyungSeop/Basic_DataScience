import numpy as np
import pandas as pd

s = pd.Series(np.random.randint(-10, 10, size=(10)))

# rank() : rank 순위 출력
print("rank() : rank 순위 출력", '-'*20)
print(s, end='\n\n')
print(s.rank())

# rank(method='first') : 동일한 값이 있을 때, 먼저 나오는 숫자가 rank가 높도록( (9.5, 9.5)X / (9 10)O)
print("rank(method='first') : rank 순위 출력", '-'*20)
print(s, end='\n\n')
print(s.rank(method='first'))

# rank(method='max') : 같은 값을 가지는 그룹을 같은 랭킹으로 (랭킹이 가장 높은 두 숫자가 있는 경우, 1.0이 사라지고 2.0, 2.0이 된다)
print("rank(method='max') : rank 순위 출력", '-'*20)
print(s, end='\n\n')
print(s.rank(method='max'))
