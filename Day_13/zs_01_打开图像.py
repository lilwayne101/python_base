"""
    找到图像位置（路径）
    打开
    显示
"""
import numpy as np
from PIL import Image

img = Image.open("OIP-C.jpg")
# <PIL.JpegImagePlugin.JpegImageFile image mode=RGB size=474x632 at 0x1F5F3957A00>
print(img)
imgData = np.asarray(img)
# (632, 474, 3)
print(imgData.shape)
# print(imgData)
# print(img.height)
# print(img.width)
# print(img.mode)
# print(img.size)
# print(img.info)
img.show()
