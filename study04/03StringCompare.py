## a>a? p>p? p>p? l>null? true
print("apple" > "app")
##a>b? false
print("apple" > "banana")

print(chr(97), chr(98))
a = "abc"
b = "abce"
print("======= a is b  ========")
# 比较内存地址
print(a is b)
# 输出a的内存地址
print(id(a))

str = "Python java c go javascript"
print("用[]拆分  完整写法------[start:end:step]-----完整字符：", str)

print(str[0:1:1])
print(str[:1])
# 没写开始默认0开始 没写结束 默认到结尾
print(str[::-1])
# 从第一位开始切
print(str[1:])

name = "jayChou"
age = 20
# %d 是数字
print("我叫%s,我%d岁" % (name, age))
print("我叫{0},我{1}岁".format(name, age))
# 前面有一个f
print(f"我叫{name},我{age}岁")

# 10d的意思是指数字宽度   %.3f  的意思是保留小数点后3位
print("%10d" % 50)
print("{0:.3}".format(3.1415926))
print("{0:.3f}".format(3.1415926))
