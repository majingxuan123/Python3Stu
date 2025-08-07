def scopeTest():
    print("========== if test ==============")
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
    print("========== while test ==============")
    # if
    name = 1
    while name < 3:
        if name == 1:  # 判断变量是否为 python
            print('zhoujielun')  # 并输出欢迎信息
            name += 1
        elif name == 2:
            print("majingxuan")  # 条件不成立时输出变量名称
            name += 1
        else:
            print("caixukun")
            break
whileTest()

def forTest():
    print("========== for test ==============")

    for letter in 'Python':  # 第一个实例
        print("当前字母: %s" % letter)

    fruits = ['banana', 'apple', 'mango']
    for fruit in fruits:  # 第二个实例
        print('当前水果: %s' % fruit)

    for i in range(5):
        print("输出第"+str(i)+"次")

forTest()



def game():
    print("========== 测试 game ==========")
    index =1
    while index < 6:
        inputInteger = int(input("========== 请输入一个数字 =========="))
        if inputInteger >50 :
            print(f"输入了{index} 次 您输入的过大")
            index+=1
        elif inputInteger < 50:
            print(f"输入了{index} 次 您输入的过小")
            index+=1
        else:
            print("您输入的正确")
            break
game()
