#闭包
def checkPermission(func):
    def innerFunc():
        print("校验权限测试")
        func()
    return innerFunc

def s1():
    print("业务代码 1")

@checkPermission
def s2():
    print("业务代码 2")

if __name__ == '__main__':
    #原本业务是调用s1 。现在使用这样嵌套可以不更改源代码
    # 。就实现了先调用权限 再执行业务
    innerFunc = checkPermission(s1)
    innerFunc()

    s1 = checkPermission(s1)
    s1()
    # @checkPermission 等同于上面的操作
    print("++++++++++=================")
    s2()