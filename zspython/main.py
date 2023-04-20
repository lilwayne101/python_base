import numpy as np
# a = np.array([1,2,3,4,5])
# print(a)
# b = np.zeros((2,3))
# print(b)
# c = np.arange(10)
# print(c)
# d = np.arange(2,10,dtype=float)
# print(d)
# e = np.linspace(1.0,4.0,6)
# print(e)
# f = np.indices((3,3))
# print(f)

# a = np.array([1, 2, 2])
# print(np.argmax(a))

# print(np.hstack(([1, 2, 3], [4, 5, 6])))
# print(np.vstack(([1, 2, 3], [4, 5, 6])))

a = np.arange(1, 10, dtype=np.int8).reshape(3, 3)
b = np.array([1, 1, 1])
print(a)
print(b)
print(np.add(a, b)) # 广播机制
print(np.subtract(a, b))