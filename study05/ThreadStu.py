import threading
import time
from threading import Thread

def eat():
    for i in range(1, 4):
        time.sleep(1)
        print("吃吃吃")

def drink():
    for i in range(1, 4):
        time.sleep(1)
        print("喝喝喝")


list = {1,2,3,4,5,6,7,8,9,10}
# 上锁
lock = threading.Lock()

def sellTicket1():
    global list
    while True:
        time.sleep(0.26)
        if len(list) <= 0:
            break
        lock.acquire_lock()
        pop = list.pop()
        print(f"卖第{pop}位置的票")
        lock.release_lock()
def sellTicket2():
    global list
    while True:
        time.sleep(0.2)
        if len(list) <= 0:
            break
        lock.acquire_lock()
        pop = list.pop()
        print(f"卖第{pop}位置的票")
        lock.release_lock()


if __name__ == '__main__':
    # eatThread = Thread(target=eat)
    # drinkThread = Thread(target=drink)
    # drinkThread.start()
    # eatThread.start()

    thread1 = Thread(target=sellTicket1)
    thread2 = Thread(target=sellTicket2)
    thread1.start()
    thread2.start()
