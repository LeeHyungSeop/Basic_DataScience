'''
boolean operator

& : bitwise_and
| : bitwise_or
^ : bitwise_xor
~ : bitwise_not
'''

import numpy as np

a2 = np.arange(1, 10).reshape(3,3)
print(a2)

print("&", '-'*20)
print((a2 > 5) & (a2 < 8), end="\n\n")
print(a2[(a2 > 5) & (a2 < 8)], end="\n\n")

print("|", '-'*20)
print((a2 > 5) | (a2 < 8), end="\n\n")
print(a2[(a2 > 5) | (a2 < 8)], end="\n\n")

print("^", '-'*20)
print((a2 > 5) ^ (a2 < 8), end="\n\n")
print(a2[(a2 > 5) ^ (a2 < 8)], end="\n\n")

print("~", '-'*20)
print(~(a2 > 5), end="\n\n")
print(a2[~(a2 > 5)], end="\n\n")