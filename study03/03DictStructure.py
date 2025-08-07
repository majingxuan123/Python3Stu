##类似java的map
##可变

##第一种
teacher = {'name': "张三", "age": 30}
##第二种
student = dict(name="zhangsan",age=18)
##空字典
d = {}
print(type(teacher))
print(teacher)
print(student)
print("===========以下是测试===========")

def getDic():
    ##
    # name = teacher.get("name")
    ##下面这种方式如果没有查到  就给它一个默认值 周杰伦
    name = teacher.get("nam2e","周杰伦")
    ##这种方式获取不到会报错
    name2 = teacher["name"]
    print("name:",name)
    print("name2:",name2)

# 移除元素
def removeDic(key):
    teacher.pop(key)

# 清空元素
def clearDic():
    teacher.clear()

def checkDic():
    print("name" in teacher)
    ##删除某元素
    del teacher['name']
    print("name" not in teacher)


##字典内容类型
def testDic():
    keys = teacher.keys()
    print(keys)
    print(type(keys))
    ##将 dict_keys 类型转换成list
    keyList = list(keys)
    print(keyList)
    #dict_items  元组
    items = teacher.items()
    print(type(items))

##字典循环
def testDic2():
    for item in teacher:
        print("======== 字典循环  =========")
        print("key:",item)
        print("key type :",type(item))
        print("value:",teacher.get(item))

def zipDic():
    print("========== 压缩转list ============")
    names=["周杰伦","林俊杰","邓紫棋"]
    ids=[5,7,9]
    zipDic = zip(names, ids)

    print(f"压缩结果：{zipDic}")
    # 这一步转换会将原始的数据改变  zipDic 就不能循环了
    listTest =list(zipDic)
    print(f"zip 转 list  {type(listTest)}  内容:{listTest} ")
    newNames , newIds = zip(*listTest)
    print(f"解包之后得到 names:{newNames} ids:{newIds}")
    print("========== 压缩转list ============")

    print("========== 压缩转 dict ============")
    names=["周杰伦","林俊杰","邓紫棋"]
    ids=[5,7,9]
    zipDic = zip(names, ids)
    print(f"压缩结果：{zipDic}")
    # 这一步转换会将原始的数据改变  zipDic 就不能循环了
    dictTest =dict(zipDic)
    print(f"zip 转 dict  {type(dictTest)}  内容:{dictTest} ")
    print(f"解包之后得到 names:{newNames} ids:{newIds}")

    for name1,id1 in zipDic:
        print(name1,id1)
    print("========== 压缩转 dict ============")


    print("========== 测试解包 ============")
    names1=["周杰伦","林俊杰","邓紫棋"]
    ids1=[5,7,9]
    zipDic1 = zip(names1, ids1)
    print(f"压缩结果：{zipDic1}")
    name2,id2 = zip(*zipDic1)
    print(f"解包结果name2:{name2} id2:{id2}")

    print("========== 测试解包 ============")

if __name__ == '__main__':
    testDic2()