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
        print("======================")
        print("key:",item)
        print("key type :",type(item))
        print("value:",teacher.get(item))

def zipDic():
    items=["fruits","book","other"]
    price=[5,7,9]
    zipDic = zip(items, price)
    ##可以转换成map或者list
    print(type(dict(zipDic)))
    print(type(list(zipDic)))

zipDic()