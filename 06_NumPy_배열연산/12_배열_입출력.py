'''
save()    : NumPy 배열 객체 1개를 파일에 저장    --> 파일종류 : 바이너리
savez()   : NumPy 배열 객체 여러개를 파일에 저장  --> 파일종류 : 바이너리
load()    : NumPy 배열 저장 파일로부터 개개체 로딩 --> 파일종류 : 바이너리
savetxt() : 텍스트 파일에 NumPy 배열 객체 저장    --> 파일종류 : 텍스트
loadtxt() : 텍스트 파일로부터 배열 로딩           --> 파일종류 : 텍스트
'''

import numpy as np

a2 = np.random.randint(1, 10, size=(5, 5))
print(a2)
b2 = np.random.randint(1, 10, size=(5, 5))
print(b2)

# save()
print("save()", "-"*20)
np.save("./06_NumPy_배열연산/a", a2) # a2 객체를 ./06_NumPy_배열연산/a 에 저장

# savez() 
print("savez()", "-"*20)
np.savez("./06_NumPy_배열연산/ab", a2, b2) # a2, b2 객체를 ./06_NumPy_배열연산/ab 에 저장

# load()
print("load()", "-"*20)
npy = np.load("./06_NumPy_배열연산/a.npy")
print(npy)

npz = np.load("./06_NumPy_배열연산/ab.npz")
print(npz.files)
print(npz['arr_0'])
print(npz['arr_1'])

# savetxt()
# txt파일로 저장할 때, 특정 구분자에 의해서 저장한다. --> 대표적으로 Comma Seperated Value(csv)
print("savetxt()", "-"*20)
print(a2)
np.savetxt("06_NumPy_배열연산/a.csv", a2, delimiter=',') 

# loadtxt()
print("loadtxt()", "-"*20)
csv = np.loadtxt("06_NumPy_배열연산/a.csv", delimiter=',') # 구분자를 ,로 지정했으니까 ,로 불러와야 한다.
print(csv)

# savetxt() 여러 옵션 전달
print("savetxt(fmt, headers)", "-"*20)
print(b2)
# fmt : 소숫점 2자리까지만 나타내라 / headers: header정보 == column명을 'c1, c2, c3, c4, c5' 라고 해라.
np.savetxt("06_NumPy_배열연산/b.csv", b2, delimiter=',', fmt='%.2e', header='c1, c2, c3, c4, c5') 

csv = np.loadtxt("06_NumPy_배열연산/b.csv", delimiter=',')
print(csv)