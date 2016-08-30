import threading

import time


# def loop():
#     print("thread %s is running..." % threading.current_thread().name)
#     n = 0
#     while n < 5:
#         n += 1
#         print("thread %s >>> %s" % (threading.current_thread().name, n))
#         time.sleep(1)
#     print("thread %s ended" % threading.current_thread().name)
#
#
# print('thread %s is running...' % threading.current_thread().name)
# # 启动西纳城传入函数loop,命名该子线程名称为LoopThread
# t = threading.Thread(target=loop, name="LoopThread")
# t.start()
# t.join()
# print('thread %s ended.' % threading.current_thread().name)

# 看看多个线程同时操作一个变量怎么把内容给改乱了
balance = 0
lock = threading.Lock()


def change_it(n):
    # 先存后取,结果应为0
    global balance
    balance = balance + n
    balance = balance - n


def run_thread(n):
    for i in range(100000):
        # 获取锁
        lock.acquire()
        try:
            change_it(n)
        finally:
            # 释放锁
            lock.release()

t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)


