"""
    内容总结：变量：
            类型：
            运算符：算术，比较，赋值，身份，逻辑
            类型转换：
            格式化输出：
            条件控制语句：
            循环语句：
            列表：容器，增删改查
            元组：


"""

"""
    需求:
    1.找出全为255的行数
    2.多少个值是255
    nums = [
            [255, 255, 255, 255],
            [0, 255, 0, 255],
            [255, 255, 255, 255]
            ]
"""
# nums = [
#     [255, 255, 255, 255],
#     [0, 255, 0, 255],
#     [255, 255, 255, 255]
# ]
# times1 = 0    #一行中255的次数
# times2 = 0    #255出现的总次数
# print("全为255的行数是：", end='')
# for i in range(len(nums)):
#     for var in nums[i]:
#         if var != 255:          #times = 0
#             break               #if var == 255
#         else:                   #    times1 += 1
#             times1 += 1         #删除
#     if times1 == len(nums[i]):
#         print(f"{i}",end=" ")
#     times1 = 0
#     times2 += nums[i].count(255)
# print(f"列表中255的个数为：{times2}")

# nums = [
#     [255, 255, 255, 255],
#     [0, 255, 0, 255],
#     [255, 255, 255, 255]
# ]
# tempList = []
# row = 0
# total = 0
# for index,secNums in enumerate(nums):
#     if secNums.count(255) == len(secNums):
#         print(index,secNums)
#         tempList.append(secNums)
#     total += secNums.count(255)
# print(total)
# print(tempList)

"""
    遍历异常
"""
# nums = [10,20,30,40,50,60,70]
# for index,num in enumerate(nums):
#     nums.remove(num)
#     print(index)
#     print(nums)
# print(nums)
# tempList = [20,40,50]
# for num in tempList:
#     nums.remove(num)
# print(nums)

"""
    列表生成式构造：[元素 迭代式 条件表达式]
"""
# nums = [var for var in range(1,11)]
# print(nums)
#
# nums = [var for var in range(1,101) if var %2 == 0]
# print(nums)

"""
    字符串的加强：字符串一旦定义，其内存地址不变
"""
# name = 'sun'
# print(id(name))
# print(id('sun'))
# name1 = 'sun'  #等价于 name1 = name = 'sun'
# print(id(name1))

"""
    转义字符：\n  \t  \\

"""
# print("i lo\\ve\n people\n")

"""
    字符串操作
"""
# info = '英特纳雄耐尔'
# print(info[0])
# print(info[3])
# #切片
# print((info[0:3]))
# print(info[-5:-1])
# print(info[-1:-5])
# print(info[-1:-5:-1])

"""
    字符串的练习
"""
# info = '英特纳雄耐尔'
# i = 0
# while i < len(info):
#     print(info[i])
#     i += 1
#
# for letter in info:
#     print(letter)

# info = 'a=bcd=eFG'
# print(info.islower())
# print(info.lower())
# print(info.isupper())
# 分割之后返回的是列表
# print(info.split('='))

# info = '全世界无产者，联合起来！'
# print(info.replace('无产者','资本家'))

# info = 'mler.jpg'
# list = ['1','2','3']
# print(info.isspace())
# print(info.isalnum())
# print(info.isalpha())
# print(info.isdecimal())
# print(info.isdigit())
# print(info.istitle())
# print(info.startswith('m'))
# print(info.endswith('m'))
# print(info.find('m',0,len(info)))
# print(info.rfind('l',0,len(info)))
# print(info.index('f'))
# print(info.rindex('o'))
# print(info.replace('e','b',1))
# print(info.capitalize())
# print(info.title())
# print(info.lower())
# print(info.upper())
# print(info.swapcase())
# print(info.partition('f'))
# print(info.rpartition('e'))
# print(info.splitlines())
# print(info.rsplit(' ',2))
# print(info.join('123'))
# print('='.join(list))
# print(info.lstrip())
# print(info.rstrip())
# print(info.strip('mlm'))
# print(info.lstrip('ml'))
# print(info.rstrip('er'))
# print(info.startswith('ml'))
# print("你的名字是{}，我的年龄是{}".format('小王',47))
# print('你的名字是{0}，我名字是{1},我的小名是{0}'.format('小王','小张'))
# print('我的名字是{name}，年龄是{age}'.format(name = '小张', age = '23'))

"""
    字典：容器
    定义：{key1:value1,key2:value2}  注：key值唯一，value可不唯一
    
    添加：
    删除：
    修改：
    查询：
"""
# dic = {'age': 20, 'name': 'bob'}
# print(dic)

# 添加
# 如果key不存在中没有就会添加:如果key存在就会修改
# dic['job'] = 'actor'
# print(dic)
# dic['job'] = 'doctor'
# print(dic)
# 删除 :只能删除key
# del dic['name']
# print(dic)
# del dic['bob']
# print(dic)   #KeyError

# 查询
# print(dic.keys())
# for key in dic.keys():
#     print(key)
# print(dic.values())
# for value in dic.values():
#     print(value)

# for key,value in dic.items():
#     if key == 'age':
#         if value >= 18:
#             print('ok')
#     print(key,value)

# for key in dic.keys():
#     print(key,dic[key],end=' ')

"""
    练习
"""
# dic = {'姓名':'张飞','年龄':20,'职业':'将军','住址':'成都'}
# dic['性别'] = '男'
# print(dic)
# dic['姓名'] = '关羽'
# print(dic)
# dic.setdefault('性别','女')
# print(dic)
# dic.setdefault('关系','父子')
# print(dic)
# dic.update({'婚姻':'未婚'})
# print(dic)
# del dic['婚姻']
# print(dic)
# dic.pop('关系')
# print(dic)
# # dic.clear()
# # print(dic)
# dic1 =dic['职业']
# print(dic1)
# print(dic.get('住址'))
# print(len(dic))
# print(dic.values())
# print(dic.keys())
# print('姓名' in dic.keys())
#
# if '住址' in dic.keys() and '成都' == dic['住址']:
#     print('立即抓捕')

"""
    集合：无序的不重复元素序列， 作用，去掉列表中的重复元素
"""

# nameSet = {'张飞','关羽','刘备'}
# names = ['张飞','关羽','张飞','关羽']
# print(set(names))

"""
    内置函数：len(),del(),max(),min()
"""
"""
    运算符：+，*，in，not in
"""
# nums1 = [0,2,3,4]
# nums2 = [1,2,3]
# print(nums1 + nums2)
# print(nums1 * 3)
# print(4 in nums1)
# print(5 not in nums1)

"""
    课堂练习：
    名片管理 系统 录入三张名片即可
    名片盒子 列表中存放字典,为什么要这样存放?为什么不是字典中存放列表?
    cards = [
        {“name”:”张三”,”tel”:”13812345678”,”job”:”CEO”,”addr”:”四川”}, # 字典
        {名片信息2},
        {名片信息3}
    ]
    需要完成的功能 就是对 名片盒子 进行增删改查
        1. 添加名片: 根据用户录入的信息, 组装成字典 追加到名片盒子里面 cards.append(一个人的名片字典)
        2. 显示所有名片: 遍历名片盒子输出名片信息
        3. 修改名片: 录入需要修改名片的姓名, 根据名字到名片合子查找对应的哪一张名片,如果找到 , 重写录入新的名片信息, 完成修改操作
        4. 删除名片: 录入需要删除名片的姓名, 根据名字到名片盒子中查到对应的名片并删除.
"""
# cards = [
#     {'name': '张三', 'tel': '13812345678', 'job': 'CEO', 'addr': '四川'},
#     {'name': '李四', 'tel': '13698746422', 'job': 'CFO', 'addr': '安徽'}
# ]
# card = {}
# card['name'] = input('请输入姓名：')
# card['tel'] = input('请输入电话号码：')
# card['job'] = input('请输入工作职位：')
# card['addr'] = input('请输入地址：')
# cards.append(card)
# for dic in enumerate(cards):
#     print(dic)
# i = 0
# succeed = 0
# while succeed != 1:
#     rename = input('请输入需要修改名片的名字：')
#     for index, card1 in enumerate(cards):
#         i += 1
#         if rename == card1.get('name'):
#             print("已找到名片")
#             cards[index]['name'] = input('请输入新的姓名：')
#             cards[index]['tel'] = input('请输入新的电话号码：')
#             cards[index]['job'] = input('请输入新的工作职位：')
#             cards[index]['addr'] = input('请输入新的地址：')
#             print('修改成功！')
#             succeed = 1
#             for dic in enumerate(cards):
#                 print(dic)
#             break
#         elif i == len(cards):
#             print('未录入此人名片，请重新输入！')
# i = 0
# succeed = 0
# while succeed != 1:
#     delName = input("请输入需要删除名片的名字：")
#     for index, card2 in enumerate(cards):
#         i += 1
#         succeed = 0
#         if delName == card2.get('name'):
#             print("删除成功！")
#             cards.pop(index)
#             succeed = 1
#             for dic in enumerate(cards):
#                 print(dic)
#             break
#         elif i == len(cards):
#             print('未录入此人名片，请重新输入！')

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
# name = name.strip()
# print("=={}==".format(name))
# print(name.startswith('po'))
# print(name.endswith('a'))
# # print(name.replace('k','c'))
# print(name.split('k'))
# print(type(name.split('k')))

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
# {'name': 'Tom', 'age': 19, 'score': 92, 'sex': '女', 'tel': '15300022839'},
# {'name': 'Jerry', 'age': 20, 'score': 40, 'sex': '男', 'tel': '15300022838'},
# {'name': 'Andy', 'age': 18, 'score': 85, 'sex': '女', 'tel': '15300022837'},
# {'name': 'Jack', 'age': 16, 'score': 65, 'sex': '男', 'tel': '15300022428'},
# {'name': 'Rose', 'age': 17, 'score': 59, 'sex': '男', 'tel': '15300022653'},
# {'name': 'Bob', 'age': 18, 'score': 78, 'sex': '男', 'tel': '15300022867'}
# ]
# num = 0
# aveScore = 0
# for index,stuDic in enumerate(students):
#     print(stuDic.get('name'), end='  ')
#     if stuDic.get('score') < 60:
#         num += 1
#     aveScore += stuDic.get('score')
# print("\n男生信息")
# for index, stuDic in enumerate(students):
#     if stuDic.get('sex') == '男':
#         print(f" {stuDic}")
# print(f"不及格人数为：{num}")
# aveScore = aveScore / len(students)
# print(f"平均分为：{round(aveScore,2)}")

"""
1. 统计下面字符出现的次数
letters = 'abcdabcdabcdabcefg'
打印出下面的结构:
a:4
b:4
c:4
...
"""
# letters = 'abcdabcdabcdabcefg'
# dic = {}
# for letter in letters:
#     if letter in dic:
#         dic[letter] += 1
#     else:
#         dic[letter] = 1
# for key, value in dic.items():
#     print(f"{key} : {value}")

"""
2. 给定一个整数列表 nums 和一个整数目标值 target，请在数组中找出和为目标值的两个整数。
打印形式:
{num1:num2, num3:num4}
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
1:9 <-->9:1 取其中一个
2:8 <-->8:2
"""
# aim = input("请输入一个整数目标值：")
# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# dic = {}
# for num1 in nums:
#     for num2 in nums:
#         if num1 != num2 and num1 + num2 == int(aim) and num1 < num2:
#             dic[num1] = num2
# print(dic)
