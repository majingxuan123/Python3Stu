print("hello\nworld")
print("hello\tworld")
#上下输出的\t 站位不一样是因为  制表符的存在
#默认4个字符占用一个制表符 hello o占用了一个 所以剩下的\t占用剩下的3个
print("helloooo\tworld")
print("hello\rworld")
#\b 是回退一个格 把o退没了
print("hello\bworld")
#转译
print("http:\\\\www.baidu.com")
print("你好我叫:\"jaychou\"")
#前面加个r 让转译无效  但是最后一个字符不能是\   print(r"hello\nworld\")
print(r"hello\nworld")

