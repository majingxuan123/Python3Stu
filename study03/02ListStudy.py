list1 = [1, 2, 3, 5, 4, 9, 8, 7]

list2 = list(["hello", "world", 2, 3, 4, 9.99, "最后"])
print(list2)
print(type(list))
print("===========以下是测试===========")


def xunhuanList():
    testAddObj()
    for obj in list2:
        print(obj)


def testRemove():
    # 删除一个元素  不存在会报错
    list2.remove("2")
    # 移除索引为1的元素
    list2.pop(2)


def testCutList():
    # 新的list会保留第二 第三个元素
    list_ = list2[2:4]
    print(list_)
    # 让第2第三个元素变成null
    list2[2:4] = []
    print(list2)


def testAddObj():
    # 添加一个元素
    list2.append("测试添加")
    # 至少添加一个元素 把list1里面所有元素添加在list2里面
    list2.extend(list1)
    list2.insert(2, "添加到第二位后面")


def testFunction1():
    index = list2.index("world")
    print("index:" + str(index))


# 切除list  从第二位开始  到第七位  每隔一个取一次 生成新的list
def testFunction2():
    print("切除:")
    # list_ = list2[2:7:1]
    # 不写就是到最后一位
    list_ = list2[2::1]
    print(list_)
    # 步长为负数
    print("倒序")


def checkObjIn():
    print("元素在列表中？:")
    print("ceshi" in list2)
    print(list2[::-1])


def updateListObj():
    list2[1] = "测试更换数据"
    print(list2)
    # 第一位和第二位会替换
    list2[1:3] = [10, 20, 30]
    print(list2)
    # 第一位和第二位会替换
    list2[1:3] = list1
    print(list2)


def sortList():
    list1.sort()
    # 按字典顺序升序排列
    list1.sort()
    print("升序:", list1)
    # 按降序排列
    list1.sort(reverse=True)
    print("降序:",list1)

def createList():
    listTest = [i for i in range(1,10)]
    print(listTest)

createList()
