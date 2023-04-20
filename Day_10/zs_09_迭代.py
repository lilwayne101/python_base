import numpy as np

data = np.arange(1, 10).reshape((3, 3))
print(data)
print("-----------------")

for num in np.nditer(data, order='F'):
    print(num)