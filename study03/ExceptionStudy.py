# 有了这个变量 如果别人导入方式是  from study03.ExceptionStudy import *
# 那么只能使用这个列表中的元素
__all__ = ["testError"]

def testError():
    try:
        print(1 / 0)
    except(NameError, ZeroDivisionError) as e:
        print("catch error", e)


def finallyTest():
    try:
        print(0 / 1)
    except(NameError, ZeroDivisionError) as e:
        print("catch error", e)
    else:
        print("no error")
    finally:
        print("finally")
