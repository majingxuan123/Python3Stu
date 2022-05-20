## a>a? p>p? p>p? l>null? true
print("apple" > "app")
##a>b? false
print("apple" > "banana")

print(chr(97), chr(98))
a = "abc"
b = "abce"
# 比较内存地址
print(a is b)
# 输出a的内存地址
print(id(a))
print("用[]拆分  完整写法------[start:end:step]-----")
str = "Python java c go javascript"

print(str[0:1:1])
print(str[:1])
#没写开始默认0开始 没写结束 默认到结尾
print(str[::-1])
#从第一位开始切
print(str[1:])
