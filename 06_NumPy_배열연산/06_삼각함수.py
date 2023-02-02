'''
sin, cos, tan
arcsin, arccos, arctan
arctan2
sinh, cosh, tanh
arcsinh, arccosh, arctanh
deg2rad. rad2deg
hypot
'''
import numpy as np

# sin, cos ,tan
print("sin, cos, tan", '-'*20)
t = np.linspace(0, np.pi, 3)
print(t)
print(np.sin(t))
print(np.cos(t))
print(np.tan(t))

# arcsin, arccos, arctan
print("arcsin, arccos, arctan", '-'*20)
x = [-1, 0, 1]
print(x)
print(np.arcsin(x))
print(np.arccos(x))
print(np.arctan(x))