import threading
from multiprocessing.pool import ThreadPool

import okx.MarketData as MarketData
import time
from datetime import datetime

import pymysql

from okxtest.MySqlUtil.MySqlUtil import MySqlUtil

flag = "0"  # 实盘:0 , 模拟盘：1
marketDataAPI = MarketData.MarketAPI(flag=flag)


# 获取指数K线数据
# https://www.okx.com/docs-v5/zh/?language=python#public-data-rest-api-get-index-candlesticks
# def getKlineData(instId, bar, limit, beforeTs):
#     # 获取指数K线数据
#     result = marketDataAPI.get_index_candlesticks(
#         instId=instId, bar=bar, limit=limit, before=beforeTs
#     )
#     return result["data"]



#  种类:ETH-USDT 开始时间:2025-08-27 09:00:00 结束时间:2025-08-27 10:00:00 长度:59
def getDateStrByTs(ts):
    # 将时间戳转换为格式化时间
    if type(ts) == str:
        return datetime.fromtimestamp(int(ts) / 1000).strftime("%Y-%m-%d %H:%M:%S")
    if type(ts) == int:
        return datetime.fromtimestamp(ts / 1000).strftime("%Y-%m-%d %H:%M:%S")


def insertLine(conn: pymysql.Connection, sql: str) -> int:
    return MySqlUtil.insertLine(conn, sql)


## 组织参数
instId = "BTC-USDT"
beginDatetime = datetime(2024, 1, 19, 0, 0, 0)
endDateTime = datetime(2024, 1, 19, 1, 0, 0)

# beginDatetime = datetime(2025, 1, 1, 0, 0, 0)
# endDateTime = datetime(2025, 1, 1, 1, 0, 0)

beginDateTs = int(time.mktime(beginDatetime.timetuple())) * 1000
endDateTime = int(time.mktime(endDateTime.timetuple())) * 1000
globalDict = {"begin": beginDateTs, "end": endDateTime}
lock1 = threading.Lock()

# 任务执行
mysqlUtil = MySqlUtil("192.168.88.20", 4000, "root", "Root@123", "okxapp")
# mysqlUtil = MySqlUtil("laowangjia.site", 4306, "root", "Majingxuan123.", "okxapp")
connect = mysqlUtil.selfConnect()
lock2 = threading.Lock()

currentTimeStamp = int(time.time() * 1000)

def blockExec():
    firstExec = True
    dataList = []
    stopFlag = False
    while not stopFlag:
        if firstExec:
            print(f"种类:{instId} 开始时间:{getDateStrByTs(beginDateTs)} 结束时间:{getDateStrByTs(endDateTime)} ")
            # 获取指数K线数据
            # https://www.okx.com/docs-v5/zh/?language=python#public-data-rest-api-get-index-candlesticks
            dataList = marketDataAPI.get_history_candlesticks(instId=instId, bar="1m", before=str(beginDateTs),
                                                              after=str(endDateTime))["data"]
            for item in dataList:
                insertLine(connect,
                           f"insert into t_klinedata(ts,o,h,l,c,inst_id,line_type,date_str) values({item[0]},{item[1]},{item[2]},{item[3]},{item[4]},'{instId}','1m','{getDateStrByTs(item[0])}'); \n ")
            connect.commit()
            firstExec = False
            if len(dataList) <= 0:
                stopFlag = True
        elif not firstExec:
            beginDateTs = beginDateTs + 3600000
            endDateTime = endDateTime + 3600000
            print(f"种类:{instId} 开始时间:{getDateStrByTs(beginDateTs)} 结束时间:{getDateStrByTs(endDateTime)} ")
            dataList = marketDataAPI.get_history_candlesticks(instId=instId, bar="1m", before=str(beginDateTs),
                                                              after=str(endDateTime))["data"]
            for item in dataList:
                insertLine(connect,
                           f"insert into t_klinedata(ts,o,h,l,c,inst_id,line_type,date_str) values({item[0]},{item[1]},{item[2]},{item[3]},{item[4]},'{instId}','1m','{getDateStrByTs(item[0])}'); \n ")
            if len(dataList) <= 0:
                stopFlag = True
            connect.commit()


def getBeginEnd():
    global globalDict
    lock1.acquire_lock()
    timpBegin = globalDict["begin"]
    timeEnd = globalDict["end"]
    globalDict["begin"] = globalDict["begin"] + 3600000
    globalDict["end"] = globalDict["end"] + 3600000
    lock1.release_lock()
    return timpBegin, timeEnd


class getKlineData(threading.Thread):
    def run(self):
        global currentTimeStamp
        while True:
            being, end = getBeginEnd()
            if int(being) > currentTimeStamp or int(end) > currentTimeStamp:
                break
            # 获取指数K线数据
            # https://www.okx.com/docs-v5/zh/?language=python#public-data-rest-api-get-index-candlesticks
            dataList = marketDataAPI.get_history_candlesticks(instId=instId, bar="1m", before=str(being),
                                                              after=str(end))["data"]
            lock2.acquire_lock()
            print(
                f"种类:{instId} 开始时间:{getDateStrByTs(being)} 结束时间:{getDateStrByTs(end)} 长度:{len(dataList)} ")
            for item in dataList:
                insertLine(connect,
                           f"insert into t_klinedata(ts,o,h,l,c,inst_id,line_type,date_str) values({item[0]},{item[1]},{item[2]},{item[3]},{item[4]},'{instId}','1m','{getDateStrByTs(item[0])}'); \n ")
            connect.commit()
            lock2.release_lock()
            time.sleep(0.1)


if __name__ == '__main__':
    # 创建5个线程实例并启动
    thread_list = []
    for i in range(3):
        thread = getKlineData()
        thread_list.append(thread)
        thread.start()

    # 等待所有线程执行完毕
    for thread in thread_list:
        thread.join()

    print("所有线程执行完成")
