def testFun(a, b, c):
    print("a:", a)
    print("b:", b)
    print("c:", c)
    print("==============")


lst = {"aaaaa", "bbbbbb", "cccccc"}
# 这样传入会报错
# testFun(lst)

# 函数调用时将每个 参数都转换为位置参数代入
print("函数调用时将每个 参数都转换为位置参数代入")
testFun(*lst)

print("用字典代入")
dic = {"a": "aaaaa", "b": "bbbbbbb", "c": "ccccccccccc"}
testFun(**dic)

print("中间多了一个* 代表从这里开始后面的必须要用指定参数")
def testFun1(a, b, *, c, d):
    #这样定义的变量就是全局变量 声明为全局变量
    global gl_str
    gl_str = "马境宣"
    print("a:", a)
    print("b:", b)
    print("c:", c)
    print("d:", d)
    print("==============")



dic2 = {"c" : "30", "d" : "40"}

testFun1(10, 20, c=30, d=40)
testFun1(10, 20, **dic2)
