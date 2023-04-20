import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
"""
3.arr_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]]) 转为一维数组
"""
# 方法1：
# arr_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
# arr = arr_3d.flatten()
# print(arr)
# 方法2：
# arr_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
# arr = arr_3d.reshape((-1,))
# print(arr)
# 方法3
# arr_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
# # print(arr_3d.size)
# new_arr_3d = np.zeros(arr_3d.size, dtype=int)
# print(new_arr_3d)
# tuple_arr = arr_3d.shape
# # print(tuple_arr)
# num = 0
# for oneDim in range(tuple_arr[0]):
#     # arr_3d[oneDim, ]
#     for secDim in range(tuple_arr[1]):
#         for thirdDim in range(tuple_arr[2]):
#             new_arr_3d[num] = arr_3d[oneDim, secDim, thirdDim]
#             num += 1
#             # np.concatenate([new_arr_3d, arr_3d[oneDim, secDim, :]], axis=1)
#             print(arr_3d[oneDim, secDim, thirdDim])
# print(new_arr_3d)

"""
#使用代码完成下面的二维数组，边界值为1，其余值为0 
[   [1. 1. 1. 1. 1.] 
    [1. 0. 0. 0. 1.] 
    [1. 0. 0. 0. 1.] 
    [1. 0. 0. 0. 1.] 
    [1. 1. 1. 1. 1.]
]
"""
# arr = np.ones((5, 5))
# arr[1:4, 1:4] = 0
# print(arr)

"""
5. 观察下列数组使用代码完成
最后得到的数组： 
[[ 1 4 255 5]
[ 5 255 255 255]
[ 9 10 255 255]]
"""
a = np.array([[1, 4, 2, 5],
              [5, 6, 7, 8],
              [9, 10, 12, 13]
])
# (3, 4)
c = np.array([[8, 7, 255, 6],
              [5, 255, 255, 255],
              [3, 5, 255, 255]
])
# shapeTemp = a.shape
# # b = np.maximum(a, c)
# # print(b)
# b = np.empty(shape=shapeTemp, dtype=np.int32)
# for x in range(shapeTemp[0]):
#     for y in range(shapeTemp[1]):
#         if c[x, y] == 255:
#             a[x, y] = 255
# print(a)
# 方法2:找索引
# idx = np.where(c==255)
# a[idx] = 255
# print(idx)
# print(a)

# data = np.where(c == 255, c, a)
# print(data)
"""
6. 如现在四个同学对球球、冷檬、蘑菇头 三人舞蹈进行打分的一个数据（总分为10），每个同学分
别从三个角度打分：
item = np.array([ [3,5,8], [4,6,5], [3,8,3], [2,6,9] ])
1) 如果我们想看看哪个同学最喜欢看跳舞。
2) 看看哪位同学最受欢迎。
"""
# stu = ["球球", "冷檬", "蘑菇头"]
# item = np.array([
#     [3, 5, 8],
#     [4, 6, 5],
#     [3, 8, 3],
#     [2, 6, 9]
# ])
# itemMean0 = np.mean(item, axis=0)
# itemMean1 = np.mean(item, axis=1)
# itemVar0 = np.var(item, axis=0)
# itemVar1 = np.var(item, axis=1)
# itemMaxMean0 = np.argmax(itemMean0)
# itemMaxMean1 = np.argmax(itemMean1)
# itemMinVar0 = np.argmin(itemVar0)
# itemMinVar1 = np.argmin(itemVar1)
# # print(itemMaxMean0)
# print(f"第{itemMaxMean1}个同学最喜欢看跳舞")
# print(f"{stu[itemMaxMean0]}最受同学欢迎")

"""
1. 求矩形的面积
 现在给定两个矩形区域的坐标 分别使用box 和 boxes表示 元素对应表示为
 [x1, y1, x2, y2], x1,y1表示矩形左上角的点 x2, y2表示矩形右下角的点 
 box = np.array( [2, 2, 20, 15])
 boxes = np.array([[15, 12, 25, 21]])
1) 分别作图画出 两个矩形区域
2） 分别求出两个矩形的面积
3) 相交部分的面积
备注: np.maximum(X, Y)
X和Y逐位进行比较,选择最大值
如下:
"""

# box = np.array([2, 2, 20, 15])
# boxes = np.array([15, 12, 25, 21])
# areaBox = (box[2]-box[0]) * (box[3]-box[1])
# areaBoxes = (boxes[2]-boxes[0]) * (boxes[3]-boxes[1])
# areaMix = (box[3]-boxes[1]) * (box[2]-boxes[0])
# print(areaBox)
# print(areaBoxes)
# print(areaMix)

box = np.array([2, 2, 20, 15])
boxes = np.array([
    [15, 12, 25, 21],
    [13, 12, 25, 21],
    [12, 12, 25, 21]
])


def areas(box, boxes):
    boxArea = (box[2] - box[0]) * (box[3] - box[1])
    boxesArea = (boxes[:, 0] - boxes[:, 2]) * (boxes[:, 1] - boxes[:, 3])
    print(boxArea)
    print(boxesArea)
    interX1 = np.maximum(box[0], boxes[:, 0])
    interY1 = np.maximum(box[1], boxes[:, 1])
    interX2 = np.minimum([box[2], boxes[:, 2]])
    interY2 = np.minimum(box[3], boxes[:, 3])
    print(interY2.shape)
    # l = max(0, interY2 - interY1)
    # d = max(0, interX2 - interX1)
    # mixArea = l * d
    # print(mixArea)


areas(box, boxes)





"""
2. 给定三个点，求夹角。
"""
# a = np.array([1, 2])
# b = np.array([5, 8])
# c = np.array([3, 10])
# print(np.dot(np.subtract(c, a), np.subtract(b, a)))
# cos = np.dot(np.subtract(c, a), np.subtract(b, a)) / (np.linalg.norm(np.subtract(c, a)) * np.linalg.norm(np.subtract(b, a)))
# angle = np.arccos(cos)
# print(f"角A为：{np.degrees(angle)}")
# cos = np.dot(np.subtract(c, b), np.subtract(a, b)) / (np.linalg.norm(np.subtract(c, b)) * np.linalg.norm(np.subtract(a, b)))
# angle = np.arccos(cos)
# print(f"角B为：{np.degrees(angle)}")
# cos = np.dot(np.subtract(a, c), np.subtract(b, c)) / (np.linalg.norm(np.subtract(a, c)) * np.linalg.norm(np.subtract(b, c)))
# angle = np.arccos(cos)
# print(f"角C为：{np.degrees(angle)}")





