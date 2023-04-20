"""
    多态:
    继承关系是实现多态的一种方式

"""
"""
案例:GirlFriend很喜欢学习，大学期间学习了很多的课程。Linux、AI、DABABASE、DataStructure等等
每学习一门课程 打印对应的内容...(如:正在学习Linux)

分析：
Linux:
    show_info():
        print("正在学习Linux")

AI:
    show_info():
        print(" ")


...

class Girlfriend:
    name
    * 
"""


# class Course:
#     def study(self):
#         print(f"正在学习...")
#
#
# class AI(Course):
#     def study(self):
#         print("正在学习AI")
#
#
# class Linux(Course):
#     def study(self):
#         print("正在学习Linux")
#
#
# class DateBase(Course):
#     def study(self):
#         print("正在学习DateBase")
#
#
# class DataStructure(Course):
#     def study(self):
#         print("正在学习DataStructure")
#
#
# class Girlfriend:
#     def study(self, course):
#         course.study()
#
#
# grilfriend = Girlfriend()
# ai = AI()
# grilfriend.study(ai)


"""
    需求：小孩，喜欢编程，找家教，要求：家教老师会编程
    老师：
    
    tutor
    
    student
        name
        行为：program 
            print ()  
    robot
        name
        行为：program
    
    Teacher
        name
        行为：program
        
    Child
        study(self, tutor)
        
             
"""

#
# class Tutor:
#     def teach(self):
#         print(f"正在教编程...")
#
#
# class Student(Tutor):
#     def __init__(self, name):
#         self.name = name
#
#     def teach(self):
#         print(f"{self.name}", end='')
#         super().teach()
#
#
# class Teacher(Tutor):
#     def __init__(self, name):
#         self.name = name
#
#     def teach(self):
#         print(f"{self.name}", end='')
#         super().teach()
#
#
# class Robot(Tutor):
#     def __init__(self, name):
#         self.name = name
#
#     def teach(self):
#         print(f"{self.name}", end='')
#         super().teach()
#
#
# class Child:
#     def __init__(self, name):
#         self.name = name
#
#     def study(self, tutor):
#         tutor.teach()
#         print(f"{self.name}正在学习...", end='')
#
#
# robot = Robot('Kay/O')
# child = Child('小王')
#
# child.study(robot)


"""
    
"""


# class Girlfriend:
#     # 和类绑定
#     # count = 0
#
#     def __init__(self, name):
#         self.name = name
#         # Girlfriend.count += 1
#         self.count = 0
#     # 类方法是和类绑定：正常情况下使用类名.方法名([参数列表])
#     # 实力对象也可以调用的原因是，当我们调用的时候会将对象所属的类传过去
#     @classmethod
#     def test(cls):
#         # Girlfriend ----cls
#         print('测试中...')
#
#     # 静态方法 没有和类以及对象绑定  可以访问
#     @staticmethod
#     def test2():
#         print("test2测试中")
#         pass
#
#     def __del__(self):
#         print('销毁了')
#
#
# girlfriend = Girlfriend('小王')
# girlfriend.count += 1
# print(girlfriend.count)
#
# girlfriend.test()
# Girlfriend.test()
# Girlfriend.test2()
# girlfriend.test2()


# class GirlFriend:
#     n = 0
#     def __init__(self, name, age):
#
#         self.name = name
# # 将字段年龄私有化之后， 外部不能够正常访问啦。怎么办?
# # 提供一种功能能够被外部正常访问。getAge()
#         if age < 0:
#             print('输入的年龄不合法')
#             age = 16
# # self.age = age
#         self.__age = age
#     pass
#
# # 提供get方法供外部访问
#     def getAge(self):
#         return self.__age
#
#
# girlfriend = GirlFriend('NIKE', 18)
# print(girlfriend.getAge())
# print(girlfriend.n)










# 随堂测试

# 需求:1:

# 商品类: Goods
#
# 具有成员变量,:
# 编号(code)
# 商品编号
# 名称(name)
# 商品名称
# 类别(type)
# 商品的具体类别
# 价格(price)
# 商品的价格
#
# 在魔术方法\__str__显示商品信息


# class Goods:
#     def __init__(self, code, name, type, price):
#         self.code = code
#         self.name = name
#         self.type = type
#         self.price = price
#
#     def __str__(self):
#         return f"商品编号：{self.code}\n商品名称：{self.name}\n商品类别：{self.type}\n商品价格：{self.price}"
#
#     pass
#
#
# goods = Goods(121, '绵长', 52, 25)
# print(goods)


# 需求2:

# 当父类的某个方法不适合子类本身的特征时，此时怎么办？
# 比如鸵鸟（Ostrich）是鸟类（Bird）中的一个特殊品种，所以鸵鸟类是鸟类的一
# 个子类，但是鸟类有飞翔的功能，但是对应鸵鸟，飞翔的行为显然不适合于它。
# 要求: 完善下面的代码
#
# ```python


# class Bird:
#     def fly(self):
#         print('飞啊飞.....')
#
#
# class Ostrich(Bird):
#     def __init__(self, isfly):
#         self.isfly = isfly
#
#     def fly(self):
#         if self.isfly:
#             super().fly()
#         else:
#             print('跑啊跑.....')
#
#     pass
#
#
# ostrich = Ostrich(False)
# # 飞啊飞.....
# ostrich.fly()


# #### 需求3:
#
# 使用面向对象的知识定义出老师（Teacher）、学生（Student）、员工（Employee）三个类：
# 老师：拥有名字、年龄、级别三个状态，有授课和休息两个功能
# 学生：拥有名字、年龄、学号三个状态，有学习和休息两个功能
# 员工：拥有名字、年龄、入职时间三个状态，有工作和休息两个功能
# 此时，发现三个类中的存在着大量的共同代码，而我们要考虑的就是如何解决代码重复的问题


# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def rest(self):
#         print(f"{self.name}正在休息...")
#
#
# class Teacher(Person):
#     def __init__(self, name, age, rank):
#         super().__init__(name, age)
#         self.rank = rank
#
#     def teach(self):
#         print(f"{self.name}正在授课...")
#
#
# class Student(Person):
#     def __init__(self, name, age, num):
#         super().__init__(name, age)
#         self.num = num
#
#     def study(self):
#         print(f"{self.name}正在上课...")
#
#
# class Employee(Person):
#     def __init__(self, name, age, time):
#         super().__init__(name, age)
#         self.time = time
#
#     def work(self):
#         print(f"{self.name}正在工作...")
#
#
# teacher = Teacher('王老师', 47, '教授')
# teacher.teach()
# teacher.rest()
# student = Student('小王同学', 18, '201909110505')
# student.study()
# student.rest()
# employee = Employee('小张', 24, '18年')
# employee.work()
# employee.rest()

# 需求4:

# 统计下面字符出现的次数

# letters = 'abcdabcdabcdabcefg'
#
# ```python
# 打印出下面的结构:
# a: 4
# b: 4
# c: 4
# ```
#
# letters = 'abcdabcdabcdabcefg'
# dic = {}
# for letter in letters:
#     if letter in dic:
#         dic[letter] += 1
#     else:
#         dic[letter] = 1
# for key, value in dic.items():
#     print(f"{key}:{value}")
#

