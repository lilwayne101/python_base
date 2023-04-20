"""
    friend：
    特点：黑头发，黄皮肤，性别，年龄
        爱好（hobby）


    类：
    抽象（不具体）是一个模板

    对象：
    年龄：18
    姓名：lilwayne
    身份证； **********


    特点：
    具体，通过模板创建出来的

    类的声明：
    class 类名：
        成员属性***
        成员方法

"""

# class GirlFriend:
#     #初始化方法
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         # print('被创建啦')
#         pass
#
#     #成员方法
#     def hobby(self, msg):
#         print(f"爱好看电影{msg}")
#         # print(id(self))
#         pass
#
#     def show_info(self):
#         print(f"姓名是：{self.name} 年龄是：{self.age}")
#
#     def __str__(self):
#         return f"姓名是：{self.name} 年龄是：{self.age}"
#

# 找到朋友 创建对象
# 创建对象 变量名 = 类名()
# 创建对象 类名([参数列表])
# 创建对象时，会调用_init_(self, name, age)
# girlFriend = GirlFriend('小王',19)
# girlFriend.hobby('很开心')
# print(girlFriend)
# 添加属性，对象.属性名=值
# girlFriend.name = '张伟'
# girlFriend.age = 18
# print(f"姓名是：{girlFriend.name},年龄是:{girlFriend.age}")

"""
    类的练习
"""

# class Stu:
#     def __init__(self, name, height, age=16):
#         self.name = name
#         # 加__ 使属性私有化，外部无法访问
#         # 提供一种可以供外部访问的功能（方法）
#         self.__age = age
#         self.height = height
#
#     def get_age(self):
#         return self.__age
#
#     def stu_msg(self):
#         print(f"姓名：{self.name}，年龄:{self.__age},身高：{self.height}")
#
#     def study_age(self, stu_age):
#         if stu_age > 4:
#             print("该学生大学毕业")
#         else:
#             print("该学生是在校生")
#
#     def __str__(self):
#         return f"姓名：{self.name}，年龄:{self.__age},身高：{self.height}"


# stu = Stu("小王", 18, 188)
# # stu.stu_msg()
# # stu.study_age(4)
# print(stu)

"""
    封装的作用:保证数据的安全性
"""

# stu = Stu('小王', 160, 18)
# stu.stu_msg()
# print(f"姓名：{stu.name}，年龄:{stu.get_age()},身高：{stu.height}")


"""
    继承：
    作用：1.简化代码
         2.当父类的功能不满足子类的要求时，可以扩展
    案例2: 定义一个狗类，继承自动物类，定义一个猫类，继承自动物类。动物类有方法makeSound,Dog类和Cat类分别继承Animal类.
    并覆写父类的方法makeSound
    分析：
    类：动物类
            class animal：
                def makeSoundDog():
                
                
"""

# class Animal:
#     def __init__(self, name):
#         self.name = name
#         pass
#
#     def make_sound(self):
#         print("叫")
#         pass
#
#
# """
#     因为Dog和Cat有相同的属性和方法，抽取到Animal类中，创建父类
#
#     class 子类（父类）
#         ......
# """
#
#
# class Dog(Animal):
#
#     def __init__(self, name):
#         super().__init__(name)
#
#     """
#         重写父类的方法：方法名和参数保持一致----->直接把父类的方法拷贝在子类即可，然后做拓展
#     """
#     def make_sound(self):
#         super().make_sound()
#         print(f"{self.name} wool!")
#
#
# class Cat(Animal):
#     def __init__(self, name):
#         super().__init__(name)
#
#     def make_sound(self):
#         super().make_sound()
#         print(f"{self.name} miao!")
#
#
# dog = Dog('旺财')
# # 如果子类继承父类，父类里面的成员变量和方法子类也会拥有
# # 如果子类重写父类的方法，就会调用子类的方法
# dog.make_sound()
# cat = Cat('汤姆')
# cat.make_sound()


"""
    案例1:GirlFriend有很多爱好，现在她的闺蜜(HoneyFriend) 和 她的BoyFriend陪她一起学习，或者看电影
    分析：
        class GirlFriend
            study()
            watch_film()
            
        class HoneyFriend(GirlFriend)
             
        class BoyFriend(GirlFriend)
        
"""

# class Friend:
#     def __init__(self, name):
#         self.name = name
#
#     def study(self):
#         print(f"{self.name}正在学习。。。")
#
#     def film(self):
#         print(f"{self.name}正在看电影。。。")
#
#
# class HoneyFriend(Friend):
#     def __init__(self, name):
#         super().__init__(name)
#     pass
#
#     def study(self):
#         super().study()
#         print(f"{self.name}很开心")
#
#     def film(self):
#         super().film()
#         print(f"{self.name}很开心")
#
#
# class BoyFriend(Friend):
#     def __init__(self, name):
#         super().__init__(name)
#     pass
#
#     def study(self):
#         super().study()
#         print(f"{self.name}很开心")
#
#     def film(self):
#         super().film()
#         print(f"{self.name}很开心")
#
#
# class Girlfriend:
#     def __init__(self, name):
#         self.name = name
#
#     def study_with(self, friend):
#         friend.study()
#         print(f"{self.name}和{friend.name}正在学习。。。")
#
#     def film_with(self, friend):
#         friend.film()
#         print(f"{self.name}和{friend.name}正在看电影。。。")
#
#
# girlfriend = Girlfriend("女朋友")
# honeyFriend = HoneyFriend("女朋友的闺蜜")
# boyfriend = BoyFriend("女闺蜜的男朋友")
# # honeyFriend.study()
# # honeyFriend.film()
# # boyfriend.study()
# # boyfriend.film()
# girlfriend.study_with(honeyFriend)
# girlfriend.film_with(honeyFriend)


"""
    课后练习：
    2、创建一个手机类。手机属性有 颜色, 屏幕大小，价格，品牌, 创建一个对象打印信息
"""

# class Phone:
#     def __init__(self, color, screen_size, price, brand):
#         self.color = color
#         self.screen_size = screen_size
#         self.price = price
#         self.brand = brand
#         pass
#
#     def info(self):
#         print(f"该手机的颜色是：{self.color},屏幕大小为：{self.screen_size},价格为:{self.price},品牌为：{self.brand}")
#
#
# phone = Phone('白色', '50寸', '500', '人革联')
# phone.info()

"""
    3、学生信息
    1) 封装Student类，包含属性name、age、tel、score、sex，包含方法getScore(打印name、score)、 getStudent（打印个人的全部信息）。
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
#         pass
#
#     def get_score(self):
#         print(f"name：{self.name}  score：{self.score}")
#
#     def get_student(self):
#         print(f"name：{self.name} age:{self.age} tel:{self.tel} score：{self.score} sex:{self.sex} ")
#         pass
#
#
# listStu = [Student('小赵', '18', '12345', 80, '男'),
#            Student('小钱', '18', '12345', 70, '男'),
#            Student('小孙', '18', '12345', 60, '男'),
#            Student('小李', '18', '12345', 50, '男'),
#            Student('小周', '18', '12345', 40, '男'),
#            Student('小吴', '18', '12345', 30, '女'),
#            Student('小孙', '18', '12345', 20, '女'),
#            Student('小王', '18', '12345', 90, '女'),
#            Student('小马', '18', '12345', 86, '女'),
#            Student('小毛', '18', '12345', 53, '女')]
#
# for i in range(len(listStu)):
#     listStu[i].get_student()
# count_stu = 0
# print("不及格的同学有：")
# for i in range(len(listStu)):
#     if listStu[i].score < 60:
#         listStu[i].get_student()
#         count_stu += 1
# print(f"不及格人数为：{count_stu}")

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
#     def __init__(self, name, age, weapon, rank, understanding):
#         self.name = name
#         self.age = age
#         self.weapon = weapon
#         self.rank = rank
#         self.understanding = understanding
#
#     def info_print(self):
#         print(f"人物:{self.name}  年龄:{self.age}  武器:{self.weapon}  等级:{self.rank}  悟性:{self.understanding}")
#
#     def buddha(self, times):
#         self.rank += times
#         print(f"{self.name}念佛{times}次,已升{times}级，目前等级:{self.rank}")
#
#     def do_pilgrimage(self, times):
#         self.understanding += times
#         print(f"{self.name}进行{times}次取经经,成功增加{times}点悟性，目前悟性:{self.understanding}")
#
#     def fight(self, combat_power):
#         if (self.rank + (self.understanding * int(str(list(self.weapon.values())[0])))) > combat_power:
#             print(f"战斗胜利！{self.name}获得{combat_power}点经验！")
#             if combat_power > 10:
#                 self.rank += int (combat_power/10)
#                 print(f"成功升了{int(combat_power/10)}级，目前等级：{self.rank}")
#             else:
#                 print("经验值过少，已逸散。")
#     pass
#
#
# class SunWuKong(Prentice):
#     def __init__(self, name, age, weapon, rank, understanding, formula):
#         super().__init__(name, age, weapon, rank, understanding)
#         self.formula = formula
#
#     def do_maigre(self, times):
#         self.rank += times
#         print(f"{self.name}吃斋{times}次,已升{times}级，目前等级:{self.rank}")
#
#     def ext_devil(self, devil):
#         if devil <= self.rank:
#             print("成功降妖！")
#         else:
#             self.rank -= 1
#             print(f"降妖失败！等级降低1级，目前等级：{self.rank}")
#     pass
#
#
# class ZhuBaJie(Prentice):
#     def __init__(self, name, age, weapon, rank, understanding, wife):
#         super().__init__(name, age, weapon, rank, understanding)
#         self.wife = wife
#
#     def hold_horse(self, horse):
#         print(f"猪八戒牵着{horse}，马上坐着猪八戒的老婆:{self.wife}")
#
#
# class ShaSeng(Prentice):
#     def __init__(self, name, age, weapon, rank, understanding, sand_river):
#         super().__init__(name, age, weapon, rank, understanding)
#         self.sand_river = sand_river
#
#     def pick_up_luge(self):
#         print(f"沙僧从{self.sand_river}上岸，就开始挑行李")
#
#
# Westbound_team = [SunWuKong('孙悟空', 750, {'金箍棒': '15'}, 1, 3, '紧箍咒'),
#                   ZhuBaJie('猪八戒', 1500, {'九齿钉耙': '10'}, 1, 2, '高翠兰'),
#                   ShaSeng('沙僧', 1430, {'月牙铲': '8'}, 1, 2, '流沙河')]
#
# for i in range(len(Westbound_team)):
#     Westbound_team[i].info_print()
#
# for i in range(len(Westbound_team)):
#     Westbound_team[i].buddha(1)
#
# for i in range(len(Westbound_team)):
#     Westbound_team[i].do_pilgrimage(1)
#
# for i in range(len(Westbound_team)):
#     Westbound_team[i].fight(20)
#
# Westbound_team[0].do_maigre(1)
# Westbound_team[0].ext_devil(2)
# Westbound_team[1].hold_horse('白龙马')
# Westbound_team[2].pick_up_luge()

"""
1. 你和你的女朋友今天准备出去玩：你的男朋友说要出去看电影，女朋友说要学习。
怎么办? 剪刀石头布游戏 3局两胜。请最后显示 获胜的是哪一方?
分析：class Game
        name1
        name2
        times_win
        
        def play()
            num1,num2 = 0
            while 1 == 1
                str1 = input()
                str2 = input()
                if str1 == str2
                    print(平局)
                elif str1 == '石头' 
                    if str2 == '布'
                    
                    else：
                    print（）
                    num1 += 1
                elif str1 == '布' 
                    if str == ’石头‘
                    else：
                
                
                    
                    print（）
                    num2 += 1
"""


# class Game:
#     def __init__(self, player1, player2, times_win):
#         self.player1 = player1
#         self.player2 = player2
#         self.times_win = times_win
#
#     def play(self):
#         num1 = num2 = 0
#         while 1 == 1:
#             str1 = input(f"{self.player1}请出招：")
#             str2 = input(f"{self.player2}请出招：")
#             if str1 == str2:
#                 print('平局！')
#             elif str1 == '石头':
#                 if str2 == '布':
#                     num2 += 1
#                     print(f"{self.player2}获胜，目前比分{num1}:{num2}")
#                 else :
#                     num1 += 1
#                     print(f"{self.player1}获胜，目前比分{num1}:{num2}")
#             elif str1 == '布':
#                 if str2 == '石头':
#                     num1 += 1
#                     print(f"{self.player1}获胜，目前比分{num1}:{num2}")
#                 else:
#                     num2 += 1
#                     print(f"{self.player2}获胜，目前比分{num1}:{num2}")
#             elif str2 == '布':
#                 num1 += 1
#                 print(f"{self.player1}获胜，目前比分{num1}:{num2}")
#             else:
#                 num2 += 1
#                 print(f"{self.player2}获胜，目前比分{num1}:{num2}")
#
#             if num1 == self.times_win:
#                 return print(f"{self.player1}获胜!")
#             elif num2 == self.times_win:
#                 return print(f"{self.player2}获胜!")
#
#
# game = Game('男朋友', '女朋友', 2)
# game.play()

"""
2. 人体关键点的描述
1) 人有姓名、年龄。根据下面的图形还有很多的关键点landmarks。每一个关键点的描述使用 x, y去描述。
要求:
创建关键点(创建3个即可), 给person人添加关键点之后。遍历每一个关键点
2) 人体关键点的描述 plus版本 扩展:
plus版本:
增加描述人体的：眼部关键点、手部关键点。(分别创建3个即可),然后分别遍历 眼部 和 手部关键点
"""


# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
#
# class Organ:
#     def __init__(self, name_organ):
#         self.name_organ = name_organ
#         self.organ_point = []
#
#     def organ_landmarks_input(self, nums):
#         for i in range(nums):
#             self.organ_point[i] = input(f"请输入{self.name_organ}的关键点：")
#             print(f"{self.name_organ}的关键点输入完成！")
#         return self.organ_point
#
#     def organ_landmarks_print(self):
#         for ele, index in enumerate(self.organ_point):
#             print(f"{self.name_organ}的第{index + 1}个关键点是：{ele}")
#         print(f"{self.name_organ}的关键点全部放出！")
#
#
# class Eyes(Organ):
#     def __init__(self, name_organ):
#         super().__init__(name_organ)
#
#
# class Hands(Organ):
#     def __init__(self, name_organ):
#         super().__init__(name_organ)
#
#
# class Person:
#     def __init__(self, name, age, *organ):
#         self.organ = organ
#         self.name = name
#         self.age = age
#         self.landmarks = []
#
#
#     def print_landmarks(self):
#         for i in range(len(self.organ.organ_point)):
#             self.landmarks = self.organ.organ_point
#
#
#     def hand_landmarks(self, hand):
#
#
#
#
# person = Person('小王', 18, [])
#


"""
3、JD商城，商城下面有很多的店铺(3个)， 店铺下面有很多的商品(3个)
分析:
商城--->多个店铺
店铺下面--->多个商品
要求：遍历商城下面的店铺 以及店铺下面的商品
"""


# class Shop:
#     def __init__(self, goods, shop_name):
#         self.shop_name = shop_name
#         self.goods = goods
#
#     def traverse_goods(self):
#         for index, ele in enumerate(self.goods):
#             print(f"{ele}", end=' ')
#         print()
#
#
# class Mall(Shop):
#     def __init__(self, shop_name, goods):
#         super().__init__(goods, shop_name)
#         self.shop_name = shop_name
#
#     def traverse_shop(self):
#         print(f"商城内的店铺有：",end='')
#         for i in range(len(self.shop_name)):
#             print(f"{self.shop_name[i]}", end=' ')
#         print()
#         temp_goods = self.goods
#         for index, ele in enumerate(self.shop_name):
#             self.goods = temp_goods[index]
#             print(f"{self.shop_name[index]}的店里有：", end='')
#             super().traverse_goods()
#
#
# mall = Mall(['华为', '小米', '苹果'],
#             [['华为手机', '华为平板', '华为耳机'],
#             ['小米手机', '小米平板', '小米耳机'],
#              ['苹果手机', '苹果平板', '苹果耳机']])
# mall.traverse_shop()


# class Mall:
#     def __init__(self, sn, name):
#         self.sn = sn
#         self.name = name
#         self.shop_list = []
#
#
# class Shop:
#     def __init__(self, sn, shop_name):
#         self.sn = sn
#         self.shop_name = shop_name
#         self.goods_list = []
#
#
# class Goods:
#     def __init__(self, sn, goods_name, price, goods_type):
#         self.sn = sn
#         self.goods_name = goods_name
#         self.price = price
#         self.good_type = goods_type
#
#     def goods_print(self):
#         print(f"编号：{self.sn}  商品名：{self.goods_name}  单价：{self.price}  品类：{self.good_type}")
#         return 0
#
#
# xmGoodS = Goods('001', '小米10', '1120元', '手机')
# hwGoodS = Goods('002', '华为10', '5220元', '手机')
# mzGoodS = Goods('003', '魅族10', '2220元', '手机')
#
#
# xmShop = Shop('001', '小米手机店')
# hwShop = Shop('002', '华为手机店')
# mzShop = Shop('003', '魅族手机店')
#
# xmShop.goods_list.append(xmGoodS)
# hwShop.goods_list.append(hwGoodS)
# mzShop.goods_list.append(mzGoodS)
#
# jdMall = Mall('001', '京东商城')
# jdMall.shop_list.append(xmShop)
# jdMall.shop_list.append(hwShop)
# jdMall.shop_list.append(mzShop)
#
# for shop in jdMall.shop_list:
#     print(f"商城编号：{jdMall.sn}，商城名：{jdMall.name}", end=' ')
#     print(f"{shop.shop_name}：", end='')
#     shop.goods_list[0].goods_print()










