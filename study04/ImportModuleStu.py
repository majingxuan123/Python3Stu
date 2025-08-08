# pip install -i https://pypi.tuna.tsinghua.edu.cn/simple numpy
def testSleep():
    # 引入整个time
    import time
    print("开始执行")
    time.sleep(2)
    print("结束执行")


from time import *


def testSleep():
    # 引入整个time 这样引入可以不用 time.sleep
    print("开始执行")
    sleep(2)
    print("结束执行")


def testSleep1():
    # 只引入sleep
    from time import sleep
    print("开始执行")
    sleep(2)
    print("结束执行")


def testImport():
    import StringTest01
    StringTest01.cutStr()
    import study03.ExceptionStudy as es
    es.testError()

import my_package.my_module1 as module1
import my_package.my_module2 as module2
if __name__ == '__main__':
    module1.testImport01()
    module2.testImport02()
