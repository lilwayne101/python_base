# import random
# codes = "1234567890ASD"\
#         "asdjldjfkdfalkdjn"
# print("".join(random.sample(codes, 6)))


"""
    字符串的连接方法：join（）和 split（）
"""
import json
import re

# s = ""
# join() 连接的元素必须是字符串
# print("".join(['1', '2', '3', '4', '5', '6']))
# split
# I = 'a-b-c-d'.split('-b')
# print(I)

"""
    词频统计
要求：
1.输入一段中文， 统计每个字出现的次数
"""

# from collections import Counter
#
# words = input("请输入一段文字：")
# result = Counter(words)
# print(result)

"""
    字典实现英文单词词频统计
"""
# words = "Apple is my Apple"
# word = words.split(" ")
# print(word)
# dic = {}
# for w in word:
#     if w in dic:
#         dic[w] += 1
#     else:
#         dic[w] = 1
# print(dic)

"""
    词云图
"""

# from pyecharts import options as opts
# from pyecharts.charts import Page, WordCloud
#
# words = [("Python", 100), ("C#", 90), ("java", 80), ("PHP", 50), ("JS", 60), ("C", 65)]
#
#
# def wordcloud():
#     return WordCloud().add("", words, word_size_range=[20, 100], shape='cardioid')\
#         .set_global_opts(title_opts=opts.TitleOpts(title=""))
#
# wordcloud().render("wordcloud.html")

"""
    样本随机抽样
    1.从100个样本中随机抽样10个（无重复）
"""
# from random import randint, sample, shuffle
#
# Ist = [randint(50, 150) for i in range(100)]
# # sample 无重复随机抽样
# Ist_sample = sample(Ist, 10)
# # 重洗数据集，就地随机打乱位置，节约资源
# shuffle(Ist)
# print(Ist_sample)

"""
    对象序列化
    对象序列化：将内存中的对象转化为可存储或传输的过程，接口间的调用或web请求，一般使用json传输
"""
# import json
#
# class Product:
#     def __init__(self, name, price, address):
#         self.name = name
#         self.price = price
#         self.address = address
#
#
# p1 = Product("Apple", 9000, "河南")
# p2 = Product("华为", 8299, "深圳")
#
# # json 是文本文件
# with open("1.json", 'w', encoding='utf-8') as file:
#     json.dump([p1, p2], file, default=lambda obj:obj.__dict__, ensure_ascii=False, indent=2, sort_keys=True)

"""
    10.对密码进行加密传输
"""
# import hashlib
# # 对密码实现32位加密存储
# def password_hash(s):
#     m = hashlib.md5()
#     m.update(str(s).encode('utf-8'))
#     return m.hexdigest()
# print(password_hash("12346"))#a3590023df66ac92ae35e3316026d17d

"""
    turtle模块绘制奥运五环
    turtle包用于描绘绘图轨迹，使用该模块绘制奥运五环，先绘制一个环，主要坐标，颜色，半径
"""
# import turtle as p
#
#
# def drawCircle(x, y, c):
#     p.pu()#抬起画笔
#     p.pensize(5)#画笔粗细
#     p.goto(x, y)#坐标
#     p.pd()#放下画笔
#     p.color(c)#颜色
#     p.circle(30, 360)#半径，角度
#
#
# drawCircle(0, 0, "red")
# drawCircle(60, 0, "yellow")
# drawCircle(120, 0, "blue")
# drawCircle(30, -30, "brown")
# drawCircle(90, -30, "black")

"""
    13。qrcode模块生成二维码
"""

# import qrcode
# img = qrcode.make("http://www.baidu.com")
# img.save("baidu.jpg")

"""
    爬虫
    采集器的功能和实现
"""

# import requests
# # 采集器
#
#
# def get_page(url):
#     headers = {
#         'User-Agent': 'Mozilla/5.0(Windows NT 6.1)AppleWebKit/537.36(KHTML,like Gecko)'
#                       'Chrome''/75.0.3770.142''Safari/537.36'}
#     response = requests.get(url, headers=headers)
#     if response.status_code == 200:
#         return response.text
#     else:
#         return "爬取异常"
#
#
# txt_list = get_page('https://s.taobao.com/search?q=%E8%8B%B9%E6%9E%9C&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.jianhua.201856-taobao-item.2&ie=utf8&initiative_id=tbindexz_20170306')
# f = open('1.txt', 'w', encoding="utf-8")
# f.write(txt_list)

"""
    解析器：对html代码过滤筛选
"""
"""
    正则表达式
"""

# 正则表达式（点号）
# import re
# x = 'errerer3r2r34234hu3h4i837h4f83h479h4f93423g4fy34h342h34'
# print(re.findall('er.', x))# ['err', 'ere']

# 正则表达式（问号）：前一个字符存在或者不存在
# import re
# x = 'errerer3r2r34234hu3h4i837h4f83h479h4f93423g4fy34h342h34'
# print(re.findall('r3?', x)) # ['r', 'r', 'r', 'r3', 'r', 'r3']

# 正则表达式 点星组合（.*）贪婪算法：尽可能多的匹配数据 返回的列表只有一个元素
# import re
# x = 'errerer3r2r34234hu3h4i837h4f83h479h4f93423g4fy34h342h34'
# print(re.findall('r3.*h3', x))  # ['r3r2r34234hu3h4i837h4f83h479h4f93423g4fy34h342h3']

# 正则表达式（.*?非贪婪算法）
# 点星问组合(.*?):非贪婪算法，尽可能少的匹配数据
# import re
# x = 'errerer3r2r34234hu3h4i837h4f83h479h4f93423g4fy34h342h34'
# print(re.findall('h.*?h', x))  # ['hu3h', 'h4f83h', 'h4f93423g4fy34h']


# 正则表达式（圆括号()）
# import re
# x = '<img scr="http://www.baidu.com/images/1.jpg"/>'
# print(re.findall('scr="(.*?)"/>', x))  # ['http://www.baidu.com/images/1.jpg']


# 下载某个网页上的所有图片
import re
import requests
# 采集器


def get(url):
    headers = {
        'User-Agent': 'Mozilla/5.0(Windows NT 6.1)AppleWebKit/537.36(KHTML,like Gecko)'
                      'Chrome''/75.0.3770.142''Safari/537.36'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response
    else:
        return "爬取异常"


txt_list = get('https://www.sohu.com/').text
f = open('page.txt', 'w', encoding='utf-8')
f.write(txt_list)

x = re.findall(r'img src="(.*?)\.jpeg"', txt_list)
i = 1
for ele in x:
    with open('pic\\'+str(i)+'.jpg', 'wb') as jpg:
        jpg.write(get(ele).content)
    i += 1








