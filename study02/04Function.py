def testFunction1(name, age, gender):
    print(name, age, gender)


#设置默认值 无默认值的必须在前面
def defaultValue(gender,age=18, name="马"):
    print(name, age, gender)


#names 可以传入多个  会以元组方式接收
def multiInput(*names):
    print(names)

if __name__ == "__main__":
    testFunction1(gender="男", age=18, name="周杰伦")
    multiInput(18,20,"周杰伦");
