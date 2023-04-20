# import sys
# print(sys.version)

"""
    多行
    注释
"""

# 变量交换
# a,b=1,2
# a,b=b,a
# print(a,b)

"""
    标识符的规则
    字母，数字，下划线组成
    不能以数字开头
    不能写拼音
    变量名，函数名，类名
"""
# 1name='bob'  报错
# print(name)

# classstudentcount = 100

# classStudentCount = 100
# 小驼峰

# ClassStudentCount = 100
# 大驼峰

# class_student_count = 100

"""
    字符串
"""
# name = 'sunny'
# name = "sunny"
# print("出一个'单引号")

# 原样输出字符串内容
# info="""
#     我喜欢打乒乓球
#     更喜欢你
# """
# print(info)

# print('sunny' + 1)

# 布尔类型
# IsMale = False
# print(IsMale)

"""
    定义变量保存心仪女孩的信息
"""
# name = '小芳'
# age = 18
# sex = '女'
# height = 165
# isMarry = False
# money = 100.0
# info = """
#     我喜欢你
# """
# print('她的名字叫',name,'今年',age,sex,height,isMarry,money,info)
# print(type(name),type(age),type(sex),type(height),type(isMarry),type(money),type(info))

'''
    运算符：加+减-乘*除/取模%幂**取整除//
'''

# a = 377
# b = 19
# print(a / b)
# print(a // b)
# print(a % b)
# print(a ** b)

"""
    比较运算符：==,!=,>,<,>=,<=
"""

# a=10
# b=20
# print(a>b)
# isFalse=a>b
# print(isFalse)
# print(a<=b)
# print(a!=b)
# print(a==b)

"""
    赋值运算符：=,+=,-=,*=,/=,%=,**=,//=
"""

# a = 10
# b = 20
# a+=b   # a=a+b
# print(a)

# a-=b   # a=a-b
# print(a)

# a*=b    # a=a*b
# print(a)

# a/=b    # a=a/b
# print(a)

# a%=b    #a=a%b
# print(a)

# a**=b     #a=a**b
# print(a)

# a//=b      #a=a//b
# print(a)

"""
    身份运算符：is ,is not    用于比较两个值的储存单元（内存地址）是否为同一个
"""
# name1='sunny'
# name2='sunny'
# print(id(name1))
# print(id(name2))
# print(name1 is name2)  #ture
# print(id(name1) is id(name2))  #false  id(name1)和id(name2)不是内存中的值

"""
    逻辑运算符：与或非 对象都是bool类型的数据  
"""

# a = True
# b = False
# print(a and b)
# print(a or b)
# print(not b)

"""
    短路：对and和or，第一个条件假或真决定and或or是否继续运算后面代码
"""

# num1 = 10
# num2 = 21
# print(num1 > num2 and 'hello')  #and前面条件为假  不继续运行
# print(num1 < num2 and 'hello')   #and前面条件为真  继续运行
# print(num1 > num2 or 'hello')   #or前面条件为假 继续运行
# print(num1 < num2 or 'hello')   #or前面条件为真  不继续运行

"""
    注：数字0，空的字符串，None,空列表，空元组，空字典等被作为False看待，其他数据作为Ture看待
"""

# print(1 and True and 'hello' and 0 and '张三')
# print([] or False or None or ' ' or "hello")

"""
    类型转换：将变量类型进行转换
"""

# 字符串转换为浮点数
# info = '100'
# print(float(info))

# 字符串转换为整数
# info = '100'
# print(int(info))

# 浮点数转换为整数
# info = 100.0
# print(int(info))

# 查看变量类型
# info = '100'
# print(type(info))

# 将整数转换为字符，（ASC||表对应的字符）
# print(chr(97))

# ord将字符转为整数,（按ASC||表对应）
# print(ord('A'))

"""
    十进制转换为二进制
"""
# print(bin(13))   #0b1101

"""
    输入两个数然后相加，例：10 20
"""
# num1 = input('请输入第一个数：')
# num2 = input('请输入第二个数：')
# print(num1)
# print(num2)
# print(type(num1))
# print(type(num2))
# num = num1 + num2   #1020  字符串相加
# num = int(num1) + int(num2)   #30   整数型相加
# print(num)

"""
    计算面馆销售额
    需求：通过键盘录入：每天卖出多少碗面
         通过键盘录入：每碗面多少钱
         通过键盘录入：今年共营业多少天
         计算并输出一年的总销售量
"""
# num1 = input('今天卖出多少碗面：')
# num2 = input('每碗面多少钱：')
# num3 = input('今年共营业多少天：')
# sum = float(num1) * float(num2) * float(num3)
# print('今年的总销售量为：', sum)

"""
    数字类型之间可以直接运算，有浮点数参与运算，结果为浮点数
"""

# price = 5.5
# num = 10
# print('收费：',price * num)

"""
    布尔类型和数字类型之间可以直接运算：Ture作为1，False作为0
"""
# b = True
# print(b + 10)

"""
    字符串之间用+来拼接成新的字符串
"""

# str1 = 'hello'
# str2 = 'world'
# print(str1+' '+str2)
# print(str1,end=' is ') #end='' 作用是不换行，且在‘’中的字符串放在后面
# print(str2)
# print(str1,str2,sep=' ')  #sep 作用是分割两个字符，且插入‘’中的字符串

# print('878*' * 10)  #输出多个重复的字符串

"""
    变量的格式化输出：如要输出文字信息的同时，一起输出变量中保存的数据，则要用到变量的格式化操作符
    
    格式化方式一：%-string
    %-string类型如下：
    %s 字符串                          %d 有符号的十进制整数 %06d表示输出的整数显示位数，不足的地方用0不全 如：000020
    %f 浮点数 %.2f表示小数点后只显示两位    %% 输出%
"""

# name = 'bob'
# age = 13
# money = 10000.123
# info = "我的名字是：%s,今年%05d岁了，有%.2f元钱"%(name,age,money)
# print(info)

"""
    格式化方式二: f-string
    f-string格式化
"""

# info = f"我的名字是：{name},今年{age}岁了，有{money}元钱"
# print(info)

"""
    例子：个人名片
    需求：提示用户输入（input）：姓名，公司，职位，电话，公司地址
"""
# name = input('请输入你的名字：')
# company = input('请输入你的公司：')
# position = input('请输入你的职位：')
# phoneNum =input('请输入你的电话：')
# companyAddress = input('请输入公司地址：')
# print('*'*30)
# print(f'姓名：{name} ',end='')
# print(' '*10,end='')
# print(f'电话：{phoneNum}')
# print(f'职位：{position}',end='')
# print(' '*10,end='')
# print(f'公司：{company}')
# print(f'公司地址：{companyAddress}')
# print('*'*30)

# name = input('请输入你的名字：')
# company = input('请输入你的公司：')
# position = input('请输入你的职位：')
# phoneNum =input('请输入你的电话：')
# companyAddress = input('请输入公司地址：')
# sep = '*'*40
# info = f"""
#     {sep}
#     姓名：{name}          电话：{phoneNum}
#     职位：{position}       公司：{company}
#     公司地址：{companyAddress}
#     {sep}
# """
# print(info)


"""
    条件语句：起判断作用
    需求：
    1.定义两个变量，分别记录年龄和性别
    2.如果满18岁，并且带有身份证，运行进入网吧上网    
"""

# age =14
# sex = '男'
# hasCard = True
# if age > 18 and hasCard:
#     print('我们是正规网吧')  #python用缩进来代表代码块，所以缩进要一致
# else:
#     print('请你离开')

"""
    案例：成绩分级
    需求：
    1.输入一个成绩。
    2.判断并提示成绩的等级（A,B,C,D,E）
        如果分数大于等于90为A，大于等于80为B，大于等于70为C，大于等于60为D，低于60为E。
"""
# Grade = input('请输入你的成绩：')
# Grade = float(Grade)
# if Grade >= 90:
#     print('A')
# elif Grade >= 80:
#     print('B')
# elif Grade >= 70:
#     print('C')
# elif Grade >= 60:
#     print('D')
# else:
#     print('E')
#
"""
    循环语句
    需求：假如使用代码给女朋友打100次我爱你。
"""
# i = 0
# while i < 100:
#     i += 1
#     print(f"我爱你{i}遍")

"""
    课堂练习：
    1.打印出1-100的值
    2.求解1-100的和
    3.求解1-100奇数的和
"""
# 求解1-100的值
# i = 1
# sum = 0
# while i <= 100:
#     sum = i + sum
#     i += 1
# print(sum)

# 求解1-100奇数的和
# i = 1
# sum = 0
# while i <= 100:
#     if i%2 == 1:
#         sum += i
#     i += 1
# print(sum)
