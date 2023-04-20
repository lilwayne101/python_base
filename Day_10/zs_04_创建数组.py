import numpy as np
import copy

# nums = np.array([1, 2, 3], dtype=np.string_)
# print(nums)
# print(np.dtype)
#
# print(np.array([1, 2, 3, 4, 5, 6], ndmin=3))
# arr = np.array(['python', 'tensorflow', 'scikit-learn', 'numpy'], dtype=np.string_)
# print(arr)

# print(np.array([1, 2, 3], dtype="f4"))
# print(np.array([1.5, 2.2, 3]))
# print(np.array([1, 2, 3, 4], ndmin=3))
# print(np.array([1, 2, 3], dtype=str))
# print(np.array([range(i, i + 5) for i in [1, 2, 3]]))
# print(np.zeros(shape=[5, 5], dtype='i4'))
# print(np.ones(shape=[5, 5], dtype='i4'))
# print(np.array(['1.1', '2.2', '3.3'], dtype='S').astype("f4"))
# arr = np.nonzero(np.array([1, 2, 0, 6, 0, 7]))
# print(arr)

# print(np.full(shape=[5, 5], fill_value=1.5, dtype=np.float))
# print(np.eye(10))
# print(np.empty(shape=[5, 5]))
# print(np.linspace(1, 11, 3))
# print(np.random.random((5, 5)))
# print(np.random.randint(0, 10, (3, 3)))
# print(np.random.normal(0, 2, (3, 3)))
# print(np.array([1, 3, 5, 4, 5, 6]).reshape((6, 1)))
# a = [
#     [1, 2, 3],
#     [4, 5, 6]
# ]
#
# a1 = copy.deepcopy(a)
# a2 = a
# print(id(a))
# print(id(a1))
# print(id(a2))

# nums = [
#     [1, 2, 3],
#     [4, 5, 6]
# ]
#
# a = np.array(nums)
# a1 = np.array(a)
# a2 = np.asarray(a)
#
# a[0][0] = 100
# print(a)
# print(a1)
# print(a2)
