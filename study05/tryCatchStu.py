import traceback;

try:
    a=int(input("输入一个数字"))
    b=int(input("输入第二个数字"))
except BaseException as e:
    ##输出异常   e.printStack
    traceback.print_exc()
    print("出错啦")
    print(e)
else:
    print("两个数字之和为:",a+b)
finally:
    print("无论是否异常一定会执行的")