#encoding=utf-8

import threading
import time


def sayhi(threadName,delay):  #定义每个线程要运行的函数
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print("%s: %s" % (threadName, time.ctime(time.time())))

if __name__ == "__main__":

    t1 = threading.Thread(target=sayhi,args=("Thread-1",2,)) #生成一个线程实例
    t2 = threading.Thread(target=sayhi,args=("Thread-2",2,)) #生成另一个线程实例

    t1.start()  #启动线程
    t2.start()
    # print(t1.getName()) #获取线程名
    # print(t2.getName())
    t1.join()  #阻塞主线程，等待t1子线程执行完后再执行后面的代码
    t2.join()  #阻塞主线程，等待t2子线程执行完后再执行后面的代码
    print('-----end')