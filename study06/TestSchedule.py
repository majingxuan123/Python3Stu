#encoding=utf-8
##进入cmd   pip install schedule


import schedule
import time


def job():
    print(time.localtime(time.time()))

schedule.every(3).seconds.do(job)

while True :
    schedule.run_pending()
    time.sleep(1)
