# 闭包
def checkPermission(func):
    def innerFunc(*args, **kwargs):
        print(f"校验权限测试 {args}   {kwargs}")
        re = func(*args, **kwargs)
        print(f"执行完闭包方法")
        return re

    return innerFunc


def s1(a, b):
    print("业务代码 1")


@checkPermission
def s2(a, b, c):
    print(f" 参数: {a},{b},{c}")
    return a + b + str(c)


if __name__ == '__main__':
    # 原本业务是调用s1 。现在使用这样嵌套可以不更改源代码
    # 。就实现了先调用权限 再执行业务
    innerFunc = checkPermission(s1)
    innerFunc("參數1", "参数2")

    s1 = checkPermission(s1)
    s1("參數1", "参数2")

    # @checkPermission 等同于上面的操作
    print("++++++++++=================")
    print("========== s2%s" % s2("参数1", "参数2", "参数3"))
    print("========== s2%s" % s2("参数1","参数2",{"a":1,"b":2}))

