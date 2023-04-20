import matplotlib.pyplot as plt
import random

# 折线图
# x = [i for i in range(100)]
# print(len(x))
# y = [random.randint(0, 10) for i in range(100)]
# print(len(y))
# plt.plot(x, y)
# plt.show()

# 饼状图
# plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
# data = [0.2515, 0.3724, 0.3336, 0.0368, 0.0057]
# labels = ['美国', '中国', '英国', '法国', '荷兰']
# plt.pie(x=data, labels=labels)
# plt.show()

# 散点图
# x = [2, 8, 7, 4, 4, 1, 4, 2, 9]
# y = [5, 4, 3, 2, 6, 7, 8, 9, 2]
# plt.scatter(x, y)
# plt.savefig("4.jpg")
# plt.show()

# 柱状图
# plt.rcParams['font.sans-serif'] = ['SimHei']
# plt.rcParams['font.size'] = 50
# plt.rcParams['axes.unicode_minus'] = False
# plt.figure(figsize=(20, 8), dpi=10)
# movie_name = ['雷神3：诸神黄昏', '正义联盟', '东方快车谋杀案', '寻梦环游记','全球风暴', '降魔传', '追捕', '七十七天', '密战', '狂兽', '其它']
# x = range(len(movie_name))
# y = [73853, 57767, 22354, 15969, 14839, 8725, 8716, 8318, 7916, 6764, 52222]
# plt.bar(x, y, width=0.5, color=['b', 'r', 'g', 'y', 'c', 'm', 'y', 'k', 'c', 'g', 'g'])
# plt.xticks(x, movie_name)
# plt.savefig("柱状图1.jpg")
# plt.show()


"""
1、用饼图统计信息工程学院女生和男生的人数；
2、用柱图分析语文成绩优、良、中、差的人数；
3、利用散点图分析语文和英语成绩的相关性；
4、利用折线图分析学生年龄和数学平均成绩的走势图
"""
students = [{'name': '张三', 'gender': 'male', 'age': 18, 'class': 'class1', 'chinese': 80, 'math': 90, 'english': 85},
            {'name': '李四', 'gender': 'male', 'age': 16, 'class': 'class2', 'chinese': 70, 'math': 85, 'english': 80},
            {'name': '王五', 'gender': 'female', 'age': 15, 'class': 'class3', 'chinese': 90, 'math': 95, 'english': 90},
            {'name': '赵六', 'gender': 'female', 'age': 17, 'class': 'class4', 'chinese': 75, 'math': 80, 'english': 85},
            {'name': '钱七', 'gender': 'male', 'age': 18, 'class': 'class1', 'chinese': 85, 'math': 90, 'english': 80},
            {'name': '孙八', 'gender': 'male', 'age': 19, 'class': 'class2', 'chinese': 90, 'math': 95, 'english': 95},
            {'name': '周九', 'gender': 'female', 'age': 18, 'class': 'class3', 'chinese': 80, 'math': 85, 'english': 80},
            {'name': '吴十', 'gender': 'female', 'age': 17, 'class': 'class4', 'chinese': 70, 'math': 75, 'english': 70},
]
# 1、用饼图统计信息工程学院女生和男生的人数；
# plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
# data = [0, 0]
# labels = ["女生", "男生"]
# for stu in students:
#     if stu.get("gender") == 'male':
#         data[1] += 1
#     else:
#         data[0] += 1
# plt.pie(x=data, labels=labels)
# plt.show()

# 2、用柱图分析语文成绩优、良、中、差的人数；
# plt.rcParams['font.sans-serif'] = ['SimHei']
# plt.rcParams['font.size'] = 100
# plt.rcParams['axes.unicode_minus'] = False
# plt.figure(figsize=(80, 20), dpi=10)
# labels = ["优", "良", "中", "差"]
# x = range(len(labels))
# y = [0, 0, 0, 0]
# for stu in students:
#     if stu.get("chinese") >= 90:
#         y[0] += 1
#     elif stu.get("chinese") >= 80:
#         y[1] += 1
#     elif stu.get("chinese") >= 60:
#         y[2] += 1
#     else:
#         y[3] += 1
# plt.bar(x, y)
# plt.ylabel("人数")
# plt.title("语文成绩")
# plt.xticks(x, labels, color='red')
# plt.show()

# 3、利用散点图分析语文和英语成绩的相关性；
# plt.rcParams['font.sans-serif'] = ['SimHei']
# scoreChinese = []
# scoreEnglish = []
# names = []
# for stu in students:
#     scoreChinese.append(stu.get("chinese"))
#     scoreEnglish.append(stu.get("english"))
#     names.append(stu["name"])
# plt.scatter(names, scoreChinese)
# plt.scatter(names, scoreEnglish)
# plt.show()

# 4、利用折线图分析学生年龄和数学平均成绩的走势图
# plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
# ageStu = sorted(list(set([stu["age"] for stu in students])))
# dicStu = {}
# for x in ageStu:
#     dicStu[x] = []
# for stu in students:
#     dicStu[stu["age"]].append(stu["math"])
# print(dicStu)
# scoreMath = []
# for key, value in dicStu.items():
#     if len(value) == 1:
#         scoreMath.append(value[0])
#     else:
#         scoreMath.append((sum(value)/len(value)))
# plt.plot(ageStu, scoreMath)
# plt.xticks(ageStu)
# plt.show()



















