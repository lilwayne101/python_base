"""
    函数
"""
"""
    def(形式参数) 函数名（）
        ....
    作用：封装
"""
# 参数
# def 函数名(参数1，参数2....)

# def mul(maxRow):
#     row = 1
#     while row <= maxRow:
#         col = 0
#         while col < row:
#             col += 1
#             print(f"{col} * {row} ={col * row}",end=' ')
#         print()
#         row += 1
#
# # 函数定义之后需要被使用
# #使用/调用
# #函数名称()
# mul(6)

# 匿名函数
# add = lambda a, b : a + b
# ret = add(2, 3)
# print(ret)

# 参数加强：必须参数，


# def print_info(msg):
#     print(f"信息是：{msg}")
#     pass
#
#
# print('hello world')


# def print_info(name, age):
#     print(f"姓名是：{name}，年龄是：{age}")
#     pass
#
#
# print_info(age=18, name='小王')

# dic = {'name': '小王', 'age': 18}
#
#
# def print_info(temp_dic):
#     print(f"姓名是：{temp_dic['name']},年龄是：{temp_dic['age']}")
#     pass
#
#
# print_info(dic)


# def hello(num):
#     print(f"hello world {num}")
#     return 'hello world'
# print(type(hello(1)))
#
# hello(1)


# def change(i):
#     print(id(i))
#     i = 10
#     print(id(i))
#
#
# a = 100
# print(id(a))
# change(a)

# def change(mylist):
#     mylist.append([1, 2, 3])
#     print("函数内取值:", mylist)
#     return
#
#
# list1 = [10, 20, 30]
# change(list1)
# print("函数外取值:", list1)

# 关键字参数
# def display(name, age):
#     print("我叫%s,今年%d岁" % (name, age))
#
#
# display('小明', 28)

# # 默认参数
# def display(name='小张', age=18):
#     print("我叫%s，今年%d岁了" % (name, age))
#
#
# display('球球','19')

# 不定长参数(变参*var)
"""
    定义一个方法，传入两个参数，一个表示多个货品的价格，一个类型的折扣，返回货品总价格（使用可变参数）‘
    分析：
    折扣                  cutoff
    多个货品价格            tuple: goodsPrice (1.1, 2.1, 3.0)
"""


# def sale_price(cutoff, *good_price):
#     # print(type(good_price))
#     total = 0.
#     for price in good_price:
#         total += price
#     return total * cutoff
#
#
# print(f"货品总价格为：{round(sale_price(0.8, 1.1, 2.1, 3.0), 2)}")

# 变参
# 变参在在参数列表中有且只有一个，且只能写在最后
# 变参以字典封装传递（**var）
# def display(i, **j):
#     print(i)
#     print(j)
#
#
# display(1, a=2, b=3)

"""
    打印包含姓名，年龄等学生信息的函数
"""


# def print_info(name, age, dic):
#     print(f"学生姓名：{name}，年龄：{age}，工作：{dic['job']},身高：{dic['height']},体重：{dic['weight']}")
#     pass
#
#
# stu = {'job': 'actor',
#        'height': '188',
#        'weight': 160}
# print_info('bob', '18',stu)


# def print_info(name, **j):
#     print(f"学生姓名：{name}，年龄：{j['age']}，工作：{j['job']},身高：{j['height']},体重：{j['weight']}")
#     pass
#
#
# print_info('bob', age=18, job='actor', height=177, weight=120)

# 任何函数的终极形态
# def test(*i,**j):
#         pass

# 返回值加强
"""
    需求：连续射击
"""


# def shot(is_start):
#     if not is_start:
#         print("结束射击")
#         return        # return 用于结束函数类似于循环里的break，但是直接终结函数
#     print("射击")
#
#
# shot(True)
# shot(True)
# shot(False)
# shot(False)

"""
    输入数据返回不同的季节
"""


# def season(num):
#     if num == 1:
#         return "春"
#     elif num == 2:
#         return "夏"
#     elif num == 3:
#         return "秋"
#     elif num == 4:
#         return "冬"
#     else:
#         return "未知信息"
#
#
# print(season(1))

# 返回多个值


"""
    同时对x，y进行求和，减运算
"""


# def add_subtract(x, y):
#     add = x + y
#     sub = x - y
#     return add, sub
#
#
# print(add_subtract(1, 2))

"""
    求a，b，c的最小值 最大值
"""


# def max_minimum(*digit):
#     maximum = max(digit)
#     minimum = min(digit)
#     return maximum, minimum
#
#
# print(max_minimum(5, 6, 7, 3, 4, 7, 8, 1, 0))


# 变量作用域

# y = "全局变量"
#
#
# def fn():
#     global y     # 将函数内的局部变量定义为全局变量，可在函数内对全局变量进行修改
#     y = '局部变量'
#     print(y)
#
#
# fn()
# print(y)

"""
    递归函数：函数直接或间接调用函数本身
"""
# 递归打印10--1


# def recursion(num):
#     if num != 0:
#         print(num)
#         num -= 1
#         recursion(num)
#     else:
#         return
#
#
# recursion(10)

"""
    非递归求阶乘 n！=1*2*3*4*...*n
"""


# def factorial(order):
#     temp_total = 1
#     for i in range(1, order):
#         i += 1
#         temp_total *= i
#     return temp_total

#
#
# print(factorial(4))

# 递归求阶乘


# def factorial(order):
#     temp_total = 1
#     if order != 1:
#         temp_total = order * factorial(order-1)  # 为什么调用factorial()时 temp_total不会重新赋值为1呢：
#     else:  # 原因在于对于函数里面的函数递归而言，temp_total作为更外层的变量，无法被修改，之间的关系类似于全局变量和局部变量
#         order = 1
#     return temp_total
#
#
# print(factorial(6))


"""
    补充知识：os模块  
    打印当前路径下的所有文件夹和文件
"""
# import os
# fl = os.listdir()   # 将当前路径下所以文件夹名和文件名定义成列表
# print(fl)
# for fn in fl:    # 遍历文件夹名和文件名
#     if os.path.isdir(fn):   # 判断是不是目录
#         print("文件夹：" + os.getcwd() + fn)     #
#     if os.path.isfile(fn):    #判断是不是文件
#         print("文件：" + os.getcwd() + fn)


# import os
# count = 0
#
#
# def f_dir(path):
#     files_list = os.listdir(path)
#     for fileName in files_list:
#         file_abpath = os.path.join(path, fileName)
#         if os.path.isdir(file_abpath):
#             print("目录：", fileName)
#             f_dir(file_abpath)
#         else:
#             print("文件：", fileName)
#             global count
#             count += 1
#
#
# f_dir('E:\\')
# print("有%d个文件" % count)


"""
    课后题
"""
# 1. 定义一个函数,实现返回三个数的和


# def sum_num(num1, num2, num3):
#     return num1 + num2 + num3
#
#
# print(sum_num(1, 2, 3))

# 2. 定义一个函数,实现返回三个数的最大值：可直接用max（）函数


# def max_num(num1, num2, num3):
#     temp = 0
#     if num1 > num2:
#         if num1 > num3:
#             temp = num1
#         else:
#             temp = num3
#     elif num2 > num3:
#         temp = num2
#     else:
#         temp = num3
#     return temp
#
#
# print(max_num(1, 2, 3))

# 3. 定义一个函数,实现返回三个数的最小值


# def min_num(num1, num2, num3):
#     temp = 0
#     if num1 < num2:
#         if num1 < num3:
#             temp = num1
#         else:
#             temp = num3
#     elif num2 < num3:
#         temp = num2
#     else:
#         temp = num3
#     return temp
#
#
# print(min_num(1, 2, 3))

# 4. 给定列表 nums = [10, 20, 30, 50, 20], 定义一个函数找出给定元素的所有位置
# nums = [10, 20, 30, 50, 20]
#
#
# def find_num(num, list_nums):
#     for index, ele in enumerate(list_nums):
#         if ele == num:
#             print(f"{index}", end='  ')
#     return
#
#
# find_num(20, nums)

# 5. 定义一个函数,编写1个python程序，完成以下要求：
# 1.1 设计一个功能从键盘获取用户的姓名、性别、家庭地址
# 1.2 打印从该功能中获取的信息

# def name_card():
#     card = {'name': input("请输入姓名："), 'sex': input("请输入性别："), 'address': input("请输入住址：")}
#     temp_judgment = 0
#     while temp_judgment == 0:
#         temp_print = input("查询信息请输入 1\n退出请输入 0 \n请输入:")
#         if temp_print == '1':
#             print(card)
#         elif temp_print == '0':
#             print("感谢您的使用!")
#             return
#         else:
#             print("未识别信息，请重新输入：")
#
#
# name_card()

# 6.使用for循环实现99乘法表

# def list_mult(num):
#     for row in range(1, num + 1):
#         for col in range(1, row + 1):
#             print(f"{col} * {row} = {row * col}", end=' ')
#         print()
#
#
# list_mult(9)

# 7.求阶乘 n! = 1 * 2 * 3 * 4 * ..... * n

# def factorial(order):
#     temp_total = 1
#     if order != 1:
#         temp_total = order * factorial(order - 1)
#     return temp_total
#
#
# print(factorial(3))

# 8.定义一个函数, 求出1 + 2！+ 3！+ 4！+...+20！的结果

# def series_sum(series):
#     def factorial(order):
#         temp_total = 1
#         if order != 1:
#             temp_total = order * factorial(order - 1)
#         return temp_total
#     temp_sum = 0
#     for i in range(1, series + 1):
#         temp_sum += factorial(i)
#     return temp_sum
#
#
# print(series_sum(20))

# 将名片管理系统中的每个功能设计成对应的函数.


# def input_card(num):
#     card = []
#     for i in range(num):
#         card.append({'name': input('请输入姓名:'), 'tel': input('请输入电话号码:'), 'job': input('请输入工作职位：'), 'addr': input('请输入地址：')})
#     return card
#
#
# def display_card(card):
#     for i in range(len(card)):
#         print(card[i])
#
#
# def revise_card(card):
#     re_name = input("请输入要重新录入的名片：")
#     while 1 == 1:
#         for i in range(len(card)):
#             if card[i]['name'] == re_name:
#                 card[i] = input_card(1)[0]
#                 return display_card(card)
#         re_name = input("无此名片，请重新输入：")
#
#
# def del_card(card):
#     del_name = input("请输入要删除的名片：")
#     while 1 == 1:
#         for i in range(len(card)):
#             if card[i]['name'] == del_name:
#                 card.pop(i)
#                 return display_card(card)
#         del_name = input("无此名片，请重新输入：")
#
#
# card1 = input_card(3)
# display_card(card1)
# revise_card(card1)
# del_card(card1)





