"""
    文件：
        将内存中的数据持久化到磁盘中
    操作：
        open（）  文件路径  模式（w r a b w+ wb+ ab+)编码加上utf-8
        w：
        a+：seek（0）

    json:
        作为数据的交换

"""




# 异常处理
# with 可能产生异常的语句as：

# with open("") as file:
#     file.seek(0)
#     file.read()
#     file.close()
"""
try:

except:



try:

except:

else:

finally:

"""
#
# while True:
#     try:
#         x = int(input("请输入数字："))
#         break
#     except ValueError:
#         print("输入的不是数字")

# try:
#     j = input("请输入：")
#     i = 10 * (10 / int(j))
#     print("try执行完成")
# except ZeroDivisionError:
#     print("除数不能为零")
# except ValueError:
#     print("请输入数字：")
# else:
#     print("执行顺利")
# finally:
#     print("始终会执行")



"""
    多线程
"""

import time
import threading

#
# def display(count):
#     for i in range(1, count + 1):
#         print(i, end="")
#         time.sleep(1)
#
#
# print("主线程", threading.current_thread().name)
#
# for i in range(3):
#     s = threading.Thread(target=display, args=(5,))
#     print("子线程", s.name)
#     s.start()



# class MyThread(threading.Thread):
#     def __init__(self, name, count):
#         super(MyThread, self).__init__()
#         self.name = name
#         self.count = count
#
#     def run(self):
#         print("线程", self.name, "启动")
#         for i in range(1, self.count+1):
#             print(i,end="")
#             time.sleep(1)
#
#
# t1 = MyThread('t1', 5)
# t2 = MyThread('t2', 5)
# t3 = MyThread('t3', 5)
# t1.start()
# t1.join()
# t2.start()
#
# t3.start()
#
# print("当前线程名：", threading.current_thread().name)
# print("test6")

"""
    线程的阻塞
"""

"""
    线程同步和异步
"""
# import threading
# from threading import*
# threadLock = threading.Lock()
#
#
# class MyThread(Thread):
#     def run(self):
#         print("开启线程：", threading.current_thread().name)
#         threadLock.acquire()
#         for i in range(5):
#             print(threading.current_thread().name)
#         threadLock.release()
#
#
# t1 = MyThread()
# t2 = MyThread()
# t1.start()
# t2.start()


"""
    进程/线程
"""

# import threading
# print(threading.current_thread())
# print("hello")

"""
    


"""
import threading


# # 执行任务函数
# def task(*args):
#     # print('执行任务')
#     print(threading.current_thread())
#     pass
#
# # 创建线程
# # target 当前线程的任务
# # args 任务执行的时候传参
# # name 线程的名字
# thread01 = threading.Thread(target=task, args=('sunny', 18), name='thread-01')
# # 开启线程
# thread01.start()
#
# thread02 = threading.Thread(target=task, args=('bob', 18), name='thread-02')
# # 开启线程
# thread02.start()
# print(thread02.is_alive())
# print(thread02.native_id)
# print(thread02.name)

"""
    自定义线程
"""


# class MyThread(threading.Thread):
#     def run(self):
#         # 当前线程执行的任务
#         print(threading.current_thread())
#         pass
# # 创建线程
#
#
# th = MyThread()
# th.setName('thread-1008611')
# # 开启线程
# th.start()
#
# for num in range(5):
#     th = MyThread()
#     th.setName(f'thread-{num}')
#     # 开启线程
#     th.start()
#     pass

"""
    买票案例
"""
import time
# 储存100张票
ticket = 100
# 创建锁
lock = threading.RLock()


class MyThread(threading.Thread):
    # 线程执行的任务  当前是卖票
    def run(self):
        global ticket
        # 当票数大于的时候卖票
        while ticket > 0:
            lock.acquire()
            if ticket < 1:
                return
            ticket -= 1
            time.sleep(0.1)
            name = threading.currentThread().getName()
            print(f"{name}卖了1张票，还剩{ticket}张")
            lock.release()
    pass

for num in range(5):
    th = MyThread()
    th.setName(f'th-{num}')
    # 开启线程
    th.start()
    pass




