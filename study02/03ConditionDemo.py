def scopeTest():
    scope = 80
    if 90 <= scope <= 100:
        print("优秀")
    elif 80 <= scope < 90:
        print("良好")
    elif 60 <= scope < 80:
        print("及格")
    else:
        print("及格")

scopeTest()


def whileTest():
    # if
    name = 1
    while name < 3:
        if name == 1:  # 判断变量是否为 python
            name += 1
            print('zhoujielun')  # 并输出欢迎信息
        elif name == 2:
            name += 1
            print("majingxuan")  # 条件不成立时输出变量名称
        else:
            print("caixukun")
            break


def forTest():
    print("====================")
    for letter in 'Python':  # 第一个实例
        print("当前字母: %s" % letter)

    fruits = ['banana', 'apple', 'mango']
    for fruit in fruits:  # 第二个实例
        print('当前水果: %s' % fruit)

    for i in range(5):
        print("输出第"+str(i)+"次")

forTest()