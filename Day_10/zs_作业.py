import copy
import numpy as np
"""
    2.自定义User类添加到列表UserList中，使用代码进行演示copy()和deepcopy() 区别
"""


# class User:
#     pass
#
#
# user = User()
# userList = ['jack', 'bob', ['jack']]
# userCopy = copy.copy(userList)
# userDeepCopy = copy.deepcopy(userList)
# userList[2].append(user)
# print(userCopy)
# print(userDeepCopy)

"""
3. arr_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]]) 转为一维数组
"""

arr_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
arrTemp = arr_3d[1]
arr_3d = np.delete(arr_3d, 1, axis=2)
# np.append(arr_3d[0], arr_3d[1])
print(arr_3d)