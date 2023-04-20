import numpy as np

nums = np.arange(0, 60)
# print(nums)
# print(nums.shape)
# nums = nums.reshape(2, 5)
# print(nums.shape)
# print(nums)

# nums = nums.reshape(5, -1)
# print(nums.shape)
# print(nums)

# nums = nums.reshape(3, 4, -1)
# print(nums.shape)
# print(nums)
# print(nums.dtype)
# print(nums.nbytes)

# print(np.arange(0, 10, 2).reshape(1, 1, -1))
# print(nums.size * nums.itemsize)
print(np.arange(8).reshape(2, -1))
print(np.arange(8).reshape(2, 2, -1))
print(np.nbytes)

nums.bool()