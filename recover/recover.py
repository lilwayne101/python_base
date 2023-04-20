"""
QQ登录：
需求：根据用户录入的账号和密码登录QQ
"""
import os

# userName = input("请输入用户名：")
# password = input("请输入密码：")
# print(f"用户名：{userName},密码：{password}")

"""
计算面馆销售额
需求:每天卖出100碗面，每碗面13块，一年365天，计算总的销售额。
"""
# bowls = 100
# price = 13
# days = 365
# sumSale = bowls * price * days
# print(f"销售额为：{sumSale}")

"""
编写一个python程序
A. 要求用户输入数据
B. 打印输出数据的类型
"""
# data = input("请输入数据：")
# print(type(data))

"""
3. 编写1个python程序，完成以下要求
A. 从键盘获取用户的姓名、性别、家庭地址
B. 使用一个print输出： 姓名，男，地址：
"""
# userName = input("请输入用户姓名：")
# userSex = input("请输入用户性别：")
# userAddress = input("请输入用户地址：")
# print(f"姓名：{userName},性别：{userSex},地址{userAddress}")

"""
4.编写1个python程序，完成以下要求：
A. 获取用户输入的两个数字
B. 对获取的两个数字进行求和运行，并输出相应的结果
"""
# a = input("请输入一个数字")
# b = input("请输入再输入一个数字")  # 输入数字的数据类型为字符串(str)
# sumData = int(a) + int(b)   # int()将字符串变为整型
# print(sumData)

"""
5. 交换两个变量的值
交换前 a = 1， b = 2 交换后 a = 2, b = 1
把你能想到的实现方式写出来
"""
# a, b = 1, 2
# # a, b = b, a
# # print(a, b)
# temp = a
# a = b
# b = temp
# print(a, b)

"""
1.计算面馆销售额
需求：
通过键盘录入： 每天卖出多少碗面
通过键盘录入： 每碗面多少块
通过键盘录入： 今年共营业多少天
计算并且输出一年的总销售额。   
"""
# bowls = input("每天卖出多少碗面：")
# price = input("每碗面多少元：")
# days = input("今年共营业多少天：")
# sumSale = int(bowls) * float(price) * int(days)
# print("一年的总销售额为：%.1f" % sumSale)

"""
2.求解1-100中能被3整除的所有数字的和
"""
# num = 1
# sumNum = 0
# while num <= 100:
#     if num % 3 == 0:
#         sumNum += num
#     num += 1
# print(sumNum)

"""
3.求解1-100 能被3和5同时整除的数字的和
"""
# num = 1
# sumNum = 0
# while num <= 100:
#     if num % 3 == 0 and num % 5 == 0:
#         sumNum += num
#     num += 1
# print(sumNum)

"""
4.使用while，完成以下图形的输出
*                        *****
**                       ****
***         和            ***
****                      **
*****                     *
"""
# num = 1
# while num <= 5:
#     print('*' * num)
#     num += 1
# num = 5
# print()
# while num >= 1:
#     print('*' * num)
#     num -= 1

"""
6.嵌套for循环实现打印九九乘法表
"""
# for row in range(1, 10):
#     for col in range(1, row + 1):
#         print("%d * %d = %2d" % (row, col, row * col), end=" ")
#     print()

"""
扩展题:
1.输入一个数字将其转换为二进制，判断二进制中1的个数
比如:
数字8 转换为二进制 1000 1的个数是1
数字13 转换为二进制 1101
"""
# num = input("请输入一个数字：")
# num_bin = bin(int(num))
# num_bin.count('1')
# print(num_bin[2:], num_bin.count('1'))

"""
2.对于输入的四位数1234，返回翻转后的结果4321
"""
# nums = 1234
# length = 0
# renum = 0
# for num in str(nums):
#     renum += int(num) * (10 ** length)
#     length += 1
# print(renum)

"""
5. 假设有一个列表 names=[“曹操”,”刘备”,”关羽”,”张飞”,”小乔”,”诸葛亮”],如何依次打印出里面所有的人名
"""
# names = ['曹操', '刘备', '关羽', '张飞', '小乔', '诸葛亮']
# for index, name in enumerate(names):
#     print(name)

"""
6. 假设有一个列表 names = [[“张飞”,”刘备”,”关羽”],[“曹操”,”典韦”,”司马懿”]],如何将names这个列表通
过代码 转变得到如下列表 li=[“张飞”,”刘备”,”关羽”,“曹操”,”典韦”,”司马懿”]
"""
# names = [['张飞', '刘备', '关羽'], ['曹操', '典韦', '司马懿']]
# names[0].extend(names[1])  # 注意list.函数（）无返回值
# li = names[0]
# print(li)

"""
7. 随机分配商品
需求：有三个店铺，6个商品，6个商品随机分配到3个店铺
分析:
3个店铺： shopList = [[], [], []]
6个商品: goodsList = ['小米', '苹果', 'vivo', '华为']
随机取一个店铺将商品放进来
"""
# import random
# shopList = [[], [], []]
# goodList = ['小米', '苹果', '坚果', '华为']
# for goods in goodList:
#     shopList[random.randint(0, 2)].append(goods)
# print(shopList)

"""
8. 给定一个整数列表 nums 和一个整数目标值 target，请在数组中找出和为目标值的两个整数。
打印形式:
{num1:num2, num3:num4}
"""
# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# target = 10
# for addend_1 in nums:
#     for addend_2 in nums:
#         if (addend_1 + addend_2) == target and addend_1 < addend_2:
#             print(f"{addend_1}:{addend_2}")

"""
名片管理 系统 录入三张名片即可
名片盒子 列表中存放字典,为什么要这样存放?为什么不是字典中存放列表?
cards = [
 {“name”:”张三”,”tel”:”13812345678”,”job”:”CEO”,”addr”:”四川”}, # 字典
 {名片信息2},
 {名片信息3}
]
需要完成的功能 就是对 名片盒子 进行增删改查
1. 添加名片: 根据用户录入的信息, 组装成字典 追加到名片盒子里面 cards.append(一个人的名片字
典)
2. 显示所有名片: 遍历名片盒子输出名片信息
3. 修改名片: 录入需要修改名片的姓名, 根据名字到名片合子查找对应的哪一张名片,
如果找到 , 重写录入新的名片信息, 完成修改操作
4. 删除名片: 录入需要删除名片的姓名, 根据名字到名片盒子中查到对应的名片并删除.
"""
# cards = [
#  {"name": "张三", "tel": "13812345678", "job": "CEO", "addr": "四川"},  # 字典
# ]
#
# while len(cards) < 3:
#     print("名片录入中...")
#     card = {"name": input("请输入用户："), "tel": input("请输入电话号码："),
#             "job": input("请输入职位："), "addr": input("请输入地址：")}
#     cards.append(card)
# for card in cards:
#     print(card)
# judgment = 0
# while judgment == 0:
#     name = input("请输入需要修改名片的用户名：")
#     for index, card in enumerate(cards):
#         if name in card.values():
#             print("名片录入中...")
#             cards[index] = {"name": input("请输入用户："), "tel": input("请输入电话号码："),
#                             "job": input("请输入职位："), "addr": input("请输入地址：")}
#             judgment = 1
#             break
#     if judgment == 0:
#         print("无此人名片，请重新输入！")
# while judgment == 1:
#     name = input("请输入需要删除名片的用户名：")
#     for index, card in enumerate(cards):
#         if name in card.values():
#             cards.pop(index)
#             judgment = 0
#             break
#     if judgment == 1:
#         print("无此人名片，请重新输入！")
# for card in cards:
#     print(card)
"""
2. 写代码，有如下变量，请按照要求实现每个功能
name = " posekakaka "
a. 移除name 变量对应的值两边的空格，并输出移除后的内容
name = "posekakaka"
b. 判断name 变量对应的值是否以 "po" 开头，并输出结果
c. 判断name 变量对应的值是否以 "a" 结尾，并输出结果
d. 将name 变量对应的值中的 “k” 替换为 “c”，并输出结果
e. 将name 变量对应的值根据 “k” 分割，并输出结果。
f. 请问，上一题 e 分割之后得到值是什么类型（可选）
"""
# name = " posekakaka "
# name = name.strip()   # a
# print(name.startswith("po"))   # b
# print(name.endswith("a"))
# print(name.replace("k", "c"))
# print(name.split("k"))
# print(type(name.split("k")))
# print(name)
"""
3. 列表students中保存了6个学生的信息
students = [
{'name':'Tom', 'age': 19, 'score': 92, 'sex': '女', 'tel':'15300022839'},
{'name':'Jerry', 'age': 20, 'score': 40, 'sex': '男', 'tel':'15300022838'},
{'name':'Andy', 'age': 18, 'score': 85, 'sex': '女', 'tel':'15300022837'},
{'name':'Jack', 'age': 16, 'score': 65, 'sex': '男', 'tel':'15300022428'},
{'name':'Rose', 'age': 17, 'score': 59, 'sex': '男', 'tel':'15300022653'},
{'name':'Bob', 'age': 18, 'score': 78, 'sex': '男', 'tel':'15300022867'}
]
3.1 遍历所有的姓名
3.1 统计不及格学生的个数
3.2 打印所有男生的信息
3.3 求平均分数
"""
# students = [
#     {'name': 'Tom', 'age': 19, 'score': 92, 'sex': '女', 'tel': '15300022839'},
#     {'name': 'Jerry', 'age': 20, 'score': 40, 'sex': '男', 'tel': '15300022838'},
#     {'name': 'Andy', 'age': 18, 'score': 85, 'sex': '女', 'tel': '15300022837'},
#     {'name': 'Jack', 'age': 16, 'score': 65, 'sex': '男', 'tel': '15300022428'},
#     {'name': 'Rose', 'age': 17, 'score': 59, 'sex': '男', 'tel': '15300022653'},
#     {'name': 'Bob', 'age': 18, 'score': 78, 'sex': '男', 'tel': '15300022867'}
# ]
# num_fail = 0
# average_score = 0
# print("学生名单：", end="")
# for index, student in enumerate(students):
#     print(student.get("name"), end="  ")
#     if student.get("score") < 60:
#         num_fail += 1
#     average_score += student.get("score")/len(students)
# print(f"\n不及格同学人数：{num_fail}")
# print("\n男生名单：", end='')
# for index, student in enumerate(students):
#     if student.get("sex") == "男":
#         print(student)
# print(f"平均分：{average_score}")

"""
1. 统计下面字符出现的次数
letters = 'abcdabcdabcdabcefg'
"""
# letters = 'abcdabcdabcdabcefg'
# dic_letter = {}
# for letter in letters:
#     if letter not in dic_letter:
#         dic_letter[letter] = 1
#     else:
#         dic_letter[letter] += 1
# print(dic_letter)

"""
2. 给定一个整数列表 nums 和一个整数目标值 target，请在数组中找出和为目标值的两个整数。
打印形式:
{num1:num2, num3:num4}
"""
# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# target = 10
# sum_num = {}
# for num_1 in nums:
#     for num_2 in nums:
#         if num_1 + num_2 == target and num_1 < num_2:
#             sum_num[num_1] = num_2
# print(sum_num)

"""
    1. 定义一个函数,实现返回三个数的和
"""


# def sum_num(num1, num2, num3):
#     return num1 + num2 + num3
#
#
# print(sum_num(7, 8, 9))

"""
2. 定义一个函数,实现返回三个数的最大值
"""


# def max_num(num1, num2, num3):
#     return max(num1, num2, num3)
#
#
# print(max_num(5, 6, 7))

"""
3. 定义一个函数,实现返回三个数的最小值
"""


# def min_num(num1, num2, num3):
#     if num1 < num2 and num1 < num3:
#         return num1
#     elif num2 < num1 and num2 < num3:
#         return num2
#     else:
#         return num3
#
#
# print(min_num(2, 5, 6))

"""
4. 给定列表 nums = [10, 20, 30, 50, 20],定义一个函数找出给定元素的所有位置
"""
# nums = [10, 20, 30, 50, 20]
#
#
# def find_ele(ele):
#     for index, num in enumerate(nums):
#         if ele == num:
#             print(index, end='  ')
#     return
#
#
# find_ele(20)

"""
5. 定义一个函数,编写1个python程序，完成以下要求：
1.1 设计一个功能从键盘获取用户的姓名、性别、家庭地址
1.2 打印从该功能中获取的信息
"""


# def function():
#     msg = {"name": input("请输入姓名："), "sex": input("请输入性别："), "家庭地址": input("请输入家庭地址：")}
#     return print(msg)
#
#
# function()

"""
 6.使用for循环实现99乘法表
"""
# for row in range(1, 10):
#     for col in range(1, row + 1):
#         print(f"{row} * {col} = {row * col}", end='\t')
#     print()

"""
7.求阶乘 n! = 1 * 2 * 3 * 4 * ..... * n
"""


# def factorial(order):
#     total = 1
#     for i in range(1, order+1):
#         total *= i
#     return total
#
#
# print(factorial(3))

"""
 8.定义一个函数, 求出1 + 2！+ 3！+ 4！+...+20！的结果
"""


# def series_sum(order):
#     total = 0
#
#     for i in range(1, order + 1):
#         fact = 1
#         for j in range(1, i+1):
#             fact *= j
#         total += fact
#     return total
#
#
# print(series_sum(20))

"""
名片管理 系统 录入三张名片即可
名片盒子 列表中存放字典,为什么要这样存放?为什么不是字典中存放列表?
cards = [
 {“name”:”张三”,”tel”:”13812345678”,”job”:”CEO”,”addr”:”四川”}, # 字典
 {名片信息2},
 {名片信息3}
]
需要完成的功能 就是对 名片盒子 进行增删改查
1. 添加名片: 根据用户录入的信息, 组装成字典 追加到名片盒子里面 cards.append(一个人的名片字
典)
2. 显示所有名片: 遍历名片盒子输出名片信息
3. 修改名片: 录入需要修改名片的姓名, 根据名字到名片合子查找对应的哪一张名片,
如果找到 , 重写录入新的名片信息, 完成修改操作
4. 删除名片: 录入需要删除名片的姓名, 根据名字到名片盒子中查到对应的名片并删除.
"""
# cards = [
#  {"name": "张三", "tel": "13812345678", "job": "CEO", "addr": "四川"},  # 字典
# ]
#
#
# def add_card():
#     # global cards
#
#     while len(cards) < 3:
#         print("名片录入中...")
#         card = {"name": input("请输入用户："), "tel": input("请输入电话号码："), "job": input("请输入职位："), "addr": input("请输入地址：")}
#         cards.append(card)
#     for card in cards:
#         print(card)
#     return cards
#
#
# def revise_card():
#     # global cards
#     judgment = 0
#     while judgment == 0:
#         name = input("请输入需要修改名片的用户名：")
#         for index, card in enumerate(cards):
#             if name in card.values():
#                 print("名片录入中...")
#                 cards[index] = {"name": input("请输入用户："), "tel": input("请输入电话号码："),
#                                 "job": input("请输入职位："), "addr": input("请输入地址：")}
#                 judgment = 1
#                 break
#         if judgment == 0:
#             print("无此人名片，请重新输入！")
#     return cards
#
#
# def del_card():
#     # global cards
#     judgment = 1
#     while judgment == 1:
#         name = input("请输入需要删除名片的用户名：")
#         for index, card in enumerate(cards):
#             if name in card.values():
#                 cards.pop(index)
#                 judgment = 0
#                 break
#         if judgment == 1:
#             print("无此人名片，请重新输入！")
#     for card in cards:
#         print(card)
#     return cards
#
#
# add_card()
# revise_card()
# del_card()

"""
创建一个手机类。手机属性有 颜色, 屏幕大小，价格，品牌, 创建一个对象打印信息。
"""


# class Phone:
#     def __init__(self, color, screen_size, price, brand):
#         self.color = color
#         self.screen_size = screen_size
#         self.price = price
#         self.brand = brand
#
#     def __str__(self):
#         return f"手机颜色：{self.color},屏幕大小：{self.screen_size},价格：{self.price},品牌：{self.brand}"
#
#
# phone = Phone('白色', '18寸', '5000', '小米')
# print(phone)

"""
3、学生信息
1) 封装Student类，包含属性name、age、tel、score、sex，包含方法getScore(打印name、
score)、 getStudent（打印个人的全部信息）。
2) 使用list列对象，存储10个学生对象，迭代所有学生信息。
3）打印不及格学生信息以及统计不及格学生数量
"""


# class Student:
#     def __init__(self, name, age, tel, score, sex):
#         self.name = name
#         self.age = age
#         self.tel = tel
#         self.score = score
#         self.sex = sex
#
#     def get_score(self):
#         print(f"姓名：{self.name},成绩：{self.score}")
#
#     def get_student(self):
#         print(f"姓名：{self.name},年龄：{self.age},电话：{self.tel}, 成绩：{self.score}, 性别：{self.sex}")
#
#
# list_stu = [Student('小王', '18', '138888888', 89, '男'),
#             Student('小周', '18', '138888888', 69, '男'),
#             Student('小李', '18', '138888888', 59, '男'),
#             Student('小邓', '18', '138888888', 49, '男'),
#             Student('小华', '18', '138888888', 39, '男'),
#             Student('小叶', '18', '138888888', 49, '男'),
#             Student('小张', '18', '138888888', 59, '男'),
#             Student('小陆', '18', '138888888', 49, '男'),
#             Student('小毛', '18', '138888888', 99, '男'),
#             Student('小朱', '18', '138888888', 79, '男')]
# num = 0
# for stu in list_stu:
#     if stu.score < 60:
#         stu.get_student()
#         num += 1
#
# print(f"共有{num}名学生不及格")


"""
4、按要求代码实现
徒弟(Prentice):父类
孙悟空
字段：name，age，武器(weapon)，紧箍咒(formula)
方法：吃斋(doMaigre)，念佛(buddha)，取经(doPilgrimage)，战斗(fight), 降妖 (extDevil)
猪八戒
字段：name，age，武器, 媳妇(wife)，
方法，念佛，取经，战斗, 牵马 holding horses ---> (holdHorse)
沙和尚
字段：name，age，武器, 流沙河(sandRiver)，
方法:念佛，取经，战斗, 挑行李 Pick up the luggage --> pickUpLuge
要求：
 1)、分析上面信息，代码优化
 2)、添加一定的剧情(随意发挥)。
"""


# class Prentice:
#     def __init__(self, name, age, weapon):
#         self.name = name
#         self.age = age
#         self.weapon = weapon
#
#     def buddha(self):
#         print(f"{self.name}成功进行一次念经。")
#
#     def do_pilgrimage(self):
#         print(f"{self.name}成功完成一次取经。")
#
#     def fight(self):
#         print(f"{self.name}进行了一场战斗。")
#
#
# class SunWuKong(Prentice):
#     def __init__(self, name, age, weapon, formula):
#         super().__init__(name, age, weapon)
#         self.formula = formula
#
#     def do_maigre(self):
#         print(f"{self.name}成功进行一次吃斋。")
#
#     def ext_devil(self):
#         print(f"{self.name}成功进行一次降妖")
#
#
# class ZhuBaJie(Prentice):
#     def __init__(self, name, age, weapon, wife):
#         super().__init__(name, age, weapon)
#         self.wife = wife
#
#     def hold_horse(self):
#         print(f"{self.name}正在牵马。")
#
#
# class ShaHeShang(Prentice):
#     def __init__(self, name, age, weapon, sandRiver):
#         super().__init__(name, age, weapon)
#         self.sandRiver = sandRiver
#
#     def pick_up_luge(self):
#         print(f"{self.name}正在挑行李。")
#
#
# sunWuKong = SunWuKong("孙悟空", "1220", "金箍棒", "吃斋")
# sunWuKong.do_maigre()
# sunWuKong.buddha()
# sunWuKong.do_pilgrimage()
# sunWuKong.ext_devil()

"""
1. 你和你的女朋友今天准备出去玩：你的男朋友说要出去看电影，女朋友说要学习。
怎么办? 剪刀石头布游戏 3局两胜。请最后显示 获胜的是哪一方?
"""


# class Game:
#     gameTimes = 1
#     girlWin = 0
#     boyWin = 0
#
#     def __init__(self, player1, player2):
#         self.player1 = player1
#         self.player2 = player2
#
#     def play(self):
#         while Game.girlWin != 2 and Game.boyWin != 2:
#             print(f"第{Game.gameTimes}回合：")
#             Game.gameTimes += 1
#             while True:
#                 girl_move = input(f"{self.player1}请出招：(出石头请输入1  出剪刀请输入2  出布请输入3)")
#                 if girl_move not in ['1', '2', '3']:
#                     print("输入错误指令,请重新输入！")
#                 else:
#                     break
#             while True:
#                 boy_move = input(f"{self.player2}请出招：(出石头请输入1  出剪刀请输入2  出布请输入3)")
#                 if boy_move not in ['1', '2', '3']:
#                     print("输入错误指令,请重新输入！")
#                 else:
#                     break
#             if girl_move == boy_move:
#                 print("平局！请继续！")
#                 continue
#             elif (girl_move == '1' and boy_move == '2') or (girl_move == '2' and boy_move == '3') or (
#                     girl_move == '3' and boy_move == '1'):
#                 Game.girlWin += 1
#                 print(f"{self.player1}获胜，目前{self.player1}比{self.player2}的比分为{Game.girlWin}:{Game.boyWin}")
#             else:
#                 Game.boyWin += 1
#                 print(f"{self.player2}获胜，目前{self.player1}比{self.player2}的比分为{Game.girlWin}:{Game.boyWin}")
#
#         if Game.girlWin == Game.gameTimes:
#             print(f"{self.player1}获胜,决定去学习")
#         else:
#             print(f"{self.player2}获胜，决定去看电影")
#         pass
#
#
# game = Game('bob', 'lili')
# game.play()

"""
2. 人体关键点的描述
1) 人有姓名、年龄。根据下面的图形还有很多的关键点landmarks。每一个关键点的描述使用 x, y
去描述。
要求:
创建关键点(创建3个即可), 给person人添加关键点之后。遍历每一个关键点
2) 人体关键点的描述
增加描述人体的：眼部关键点、手部关键点。(分别创建3个即可)
然后分别遍历 眼部 和 手部关键点
"""


# class Person:
#     landmarks = []
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def create_print_marks(self, marks):
#         Person.landmarks = marks
#         print(f"\n年龄为{self.age}的{self.name}的人体关键点有：")
#         for landmark in Person.landmarks:
#             print(landmark, end='\t')
#
#
# class Eyes(Person):
#     rEyeLandmark = []
#     lEyeLandmark = []
#
#     def __init__(self, name, age):
#         super().__init__(name, age)
#
#     def right_eye_marks(self, marks):
#         Eyes.rEyeLandmark = marks
#         print(f"\n年龄为{self.age}的{self.name}的右眼关键点有：")
#         for landmark in Eyes.rEyeLandmark:
#             print(landmark, end="\t")
#
#     def left_eye_marks(self, marks):
#         Eyes.lEyeLandmark = marks
#         print(f"\n年龄为{self.age}的{self.name}的左眼关键点有：")
#         for landmark in Eyes.lEyeLandmark:
#             print(landmark, end="\t")
#
#
# class Hands(Person):
#     rHandLandmark = []
#     lHandLandmark = []
#
#     def __init__(self, name, age):
#         super().__init__(name, age)
#
#     def right_hand_marks(self, marks):
#         Hands.rHandLandmark = marks
#         print(f"\n年龄为{self.age}的{self.name}的右手关键点有：")
#         for landmark in Hands.rHandLandmark:
#             print(landmark, end="\t")
#
#     def left_hand_marks(self, marks):
#         Hands.lHandLandmark = marks
#         print(f"\n年龄为{self.age}的{self.name}的左手关键点有：")
#         for landmark in Hands.lHandLandmark:
#             print(landmark, end="\t")
#
#
# personLandmarks = [{12: 23}, {13: 24}, {14: 21}, {15: 22}, {16: 25}, {17, 26}]
# person = Person("小王", 47)
# person.create_print_marks(personLandmarks)
# leftEye = Eyes("小王", 47)
# leftEye.left_eye_marks(personLandmarks[1:2])
# rightEye = Eyes("小王", 47)
# rightEye.right_eye_marks(personLandmarks[2:3])
# rightHand = Hands("小王", 47)
# rightHand.right_hand_marks(personLandmarks[3:4])
# leftHand = Hands("小王", 47)
# leftHand.left_hand_marks(personLandmarks[4:5])

"""
3、JD商城，商城下面有很多的店铺(3个)， 店铺下面有很多的商品(3个)
要求：遍历商城下面的店铺 以及店铺下面的商品
"""


# class Malls:
#     def __init__(self, mall_name, shop_list):
#         self.mall_name = mall_name
#         self.shop_list = shop_list
#
#     def traverse(self):
#         print(f"{self.mall_name}有店铺：")
#         for shop in self.shop_list:
#             shop.traverse()
#
#
# class Shops:
#     def __init__(self, shop_name, goods_list):
#         self.shop_name = shop_name
#         self.goods_list = goods_list
#
#     def traverse(self):
#         print(f"{self.shop_name}，店里有商品：")
#         for goods in self.goods_list:
#             goods.traverse()
#
#
# class Goods:
#     def __init__(self, goods_name, price, address):
#         self.goods_name = goods_name
#         self.price = price
#         self.address = address
#
#     def traverse(self):
#         print(f"{self.goods_name},售价：{self.price},产地：{self.address}")
#
#
# goods_list1 = [Goods("小米1", "2999", "越南"), Goods("小米2", "3999", "越南"), Goods("小米3", "4999", "越南")]
# goods_list2 = [Goods("华为1", "2999", "越南"), Goods("华为2", "3999", "越南"), Goods("华为3", "4999", "越南")]
# goods_list3 = [Goods("苹果1", "5299", "越南"), Goods("苹果2", "6999", "越南"), Goods("苹果3", "8999", "越南")]
# shopList = [Shops("小米旗舰店", goods_list1), Shops("华为旗舰店", goods_list2), Shops("苹果旗舰店", goods_list3)]
# mall = Malls("JD商城", shopList)
# mall.traverse()

"""
 需求：
1. 程序启动，提示用户登录或者注册
2. 选择注册->要求输入用户名和密码->返回注册提示信息
3. 选择登录->要求输入用户和密码->判断是否登录成功
"""


# def user_log_in():
#     while True:
#         while True:
#             direct = input("登录请输入1  注册请输入2")
#             if direct == '1' or '0':
#                 break
#             print("未识别，请输入指定指令")
#         if direct == '1':
#             name = input("请输入用户名：")
#             name = name + '\n'
#             password = input("请输入密码：")
#             password = password + '\n'
#             with open("user_msg.txt", 'a+', encoding="utf-8") as file:
#                 file.seek(0)
#                 user_list = file.readlines()
#             file.close()
#             if name in user_list and user_list[user_list.index(name) + 1] == password:
#                 print("登录成功！")
#                 break
#             elif name in user_list:
#                 print("密码错误！请重新登录。")
#             else:
#                 print("用户未注册！请重新登录。")
#         if direct == '2':
#             name = input("请输入用户名：")
#             name = name + '\n'
#             password = input("请输入密码：")
#             password = password + '\n'
#             with open("user_msg.txt", 'a+', encoding="utf-8") as file:
#                 user_list = file.readlines()
#                 if name in user_list:
#                     print("用户已存在！")
#                 else:
#                     file.write(name + '\n')
#                     file.write(password + '\n')
#                     print("注册成功!")
#
#
# user_log_in()

"""
需求：
1. 根据录入文件名,复制出来一个新的文件,新的文件名为: 原文件名-副本.源文件后缀
"""
# import os
#
# file_name = input("请输入文件名：")
# with open(file_name, 'a+', encoding='utf-8') as scr_file:
#     scr_file.seek(0)
#     tempText = scr_file.readlines()
#     path = os.getcwd()
#
# dir, extension = os.path.splitext(file_name)
# newPath = path + '\\' + dir + '副本' + extension
#
# with open(newPath, 'w+', encoding='utf-8') as new_file:
#     for text in tempText:
#         new_file.writelines(text)

"""
1. 所有文件都是二进制组成的,包含文本文件. 我们读取文件中的二进制
2. 一次读取1k的内容,然后写入文件, 读取多次
"""
# import os
# fileName = "lenin.jpg"
# with open(fileName, 'rb+') as scrFile:
#     content = scrFile.read(1024 * 1024)
#     index = fileName.rfind('.')
#     targetFileName = fileName[:index] + '-副本' + fileName[index:]
#     with open(targetFileName, 'wb+') as newFile:
#         while len(content):
#             newFile.write(content)
#             content = scrFile.read(1024 * 1024)


"""
JSON案例1：
对dic = {
'name': 'sunny',
'age': 18
}进行Json转换,再转回来
"""

# import json
# dic = {'name': 'sunny', 'age': 18}
# jsonStr = json.dumps(dic)
# print(jsonStr)
# print(type(jsonStr))
#
# jsonDic = json.loads(jsonStr)
# print(jsonDic)
# print(type(jsonDic))

"""
案例2
"""
# import json
# with open('trans.txt', 'r', encoding='utf-8') as transFile:
#     lines = transFile.readlines()
#     for line in lines:
#         jsonContent = json.loads(line)
#         brand = jsonContent[0]['transcription']
#         point = jsonContent[0]['points']
#         print(f"车牌号：{brand},坐标：{point}")

"""
1. 打印文件夹下面的所有目录
2. 批量重命名文件
"""

# import os
# path = r'E:\software\zs_python\recover\files'
# dirList = os.listdir(path)
# for dir_ in dirList:
#     print(dir_)
#     dirPath = path + '\\' + dir_
#     if os.path.isfile(dirPath):
#         os.chdir(path)
#         os.renames(dir_, input("请输入新的文件名"))

"""
3. 按要求完成
1) 将以下数据写入文件
# 定义数据
data = [
['path', 'x', 'y', 'w', 'h'],
['1.png', '100', '100', '200', '200'],
['2.png', '50', '100', '100', '100'],
['3.png', '200', '50', '150', '100'],
['4.png', '150', '100', '100', '100']
]
2) 再将数据读取出来存储在dataDic中形式为:
{
'1.png': [100, 100, 200, 200],
'2.png': [50, 100, 100, 100],
'3.png': [200, 50, 150, 100],
'4.png': [150, 100, 100, 100]
}
"""

# data = [
#     ['path', 'x', 'y', 'w', 'h'],
#     ['1.png', '100', '100', '200', '200'],
#     ['2.png', '50', '100', '100', '100'],
#     ['3.png', '200', '50', '150', '100'],
#     ['4.png', '150', '100', '100', '100']
# ]
#
# with open("test.txt", 'w', encoding='utf-8') as dataFile:
#     for dataEle in data:
#         for ele in dataEle:
#             dataFile.writelines(ele + '\t')
#         dataFile.write('\n')
# with open("test.txt", 'r', encoding='utf-8') as dataFile:
#     dataDic = {}
#     lines = dataFile.readlines()
#     for index, line in enumerate(lines):
#         if index >= 1:
#             line_list = line.split("\t")
#             dataDic[line_list[0]] = line_list[1:len(line_list) - 1]
# print(dataDic)

"""
定义线程需要执行的任务
创建线程
启动线程
"""
# import threading
#
#
# def task(*args):
#     print(threading.currentThread())
#     print(args)
#     pass
#
#
# th = threading.Thread(target=task, args=('sunny',18), name='thread-01')
# th.start()
#
# print(threading.currentThread())
# print(threading.currentThread().name)
# print(threading.currentThread().native_id)

"""
自定义线程类
"""
# import threading
#
#
# class MyThread(threading.Thread):
#     def run(self):
#         print(threading.currentThread())
#         print(self._args)
#
#
# for index in range(2):
#     th = MyThread(args=('sunny', 18))
#     th.start()
#

"""
需求:现在有100张票，开启5个窗口卖票，编写代码请使用线程完成
"""
# import time
# import threading
#
# ticket = 100
# # lock = threading.RLock()
#
# class MyThread(threading.Thread):
#
#     def sale_ticket(self):
#         # lock.acquire()
#         global ticket
#         while ticket > 0:
#             ticket -= 1
#             name = threading.currentThread().getName()
#             print(f"\n{name}卖了一张票,还剩下{ticket}张票。")
#             time.sleep(0.1)
#         # lock.release()
#
#     def run(self):
#         while self.sale_ticket():
#             pass
#
# # threadList = []
# for index in range(5):
#     th =MyThread()
#     # th.setName(f'thread{index}')
#     th.start()
#     # threadList.append(th)



