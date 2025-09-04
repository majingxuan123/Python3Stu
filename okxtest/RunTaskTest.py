import ast

import pymysql

from okxtest.MySqlUtil.MySqlUtil import MySqlUtil

# 3倍 sol 0.006  [(0.01, 0.5), (0.02, 1.5), (0.055, 3), (0.085, 6),  (0.18, 18)]
# 时间: '2025-09-01 14:59:00' 价格:198.81
# 总资产:706.155
#  多:-24.486695840249492 均:210.981 0.8张 起:217.034  下次补仓:193.047
#  空:-1.7783310698657184 均:196.79 0.35张 起:196.509  下次补仓:200.726

startDate = "2025-06-01 00:00:00"

# 订单数量
orderCount = 0.3
# 收单翻倍
firstOrderMultiple = 2
# 买的货币
missionInstId = "SOL-USDT"
# 杠杆倍数
orderLevel = 50
# 盈利收益百分比
# sol 7.7 440
profitPercent = 0.006
# 止损百分比
stopPercent = 999
# 开始保证金
startBalance = 400
# 未实现收益
unDoProfit = 0

# 时间: [(0.025, 1),(0.055, 2), (0.085, 3), (0.014,6), (0.020, 12)] '2025-07-11 05:17:00' 价格:162.0 # 总资产:-24.328



# 逐渐减少 [(0.005, 0.2),(0.01, 0.5), (0.02, 1.5), (0.055, 3), (0.085, 6),  (0.18, 18)]

longAddList = [(0.005, 0.2),(0.01, 0.5), (0.02, 1.5), (0.055, 3), (0.085, 6),  (0.18, 18)]
shortAddList = [(0.005, 0.2),(0.01, 0.5), (0.02, 1.5), (0.055, 3), (0.085, 6),  (0.18, 18)]

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
    rows = MySqlUtil.query(conn,
                           f"select * from t_klinedata where inst_id = '{missionInstId}' and date_str > '{startDate}' order by ts asc limit {currentIndex},{querySize}")
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
    highPrice = keep_three_decimal(float(line.high_price), 3)
    lowPrice = keep_three_decimal(float(line.low_price), 3)
    # 盈利卖出价格
    longSellPrice = keep_three_decimal(currentLong["currentAvg"] * (1 + profitPercent), 3)
    shortSellPrice = keep_three_decimal(currentShort["currentAvg"] * (1 - profitPercent), 3)

    # 补仓价格
    if currentLong["currentAddIndex"] <= len(longAddList) - 1:
        longAddPrice = keep_three_decimal(
            currentLong["currentAvg"] * (1 - longAddList[currentLong["currentAddIndex"]][0]), 3)
    else:
        longAddPrice = None
    if currentShort["currentAddIndex"] <= len(shortAddList) - 1:
        shortAddPrice = keep_three_decimal(
            currentShort["currentAvg"] * (1 + shortAddList[currentShort["currentAddIndex"]][0]), 3)
    else:
        shortAddPrice = None
    longProfit, shortProfit = caculateUnDoProfit(line)
    print(f"总资产:{keep_three_decimal(startBalance + longProfit + shortProfit, 3)} ")
    print(
        f" 多:{longProfit} 均:{keep_three_decimal(currentLong["currentAvg"], 3)} {keep_three_decimal(currentLong["count"])}张 起:{currentLong["beginPrice"]}  下次补仓:{longAddPrice}")
    print(
        f" 空:{shortProfit} 均:{keep_three_decimal(currentShort["currentAvg"], 3)} {keep_three_decimal(currentShort["count"])}张 起:{currentShort["beginPrice"]}  下次补仓:{shortAddPrice}")
    # 如果没有仓位就开仓
    if currentLong["count"] == 0 and currentShort["count"] == 0:
        buySwap(line=line, addPrice=line.close_price, side="long")
        buySwap(line=line, addPrice=line.close_price, side="short")
    else:
        # ================================多单操作====================================
        if longAddPrice is not None:
            if longAddPrice > highPrice and longAddPrice > lowPrice:
                # 补仓
                buySwap(line=line, addPrice=longAddPrice, side="long")
            elif longAddPrice > lowPrice and longAddPrice < highPrice:
                # 补仓
                buySwap(line=line, addPrice=longAddPrice, side="long")
            elif highPrice > longAddPrice and lowPrice > longAddPrice:
                if longSellPrice > highPrice and longSellPrice > lowPrice:
                    pass
                elif lowPrice < longSellPrice and longSellPrice < highPrice:
                    sellSwap(line, longSellPrice, "long")
                elif lowPrice < longSellPrice and highPrice < longSellPrice:
                    sellSwap(line, longSellPrice, "long")
                elif longSellPrice < lowPrice and longSellPrice < highPrice:
                    sellSwap(line, longSellPrice, "long")
                else:
                    print("其他情况")
        else:
            if longSellPrice > highPrice and longSellPrice > lowPrice:
                pass
            elif highPrice > longSellPrice and lowPrice < longSellPrice:
                sellSwap(line, longSellPrice, "long")
            elif highPrice < longSellPrice and lowPrice < longSellPrice:
                sellSwap(line, longSellPrice, "long")
            else:
                print("其他情况")
        # ================================空单操作====================================
        if shortAddPrice is not None:
            if shortAddPrice < lowPrice and shortAddPrice < highPrice:
                # 补仓
                buySwap(line=line, addPrice=shortAddPrice, side="short")
            elif shortAddPrice < highPrice and shortAddPrice > lowPrice:
                # 补仓
                buySwap(line=line, addPrice=shortAddPrice, side="short")
            elif highPrice < shortAddPrice and lowPrice < shortAddPrice:
                if shortSellPrice < highPrice and shortSellPrice < lowPrice:
                    pass
                elif lowPrice < shortSellPrice and highPrice > shortSellPrice:
                    sellSwap(line, shortSellPrice, "short")
                elif lowPrice < shortSellPrice and highPrice < shortSellPrice:
                    sellSwap(line, shortSellPrice, "short")
                elif shortSellPrice < lowPrice and shortSellPrice < highPrice:
                    sellSwap(line, shortSellPrice, "short")
                else:
                    print("其他情况")
        else:
            if shortSellPrice < highPrice and shortSellPrice < lowPrice:
                pass
            elif lowPrice < shortSellPrice and highPrice > shortSellPrice:
                sellSwap(line, shortSellPrice, "short")
            elif lowPrice < shortSellPrice and highPrice < shortSellPrice:
                sellSwap(line, shortSellPrice, "short")
            else:
                print("其他情况")


# 卖出仓位
def sellSwap(line: KlineData, sellPrice: float, side: str):
    global startBalance
    highPrice = float(line.high_price)
    lowPrice = float(line.low_price)
    if "long" == side:
        # 因为实际上还要扣除手续费 所以我这里约等于打88折
        longProfit = (sellPrice - currentLong["currentAvg"]) / (line.close_price / 10) * currentLong[
            "count"] * orderLevel * 0.88
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
            currentLong["count"] = orderCount * firstOrderMultiple
            currentLong["currentAvg"] = addPrice
            currentLong["beginPrice"] = addPrice
            currentLong["currentAddIndex"] = 0
        else:
            # 补仓 需要计算均价
            newAvgPrice = caculateAvgPrice(currentLong["currentAvg"], currentLong["count"], addPrice,
                                           longAddList[currentLong["currentAddIndex"]][1] * orderCount)
            currentLong["count"] = currentLong["count"] + longAddList[currentLong["currentAddIndex"]][1] * orderCount
            currentLong["currentAvg"] = newAvgPrice
            currentLong["currentAddIndex"] = currentLong["currentAddIndex"] + 1
    if "short" == side:
        if currentShort["count"] == 0:
            # print(f"开仓  方向:{side} 价格:{addPrice}")
            currentShort["count"] = orderCount * firstOrderMultiple
            currentShort["currentAvg"] = addPrice
            currentShort["beginPrice"] = addPrice
            currentShort["currentAddIndex"] = 0
        else:
            # 补仓 需要计算均价
            newAvgPrice = caculateAvgPrice(currentShort["currentAvg"], currentShort["count"], addPrice,
                                           shortAddList[currentShort["currentAddIndex"]][1] * orderCount)
            currentShort["count"] = currentShort["count"] + shortAddList[currentShort["currentAddIndex"]][
                1] * orderCount
            currentShort["currentAvg"] = newAvgPrice
            currentShort["currentAddIndex"] = currentShort["currentAddIndex"] + 1


def keep_three_decimal(num, num2=3):
    formatStr = "{:." + str(num2) + "f}"
    result = formatStr.format(num)
    return float(result)


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
            print("----------------------")
            print(f"时间:{line.create_time} 价格:{keep_three_decimal(line.close_price, 3)}")

            singleLineDeal(line)
            print("----------------------")
