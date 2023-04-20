# from 模块名 import 模块中的部分（name1， name2）
# from hand import Hand, Point
import hand


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        # self.hand = Hand()
        self.hand = hand.Hand()
        pass


point1 = hand.Point(100, 200)
point2 = hand.Point(200, 300)