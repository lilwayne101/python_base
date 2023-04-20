"""
    ASCII 在早期的时候 只存储了128个字符  大小写字符  数字  特殊符号  1个字节 8位
    1000  ---> 8

    unicode 码   整了两个字节存储。 存在另一个问题：外文需要一个字节  浪费空间了
    utf-8  可变长度编码：


"""
import time

# 打开文件
# 参数w在写入的时候会将之前的文本删除，重新开始写入
# file = open('data.txt', 'w', encoding='utf-8')
# file = open('data.txt', 'a+', encoding='utf-8')
# # 写入数据
# file.write('第一行')
# file.write('第二行\n')
# file1 = open('data.txt', 'r', encoding='utf-8')
# file.writelines(['第一行', '第二行'])
# print(file1.readlines())
# print(file1.readline())
# file.seek(0)
#
# # 读取
# file = open('data.txt', 'r', encoding='utf-8')
# # 一次性读取
# # lines = file.read()
# lines = file.readlines()
# for line in lines:
#     # line = line.replace('\n', '')
#     # line = line.strip()
#     print(line)


"""
案例： 需求：
1. 程序启动，提示用户登录或者注册
2. 选择注册->要求输入用户名和密码->返回注册提示信息
3. 选择登录->要求输入用户和密码->判断是否登录成功
"""

# LoginOrRegister = input("程序启动，登录请输入1，注册请输入0\n")
# if LoginOrRegister == '0':
#     file = open('user.txt', 'a+', encoding='utf-8')
#     UserName = input("注册:请输入用户名:")
#     UserPassword = input("注册:请输入用户密码:")
#     file.writelines([UserName+'|'+UserPassword+'\n'])
#     file.close()
# elif LoginOrRegister == '1':
#     file = open('user.txt', 'r', encoding='utf-8')
#     lines = file.readlines()
#     while 1 == 1:
#         UserName = input("登录:请输入用户名:")
#         UserPassword = input("登录:请输入用户密码:")
#         for line in lines:
#             info = line.strip().split('|')
#             if info[0] == UserName and info[1] == UserPassword:
#                 print("登录成功！")
#                 break
#             else:
#                 print("登录失败，请重新登录！")
#                 break
#         break

"""
案例：
1. 打开别人的文件, 自己的文件
2. 读取别人的文件中的代码 写到自己的文件中
3. 关闭自己的文件和别人的文件
"""
# sourseFile = open('user.txt', 'r', encoding='utf-8')
# lines = sourseFile.readlines()
# file = open('task.txt', 'w', encoding='utf-8')
# for line in lines:
#     file.write(line)
# file.close()
# sourseFile.close()

with open('./media/OIP-C.jpg', 'rb') as srcFile:
    lines = srcFile.readlines()
with open('./media./lenin.jpg', 'wb') as targetFile:
    targetFile.writelines(lines)


"""
1. 所有文件都是二进制组成的,包含文本文件. 我们读取文件中的二进制
2. 一次读取1k的内容,然后写入文件, 读取多次
"""


# fileName = input('请输入需要读取的文件：')
# scrFile = open(fileName, 'rb')
# index = fileName.rfind('.')
# targetFileName = fileName[:index] + '-副本' + fileName[index:]
# targetFile = open(targetFileName, 'ab')
# content = scrFile.read(1024)
# while len(content):
#     targetFile.write(content)
#     content = scrFile.read(1024 * 1024)
#
# targetFile.close()
# scrFile.close()

"""
文件相关操作
重命名
删除文件
创建文件夹
获取当前目录
改变目录
获取目录列表
"""


import os

# 重命名
# open('user.txt', 'a+', encoding='utf-8')
# os.rename('user.txt', 'user_bak.txt')
# os.rename('user_bak.txt', 'user.txt')
# # 删除文件
# os.remove('user.txt')
# 创建文件夹
# os.mkdir('./data')
# 获取当前目录
# print(os.getcwd())
# 改变目录
# os.chdir('../')
# print(os.getcwd())
# os.chdir('./code')
# 获取目录列表
# dirs = os.listdir(r'E:\software\zs_python\Day_7')
# print(dirs)
# for dir in dirs:
#     # if os.path.isdir(dir):
#     #     print(f'目录{dir}')
#     if os.path.isfile(dir):
#         print(f'文件{dir}')

# os.rmdir(r'E:\software\zs_python\Day_7')
# filepath = r'E:\software\test\test'
# # os.mkdir(filepath)
# dirs = os.listdir(r'E:\software')
# print(dirs)
# os.rmdir(r'E:\software\test')
# print(os.path.isfile(r'E:\software\test'))
# print(os.path.isdir(r'E:\software\test'))
# filePath = r'E:\software\zs_python\Day_7\media\lenin.jpg'
# dir, extension = os.path.splitext(filePath)
# print(dir)
# print(extension)
"""
JSON语法格式
"""


import json
#
# dic = {
#     'name': 'bob',
#     'age': 18
# }
# jsonStr = json.dumps(dic)
# print(jsonStr)
# print(type(jsonStr))
#
# data = json.loads(jsonStr)
# print(data)
# print(type(data))
# file = open('user.txt', 'w', encoding='utf-8')
# file.write(jsonStr)
# file.close()
#
# file = open('user.txt', 'r', encoding='utf-8')
# print(file.read())


# {
#     {
#         'name': 'sunny',
#         'age': 19
#     },
#     {
#         'name': 'andy',
#         'age': 19
#     }
# }

"""
    案例：人有手，手有关键点
"""
# {
#     'name': 'sunny',
#     'age': 18,
#     'hand': {
#         'type': 'right',
#         'landmark': [
#             {'x': 100, 'y': 200},
#             {'x': 120, 'y': 240}
#         ]
#
#     }
# }

"""
    案例2：JD商城下面有店铺shop,shop店铺下面有商品
"""



"""
课后练习：
1. 打印文件夹下面的所有目录
2. 批量重命名文件
"""
# filePath = r"E:\software\test"
# dirs = os.listdir(filePath)
# for dirTest in dirs:
#     dirName, contest = os.path.splitext(dirTest)
#     dir_path = os.path.join(filePath, dirTest)
#     if os.path.isfile(dir_path):
#         print(dirName)
#         os.chdir(filePath)     #将当前目录路径修改为需要重命名文件的文件路径
#         os.rename(dirTest, input('请输入新的文件名：'))   #os.rename（）默认修改当前目录下的文件
#         pass

"""
3. 按要求完成
1) 将以下数据写入文件
2) 再将数据读取出来存储在dataDic中形式为:
"""
# 定义数据
# data = [
#     ['path', 'x', 'y', 'w', 'h'],
#     ['1.png', '100', '100', '200', '200'],
#     ['2.png', '50', '100', '100', '100'],
#     ['3.png', '200', '50', '150', '100'],
#     ['4.png', '150', '100', '100', '100']
# ]
# file = open('test.txt', 'w', encoding='utf-8')
# for row in range(len(data)):
# #     for col in range(len(data[row])):
# #         file.writelines(data[row][col]+"\t")
#     carInfo = '\t'.join(data[row])
#     file.write(carInfo)
#     file.write('\n')
#
# file.close()
# file = open('test.txt', 'r', encoding='utf-8')
# dataDic = file.read()
# print(dataDic)
# print(type(dataDic))
# file.close()

"""
4. 当前有以下数据集分别是对应的训练集(TRAIN) 测试集(TEST), 数据内容如下图所示
"""



"""
3. 读取文件label_train.txt内容 使用\t进行分割,车牌号的读取
    将汽车信息存在汽车的对象中，所以我们需要建立一个类
"""
# class Car:
#     def __init__(self, transcription, points):
#         self.transcription = transcription
#         self.points = points
#
#     def showInfo(self):
#         print(f"车牌号：{self.transcription}，坐标：{self.points}")
#         pass
#
#     def __call__(self, *args, **kwargs):
#         print("被调用了")
#         print(type(args))
#         print(args)
#
# def readCarInfo():
#
#
#     file = open('label_train', 'r', encoding='utf-8')
#     lines = file.readlines()
#
#     filePrint = open('car_train_print', 'w', encoding='utf-8')
#     # 保存全部的car数据
#     car_list = []
#     i = 0
#     for line in lines:
#         # 将数据转换为python对象
#         # <class 'list'>
#         lineList = line.split(' ', 1)
#         # print(lineList)
#         carList = json.loads(lineList[1])
#         # print(type(carList))
#         print(carList)
#         dic_car = carList[0]
#         # print(type(dic_car))
#         transcription = dic_car['transcription']
#         points = dic_car['points']
#         print(f"车牌号：{transcription}，坐标：{points}")
#         car = Car(transcription, points)
#         car_list.append(car)
#     return car_list
#
#
# carInfoList = readCarInfo()
# for i in range(len(carInfoList)):
#     carInfoList[i]('sunny')


        # filePrint.write(carList)

        # filePrint.write(lineList[1])

        # print(line)
        # carList = json.loads(lineList[1])
        # print(type(carList))
        # print(carList)
        # filePrint.write(carList)

"""
当前有以下数据集分别是对应的训练集（Train） 测试集（Test）
1. 请设计一个函数，分别将训练集和测试集读取到列表中
2. 将人体关键点写入文件中
    分析：
    1.找到目录
        path = D:\data_set\MNIST\TEST
        path = D:\data_set\MNIST\TRAIN
    2.遍历目录
        import os
        labels = os.listdir(path)
        for label in labels:
            labelPath = os.path.join(path, label)
            file = os.listdir(labelPath)

"""
import os


# def load_dataset(dataset, isTrain = True):
#     """
#     加载数据集Train
#     :param isTrain:
#     :return:
#     """
#     path = r"D:\data_set\MNIST"
#     if isTrain:
#         datasetPath= os.path.join(path, "Train")
#     else:
#         datasetPath = os.path.join(path, "TEST")
#
#     labels = os.listdir(datasetPath)
#     for label in labels:
#         labelPath = os.path.join(path, label)
#         files = os.listdir(labelPath)
#         for file in files:
#             filePath = os.path.join(labelPath, file)
#             dataset.append(filePath)
#     # 返回列表储存的是图片的路径
#     return dataset
#
# dataset = []
# load_dataset(dataset, True)
# print(len(dataset))
#
# testData = []
# testData = load_dataset(testData, False)
# print(len(testData))


"""
    拓展题 升华题目
    dic ={}
    
"""

"""
    异常
"""
#
# try:
# # 模拟用户输入错误
#     ZeroDivisionError
#     # num = 1 / 0
# # NameError
# #     print(num)
# # FileNotFoundError
#     open('data.txt')
#     print('输入用户信息')
# except NameError as e:
#     print('NameError:', e)
# except ZeroDivisionError as e:
#     print('ZeroDivisionError:', e)
# except ValueError as e:
#     print('ValueError:', e)
# except FileNotFoundError as e:
#     print('FileNotFoundError:', e)
# except Exception as e:
#     print('Exception:', e)
# else:
#     print('没有异常爽歪歪')
# finally:
#     print('这句话，无论异常是否发生都会执行。')

























"""
解释性语言
file = open(r'','a+',encoding='utf-8')
读写操作
file.read()
file.read(5)
file.readline()
file.seek(0)
file.close()
file.write()
删除文件
import os
if os.path.exists(r"1.txt"):
    os.remove(r"1.txt")
else:
    print("文件不存在")
删除文件夹
import os
os.rmdir(r"myfolder")#只能删除空文件夹
相对路径转绝对路径
import os
print(os.getcwd())#读取当前目录下的路径
files = listdir(r"c:\\")#返回path包含的文件或文件夹的名字的列表
for f in files:
    print(f)
#创建的目录
os.mkdir(r"d:\test\test")
"""
# import time
# print(time.time())
# print(time.strftime("%Y%m%d%H%M%S",time.localtime()))
#
# while True:
#     print(time.strftime("%Y%m%d%H%M%S", time.localtime()))
#     time.sleep(1)
import os
import time

# oldFilePath = input("请输入文件，绝对路径")
# oldFile = open(oldFilePath, "a+", encoding="utf-8")
# # 新文件的创建
# print(os.getcwd()+"\\备份\\")
# newFilePath = os.getcwd() + "\\备份\\"
# newFilePath += time.strftime("%Y%m%d%H%M%S", time.localtime())
# newFilePath += oldFilePath[oldFilePath.rfind("."):]
# # 新文件，写操作
# newFile = open(newFilePath, "a+", encoding="utf-8")
# oldFile.seek(0)
# newFile.write(oldFile.read())
# oldFile.close()
# newFile.close()












