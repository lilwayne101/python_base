"""
    案例：你的女朋友要求你说100遍“我爱你”，但是觉得第44遍不吉利，要求跳过第44遍。
"""
# import random

# i = 1
# while i <= 100:
#     if i != 44:
#         print(f"我爱你{i}遍")
#     i += 1

# n = 0
# while n < 100:
#     n += 1
#     if n == 44:
#        continue  # 结束当前这一次循环，强制进入下一次循环  break：终止整个循环
#     print(f"我爱你{n}遍")

"""
    死循环：  while Ture：
    循环嵌套：while中有while  
"""

"""
    案例：循环嵌套实现打印九九乘法表
    需求：输出九九乘法表
    总结：嵌套循环，从内到外（或者从外到内）逐步使用while循环替换
"""
# row = 1
# while row <= 9:
#     col = 1
#     while col <= row:
#         pro = row * col
#         info = f"{row} * {col} = {pro}"
#         print(info, end='  ')
#         col += 1
#     print()
#     row += 1

"""
    需求：
    打印：
    *
    **
    ***
    ****
    *****
"""

# row = 1
# while row <= 5:
#     print('*' * row)
#     row += 1

"""
    课后练习：
    2.求解1-100中能被3整除的所有数字之和
    3.求解1-100能被3和5同时整除的数字的和
    6.嵌套for循环实现打印九九乘法表
    拓展题：
    1.输入一个数字将其转换为二进制，判断二进制中1的个数
    2.对于输入的四位数1234,返回反转后的结4321
    
    注:for i in range(start,stop,step):  等价于 while start < stop:
                                                start += step
"""

# 2
# i = 1
# sum = 0
# while i <= 100:
#     if i % 3 == 0:
#         sum = sum + i
#     i += 1
# print(sum)

# 3
# i = 1
# sum = 0
# while i <= 100:
#     if i % 3 == 0 and i % 5 == 0:
#         sum = sum + i
#     i += 1
# print(sum)

# 6
# for row in range(9):
#     row = row + 1
#     for col in range(row):   #range()是从0到row-1
#         col =col + 1
#         print(f"{col} * {row} = {col * row}",end='  ')
#     print()

# 拓展题 1.输入一个数字将其转换为二进制，判断二进制中1的个数
# i = 1
# b = 0     #bin
# tim1 = 0  #转换的二进制数中1的个数
# tim2 = 0    #数字整除2的次数
# num = input("请输入一个数字：")
# num1 = num
# num = int(num)     #整数格式化
# while num != 0:
#     if num % 2 == 1:
#         num -= 1
#         num /= 2
#         b += 10 ** (i - 1)
#         i += 1
#         tim1 += 1
#     else:
#         tim2 += 1
#         num /= 2
#         i += 1
# if tim1 == 0:
#     b = 10 ** (i-1)
# print(f"数字{num1}转换为二进制{b}，1的个数是{tim1}")

# 直接使用bin()求二进制函数
# num = input("请输入一个数字：")
# num1 = num
# # print(type(num))      #输入为字符串
# num = bin(int(num))
# num = str(num)
# # print(num)
# # print(type(num))
# tim1 = 0
# for tim in num:
#     if tim == '1':   #注：tim不是int型 是字符串
#         tim1 += 1
# print(f"数字{num1}转换为二进制{num[2:]}，1的个数是{tim1}")  #[]是字符串的截取

# 拓展题 2.对于输入的四位数1234,返回反转后的结4321
# num = input("请输入4位数字:")
# renum= 0
# i = 0
# for x in num:
#     renum += int(x) * 10 ** i
#     i += 1
# print(renum)

"""
    列表
    定义:[]/list()
    容器
    添加
    移除
    修改:根据索引位置修改数据
    查询:根据索引位置查询数据
    
"""
# 定义
# names = ["a","b","c","c"]

# 添加
# names.append('bob')
# 插入
# names.insert(1,'james')

# 将另一个列表添加在后面
# subNames = ['jame','kiki']
# names.extend(subNames)
# print(names)


# None
# print(names.append('bob'))

# 移除
# names.remove('a')
# names.pop(0)
# print(names)

# 修改
# names[0] = 'bob'
# print(names)

# 查询
# name = names[2]
# print(name)

# 统计
# print(names.count('c'))

# 查询元素对应的索引位置
# index = names.index('b')
# print(index)

# 遍历列表中的元素
# for index,var in enumerate(names):
#     print(index,var,end='  ')

# index = 0
# while index < len(names):
#     name = names[index]
#     print(name,end='  ')
#     index += 1


"""
  查询  
"""

# colors = ['red','green','blue','yellow','white','black']

"""
    切片
"""
# nums = [1,2,3,4,5,6,7,8,9,0]
# print(nums[2:8:])
# print(nums[::-1])
# print(nums[-1:-11:-1])
# print(nums[-1])

"""
    排序
"""
# scores = [1,2,3,4,5,4,2,1]
# scores.sort()   #正向排序
# scores.sort(reverse=True)   #反向排序
# print(scores)

"""
    列表嵌套
"""

# students = ['刘备','张飞','关羽']
# for stu in students:
#     print(stu,end=' ')

# students =[
#             ['刘备','张飞','关羽'],  #0
#             ['刘禅','张苞','关胜']   #1
#           ]
# print(students[0])
# print(students[1])

"""
    需求:遍历列表中的每一个元素
"""

# for subStudents in students:
#     print(subStudents,end=' ')
#     for stu in subStudents:
#         print(stu,end=' ')


# 最外层
# i = 0
# while i < len(students):  # 0 1
#     subStu = students[i]   # 0 1 2
#     j = 0
#     while j < len(subStu):
#         print(subStu[j],end=' ')
#         j += 1
#     i += 1

# 练习区分extend（）和append（）
# name1 = ['python','C']
# name2 = ['C++','C']
# # name1.extend(name2)   #extend()添加所有的元素，而忽略列表或者元组
# # print(name1)
# name1.append(name2)     #append()保留原来的列表或元组作为元素进行添加
# print(name1)

"""
    注： 列表中可以储存不同类型的数据，但建议储存相同语义，相同类型的数据
        列表引索不能超出列表中所在的范围
"""

"""
    元组：元组Tuple类似列表list，但其中的元素不能修改
    定义：()/tuple()
    #添加：不能够修改
    #修改：不能够修改
    查询
    
"""
# # names = ('球球', '小斐', '小玲', '聪哥')
# names = ['球球', '小斐', '小玲', '聪哥']
# names = tuple(names)  #元组转换为列表用list(元组)
# print(type(names))
# name = (2,)
# print(name)

"""
    切片
"""

# nums = (1,2,3,4,5,6,7,6,5,4,3,2,1)
# # nums.sort()  #元组不能排序
# print(nums[0])
# print(nums[-2])
# print(nums[-1:-9:-1])
# print(nums[::-1])

# 查询元素对应的索引位置
# print(nums.index(4,1,6))   #在序号2到6中查询引索位置

# 统计
# print(nums.count(5))

"""
    使用元组，同时给多个变量赋值
"""

# info = ('bob','男',20)
# name,sex,age = info
# print(f"{name},{sex},{age}")

"""
    随机函数
"""

# index = random.randint(0,3)
# print(index)

"""
    练习题
"""
"""
2. 假定bags包含列表['a', 'b', 'c', 'd']
1) bags[int('3')//11]求值为多少？
2) bags[-1]求值为多少？
3) bags[-2]求值为多少？
"""
# bags = ['a','b','c','d']
# print(bags[int('3')//11])
# print(bags[-1])
# print(bags[-2])

"""
 3.对接下来的3个问题，假定li包含列表[1.15, 'dog', 13, 'cat', True]
1) bacon.index('cat')求值为多少？
2) bacon.append(99)让bacon中的列表值变成什么样？
3) bacon.remove('cat')让bacon中的列表值变成什么样？
"""
# bacon = [1.15, 'dog', 13, 'cat', True]
# print(bacon.index('cat'))
# bacon.append(99)
# print(bacon)
# bacon.remove('cat')
# print(bacon)

"""
4. 写代码，有如下列表，请按要求实现每个功能
li= ['ethan', 'zoran', 'jim']
a. 计算列表长度并输出
b. 列表中追加元素 “lucy”，并输出添加后的列表
c. 请在列表的第 1 个位置插入元素 “Tony”，并输出添加后的列表
d. 请修改列表第 2 个位置的元素为 “Kelly”，并输出修改后的列表
e. 请删除列表中的元素 “ethan”，并输出修改后的列表
f. 请删除列表中的第 2 个元素，并输出删除元素后的列表
"""
# li=['ethan', 'zoran', 'jim']
# # print(len(li))
# # li.append('lucy')
# # print(li)
# # li.insert(0,'Tony')
# # print(li)
# # # li[1] = 'Kelly'
# # # print(li)
# # li.remove('ethan')
# # print(li)
# li.pop(1)
# print(li)

"""
5. 给定一个列表 nums = [10, 20, 30, 50, 70, 20], 查询20首次出现的索引位置，请使用遍历方式完成。
"""
# nums = [10, 20, 30, 50, 70, 20]
# i = 0
# for x in nums:
#     if x == 20:
#         print(i)
#         break
#     i += 1

"""
5. 假设有一个列表 names=[“曹操”,”刘备”,”关羽”,”张飞”,”小乔”,”诸葛亮”],如何依次打印出里面所有的人名
"""
# names=['曹操','刘备','关羽','张飞','小乔','诸葛亮']
# for x in names:
#     print(x)

"""
6. 假设有一个列表 names = [[“张飞”,”刘备”,”关羽”],[“曹操”,”典韦”,”司马懿”]],如何将names这个列表通过代码
转变得到如下列表 li=[“张飞”,”刘备”,”关羽”,“曹操”,”典韦”,”司马懿”]
"""
# names = [['张飞','刘备','关羽'],['曹操”','典韦','司马懿']]
# li = names[0]
# li.extend(names[1])
# print(li)

"""
    拓展题:
    1. 随机分配商品
    需求：有三个店铺，6个商品，6个商品随机分配到3个店铺
"""

# import random
# shopList = [[],[],[]]
# goodList = ['a','b','c','d','e','f']
# for i in range(6):    注：需求是将商品全部随机分配给店铺，而不是店铺分给商品，所以应该对商品进行遍历而不是店铺
#     shopList[random.randint(0,2)].append(goodList[i])
# print(shopList)
# 总结：append()加在最后面，无排序要求是使用.  insert(,index)有序号要求是使用。 extend()不要列表格式，只要元素时使用

"""
2. 有1，2，3，4四个数字，求这四个数字能生成多少个互不相同且无重复数字的三位数。
"""

# amount = 0
# for i in range(4):
#     for j in range(3):
#         for k in range(2):
#             nums = [1, 2, 3, 4]
#             nums.pop(i)
#             nums.pop(j)
#             nums.pop(k)
#             amount += 1
# print(amount)

"""
    总结：增：list.append(variable) ：添加在末尾
            list.extend(list) ：把一个列表里的元素添加在另一个表后边
            list.insert(index,) ；指定位置插入
         删：del(list[index]) :删除列表中指定位置的元素  注del list 是直接取消list的定义
            list.remove(variable) ：删除列表中第一个出现的元素
            list.pop(index) ：删除列表中指定位置的元素
            list.pop ：删除列表中末尾的元素
            list.clear() ：清空列表 等于del list[:] 
         改：list[index]=variable ：直接更改列表中的指定位置的元素
         查：variable = list.index(variable) ：得出列表中指定元素的位置
            variable = list[index] ：查询列表中指定位置的元素
            len(list)  ：查询列表长度
            list.count(variable)  ：查询列表中元素出现的次数
        排序：list.sort() :将列表中元素升序排序 
             list.sort(reverse = Ture)  ：降序排列
             list.reverse()  ：逆序排列，反转
"""
