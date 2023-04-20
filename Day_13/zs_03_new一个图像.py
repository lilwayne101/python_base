import random
import cv2
from PIL import Image, ImageDraw, ImageFont
import numpy as np
import os

# img = Image.new(mode="RGB", size=(200, 100), color="#dbdbdb")
# img.show()

# data = np.array([[[255, 255, 255]]])
# # (1, 1, 3)
# print(data.shape)
# # int32  i4
# print(data.dtype)
#
# img = Image.fromarray(data)
# img.show()

# img = Image.open("./OIP-C.jpg")
# img.save("./Mom.png")
# imgTemp = Image.open("Mom.png")
# imgTemp = imgTemp.convert("RBG")
# imgTemp.save("MomT.jpg")

# img = Image.open("OIP-C.jpg")
# img = img.resize((300, 200), box=(0, 0, 300, 200))
# img.show()
# print(img.size)

# oriDir = r'C:\Users\Administrator\Desktop\lenin'
# targetDir = r"./target_lenin"
# files = os.listdir(oriDir)
# if not os.path.exists(targetDir):
#     os.mkdir(targetDir)
# for file in files:
#     img = Image.open(os.path.join(oriDir, file))
#     img = img.resize((50, 50), box=(20, 20, 100, 100))
#     img.save(targetDir + '//' + file)

# 通道的分离
# img = Image.open("OIP-C (1).jpg")
# r, g, b = img.split()
# # r.show()
# # g.show()
# # b.show()
#
# # 通道的合并
# Image.merge("RGB", (r, g, b))
# img.show()

# img = Image.open('OIP-C (1).jpg')
# # img.show()
# img = img.rotate(0, translate=(100, 100), fillcolor=(234, 3, 3))
# img.show()

# 图像的拷贝和粘贴
# img = Image.open("OIP-C (1).jpg")
# momImg = Image.open('Mom.png')
# img = img.resize((50,50))
# momImg.paste(img, box=(200, 20))
# momImg.show()

# 图片上面添加字体
# 需要将文字绘制到什么地方
# img = Image.open("OIP-C (1).jpg")
# size = img.size
# print(size)
#
# # 当前需要绘制(画布)
# draw = ImageDraw.Draw(img)
#
#
# # 绘制文字
#
# """
# xy 文字绘制的位置
# text 绘制的具体文字
# fill=None 文字的颜色
# font=None 文字的字体
# """
# # 参数1 就是字体的路径
# font = ImageFont.truetype("arial.ttf", size=20)
# draw.text((0, 0), text='good job', fill=(0, 255, 0), font=font)
#
# img.show()

"""
    需求：生成随机码
    1.生产随机码包含的文字信息
       a-z A-Z 0-9
    2.背景是随机颜色
    
    3.文字是也是随机颜色
    
    4.文字绘制
"""
"""
    a-z: 97-122
    A-Z: 65-90
    0-9: 48-57
    
"""


# def get_code():
#     codes = [code for code in range(97, 123)]
#     codes += [code for code in range(65, 91)]
#     codes += [code for code in range(48, 58)]
#     # print(codes)
#     idx = random.randint(0, len(codes)-1)
#     code = codes[idx]
#     return chr(code)
#
#
# def get_back_color():
#     return random.randint(110, 120), random.randint(100, 110), random.randint(100, 110)
#
#
# def get_color():
#     return random.randint(0, 120), random.randint(0, 110), random.randint(0, 110)
#
#
# # def draw_text():
# #     w = 200
# #     h = 100
# #     data = np.zeros((h, w, 3), dtype='u1')
# #     img = Image.fromarray(data, mode="RGB")
# #     # img.show()
# #     draw = ImageDraw.Draw(img)
# #     font = ImageFont.truetype("arial.ttf", size=70)
# #     for i in range(0, w, 50):
# #         draw.text((i, 0), text=get_code(), fill=get_color(), font=font)
# #     img.show()
#
#
# def draw_text():
#     w = 200
#     h = 100
#     data = np.zeros((h, w, 3), dtype='u1')
#     img = Image.fromarray(data, mode="RGB")
#     # img.show()
#     draw = ImageDraw.Draw(img)
#     font = ImageFont.truetype("arial.ttf", size=70)
#     # 绘制背景
#     for y in range(h):
#         for x in range(w):
#             draw.point((x, y), fill=get_back_color())
#             pass
#     for i in range(4):
#         draw.text((i * w / 4, 0), text=get_code(), fill=get_color(), font=font)
#     img.show()
#
#
# # print(get_code())
# draw_text()

"""
作业：
2.  给图像加边框
    将图像转换为矩阵
"""
# img = Image.open("OIP-C (1).jpg")
# print(img.size)
#
#
# def get_frame(get_img):
#     size = get_img.size
#     size = list(size)
#     size[0] += 20
#     size[1] += 20
#     size.append(3)
#     new_size = tuple(size)
#     print(new_size)
#     data = np.zeros(new_size, dtype='u1')
#     print(data.shape)
#     data = np.transpose(data, (1, 0, 2))
#     frame = Image.fromarray(data, mode='RGB')
#     print(frame.size)
#     draw = ImageDraw.Draw(frame)
#     for x in range(new_size[0]):
#         for y in range(new_size[1]):
#             draw.point((x, y), fill="red")
#     frame.show()
#     frame.paste(img, box=(10, 10, size[0] - 10, size[1] - 10))
#     print(frame.size)
#     print(img.size)
#     frame.show()
#     pass
#
#
# get_frame(img)
# imgData = np.asarray(img)

"""
    3. 将小黄人随机赋值到背景图像上
"""
# img = Image.open("OIP-C (1).jpg")
# imgBack = Image.open("Mom.png")
# img = img.resize((20, 20))
# data_img = np.asarray(img)
# data_back = np.asarray(imgBack)
# size = img.size
# print(data_back.shape)
# point_x = random.randint(1, data_back.shape[0] - 21)
# point_y = random.randint(1, data_back.shape[1] - 21)
# data_back[point_x: point_x + 20, point_y: point_y + 20] = data_img[0: 20, 0: 20]
# imgBack = Image.fromarray(data_back)
# imgBack.show()

"""
    4 读取文件信息，将小黄人粘贴到背景图像上
"""
# img = Image.open("OIP-C (1).jpg")
# imgBack = Image.open("Mom.png")
# img = img.resize((20, 20))
# imgBack.paste(img, (random.randint(0, imgBack.size[0]), random.randint(0, imgBack.size[1])))
# imgBack.show()

"""
    5 将图像进行分割之后进行合并
"""
# img = Image.open("OIP-C (1).jpg")
# size = img.size
# h = size[1]//2
# w = size[0]//2
#
# img_1 = img.crop(box=(0, 0, w, h))
# img_2 = img.crop(box=(w, 0, 2 * w, h))
# img_3 = img.crop(box=(0, h, w, 2 * h))
# img_4 = img.crop(box=(w, h, 2 * w, 2 * h))
#
# img_1.show()
# img_2.show()
# img_3.show()
# img_4.show()
#
# data_1 = np.asarray(img_1)
# data_2 = np.asarray(img_2)
# data_3 = np.asarray(img_3)
# data_4 = np.asarray(img_4)
# # print(img.size)
# # print(data_1.shape)
# # print(data_2.shape)
# # print(data_3.shape)
# # print(data_4.shape)
#
# data_one = np.append(data_1, data_2, axis=1)
# data_two = np.append(data_3, data_4, axis=1)
# data = np.append(data_one, data_two, axis=0)
# # print(data_one.shape)
# img_one = Image.fromarray(data_one)
# img_two = Image.fromarray(data_two)
# img = Image.fromarray(data)
# # img_one.show()
# # img_two.show()
# img.show()

