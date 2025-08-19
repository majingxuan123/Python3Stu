import threading
import time
from multiprocessing.pool import ThreadPool
from random import random

class MyTestThread(threading.Thread):
    def run(self):
        t_start = time.time();
        print("线程任务开始了！")
        time.sleep(3)
        t_stop = time.time();
        print(f"线程结束了！ 耗时:{t_stop-t_start}")


def testWorker(msg):
    t_start = time.time();
    print(f"线程任务开始了！:{msg}")
    time.sleep(3)
    t_stop = time.time();
    print(f"线程结束了！ 耗时:{t_stop - t_start}   msg:{msg}")

if __name__ == '__main__':
    pool = ThreadPool(4)
    # for i in range(10):
    #     pool.apply_async(MyTestThread().run)

    for i in range(5):
        pool.apply_async(testWorker, args=("测试",))


    print("___________ start __________")
    pool.close()
    pool.join()
    print("____________ end ___________")

