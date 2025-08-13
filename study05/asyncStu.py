import multiprocessing, queue
import time


def putTimeProcess(q: queue):
    while True:
        str = "process01" + time.ctime()
        q.put(str)
        time.sleep(2)


def getTimeProcess(q: queue):
    while True:
        get = q.get()
        print(f"获取到队列中的:{get}")


def process02(name, times):
    for i in range(times):
        print(f"process02 {name}")
        time.sleep(4)
        print(f"process02 {name} end")


def process03(name, times):
    for i in range(times):
        print(f"process03 {name}")
        time.sleep(4)
        print(f"process03 {name} end")


# 普通串行
def lineProcess():
    putTimeProcess()
    process02()
    process03()
    getTimeProcess


# 多进程
def asyncProcess():
    pro2 = multiprocessing.Process(target=process02, args=("测试进程 args", 3))
    pro3 = multiprocessing.Process(target=process03, kwargs={"name": "测试进程 kwargs", "times": 3})
    pro2.start()
    pro3.start()


    queue = multiprocessing.Queue()
    put = multiprocessing.Process(target=putTimeProcess,args=(queue,))
    get = multiprocessing.Process(target=getTimeProcess,args=(queue,))
    put.start()
    get.start()


if __name__ == '__main__':
    asyncProcess()
