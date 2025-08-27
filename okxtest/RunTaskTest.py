import ast

import pymysql

from okxtest.MySqlUtil.MySqlUtil import MySqlUtil

# 订单数量
orderCount = 0.1
# 收单翻倍
firstOrderMultiple = 3
# 买的货币
missionInstId = "ETH-USDT"
# 杠杆倍数
orderLevel = 50
# 盈利收益百分比
profitPercent = 0.006
# 止损百分比
stopPercent = 999
# 开始保证金
startBalance = 400
# 未实现收益
unDoProfit = 0

longAddList = [(0.005, 0.2), (0.01, 0.3), (0.015, 1), (0.025, 2), (0.035, 1), (0.04, 3), (0.07, 1),
               (0.08, 4), (0.12, 4), (0.15, 2), (0.18, 8)]
shortAddList = [(0.005, 0.2), (0.01, 0.3), (0.015, 1), (0.025, 2), (0.035, 1), (0.04, 3), (0.07, 1),
                (0.08, 4), (0.12, 4), (0.15, 2), (0.18, 8)]

currentLong = {"count": 0, "currentAddIndex": 0, "currentAvg": 0, "beginPrice": 0}
currentShort = {"count": 0, "currentAddIndex": 0, "currentAvg": 0, "beginPrice": 0}


# 1张 50倍 0.6盈利的话 赚1.5

# 保证金 = 均价 / 杠杆倍率


class KlineData:
    def __init__(self, id, ts, open_price, high_price, low_price, close_price, period, inst_id, create_time):
        self.id = id
        self.ts = int(ts)
        self.open_price = float(open_price)
        self.high_price = float(high_price)
        self.low_price = float(low_price)
        self.close_price = float(close_price)
        self.period = period
        self.inst_id = inst_id
        self.create_time = create_time

    def __init__(self, str):
        str.replace("'", "")
        str = str[1:-1]
        split = str.split(",")
        self.id = split[0]
        self.ts = float(split[1])
        self.open_price = float(split[2].replace("'", ""))
        self.high_price = float(split[3].replace("'", ""))
        self.low_price = float(split[4].replace("'", ""))
        self.close_price = float(split[5].replace("'", ""))
        self.period = split[6]
        self.inst_id = split[7]
        self.create_time = split[8]

    def __repr__(self):
        return f"KlineData(id={self.id}, ts={self.ts}, open={self.open_price}, high={self.high_price}, " \
               f"low={self.low_price}, close={self.close_price}, period={self.period}, inst_id={self.inst_id}, " \
               f"create_time={self.create_time})"


#   mysql 查询
def queryCurrentKlineData(conn: pymysql.Connection, currentIndex: int, querySize: int) -> (list[KlineData]):
    # 这里是用类静态方法调用的
    rows = MySqlUtil.query(conn, f"select * from t_klinedata order by ts asc limit {currentIndex},{querySize}")
    # 将每一行数据转换为KlineData对象
    kline_data_list = []
    rows = rows[1:]
    for row in rows:
        # parsed_data = ast.literal_eval(row)
        # 如果row是字符串，需要先解析它
        kline_data = KlineData(row)
        kline_data_list.append(kline_data)
    return kline_data_list

# 计算均价
def caculateAvgPrice(old_avg: float, oldCount: float, new_price: float, count: float) -> float:
    return (old_avg * oldCount + new_price * count) / (oldCount + count)

# 计算未实现收益
def caculateUnDoProfit(line: KlineData):
    # long
    longProfit = (line.close_price - currentLong["currentAvg"]) / (line.close_price / 10) * currentLong[
        "count"] * orderLevel
    shortProfit = (currentShort["currentAvg"] - line.close_price) / (line.close_price / 10) * currentShort[
        "count"] * orderLevel
    return longProfit, shortProfit

# 每一次跳动处理
def singleLineDeal(line: KlineData):
    highPrice = float(line.high_price)
    lowPrice = float(line.low_price)
    # 盈利卖出价格
    longSellPrice = currentLong["currentAvg"] * (1 + profitPercent)
    shortSellPrice = currentShort["currentAvg"] * (1 - profitPercent)
    # 补仓价格
    longAddPrice = currentLong["currentAvg"] * (1 - longAddList[currentLong["currentAddIndex"]][0])
    shortAddPrice = currentShort["currentAvg"] * (1 + shortAddList[currentShort["currentAddIndex"]][0])

    # 如果没有仓位就开仓
    if currentLong["count"] == 0 and currentShort["count"] == 0:
        buySwap(line=line, addPrice=line.close_price, side="long")
        buySwap(line=line, addPrice=line.close_price, side="short")
    else:
        # todo 这里要计算
        # ================================多单操作====================================
        if longAddPrice < highPrice:
            buySwap(line=line, addPrice=longAddPrice, side="long")
        else:
            if longSellPrice > lowPrice:
                sellSwap(line, longSellPrice, "long")
        # ================================空单操作====================================
        if shortAddPrice > lowPrice:
            buySwap(line=line, addPrice=shortAddPrice, side="short")
        else:
            if shortSellPrice < highPrice:
                sellSwap(line, shortSellPrice, "short")

# 卖出仓位
def sellSwap(line: KlineData, sellPrice: float, side: str):
    global startBalance
    highPrice = float(line.high_price)
    lowPrice = float(line.low_price)
    if "long" == side:
        # 因为实际上还要扣除手续费 所以我这里约等于打88折
        longProfit = (sellPrice - currentLong["currentAvg"]) / (line.close_price / 10) * currentLong[
            "count"] * orderLevel * 0.88
        print(f" {side}盈利{longProfit}")
        startBalance += longProfit
        # 清空所有仓位
        currentLong["count"] = 0
        currentLong["currentAvg"] = 0
        currentLong["beginPrice"] = 0
        currentLong["currentAddIndex"] = 0
        if sellPrice > lowPrice and sellPrice < highPrice:
            buySwap(line, sellPrice, "long")
        # 再次购买仓位
        else:
            buySwap(line, highPrice, "long")
    elif "short" == side:
        # 因为实际上还要扣除手续费 所以我这里约等于打88折
        # 因为实际上还要扣除手续费 所以我这里约等于打88折
        shortProfit = (currentShort["currentAvg"] - sellPrice) / (line.close_price / 10) * currentShort[
            "count"] * orderLevel * 0.88
        print(f" {side}盈利{shortProfit}")
        startBalance += shortProfit
        # 清空所有仓位
        currentShort["count"] = 0
        currentShort["currentAvg"] = 0
        currentShort["beginPrice"] = 0
        currentShort["currentAddIndex"] = 0

        if sellPrice > lowPrice and sellPrice < highPrice:
            buySwap(line, sellPrice, "short")
        # 再次购买仓位
        else:
            buySwap(line, lowPrice, "short")


# 购买仓位
def buySwap(line: KlineData, addPrice: float, side: str):
    if "long" == side:
        if currentLong["count"] == 0:
            print(f"开仓  方向:{side} 价格:{addPrice} ")
            currentLong["count"] = orderCount * firstOrderMultiple
            currentLong["currentAvg"] = addPrice
            currentLong["beginPrice"] = addPrice
            currentLong["currentAddIndex"] = 0
        else:
            # 补仓 需要计算均价
            newAvgPrice = caculateAvgPrice(currentLong["currentAvg"], currentLong["count"], addPrice,
                                           longAddList[currentLong["currentAddIndex"]][1] * orderCount)
            print(
                f"补仓  方向:{side} 补仓价格:{addPrice} 原均价:{currentLong["currentAvg"]}  新均价：{newAvgPrice} 总仓位:{currentLong["count"] + longAddList[currentLong["currentAddIndex"]][1] * orderCount}")
            currentLong["count"] = currentLong["count"] + longAddList[currentLong["currentAddIndex"]][1] * orderCount
            currentLong["currentAvg"] = newAvgPrice
            currentLong["currentAddIndex"] = currentLong["currentAddIndex"] + 1
    if "short" == side:
        if currentShort["count"] == 0:
            print(f"开仓  方向:{side} 价格:{addPrice}")
            currentShort["count"] = orderCount * firstOrderMultiple
            currentShort["currentAvg"] = addPrice
            currentShort["beginPrice"] = addPrice
            currentShort["currentAddIndex"] = 0
        else:
            # 补仓 需要计算均价
            newAvgPrice = caculateAvgPrice(currentLong["currentAvg"], currentLong["count"], addPrice,
                                           longAddList[currentLong["currentAddIndex"]][1] * orderCount)
            print(
                f"补仓  方向:{side} 补仓价格:{addPrice} 原均价:{currentShort["currentAvg"]}  新均价：{newAvgPrice} 总仓位:{currentShort["count"] + shortAddList[currentShort["currentAddIndex"]][1] * orderCount}")
            currentShort["count"] = currentShort["count"] + longAddList[currentShort["currentAddIndex"]][1] * orderCount
            currentShort["currentAvg"] = newAvgPrice
            currentShort["currentAddIndex"] = currentShort["currentAddIndex"] + 1


if __name__ == '__main__':
    currentIndex = 0
    querySize = 100

    # 这里是用成员方法调用的
    test = MySqlUtil("192.168.88.20", 4000, "root", "Root@123", "okxapp")
    # 这里用实例方法调
    conn = test.selfConnect()

    while True:
        klineData = queryCurrentKlineData(conn, currentIndex, querySize)
        currentIndex += querySize
        for line in klineData:
            longProfit, shortProfit = caculateUnDoProfit(line)
            print(
                f"时间:{line.create_time} 价格:{line.close_price} 总资产:{startBalance + longProfit + shortProfit} 多:{longProfit} 空:{shortProfit}")
            singleLineDeal(line)
