##字符串编码转换

string = "测试编码测试编码测试编码"
##字节数不一样
byteCode0 =string.encode(encoding="GBK")
print(byteCode0)
print(byteCode0.decode("GBK"))

byteCode1 = string.encode(encoding="UTF-8")
print(byteCode1)
print(byteCode1.decode("UTF-8"))
