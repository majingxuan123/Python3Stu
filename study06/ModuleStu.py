##常用的模块
#sys
import sys
print(sys.getsizeof(True))
import time
print(time.time())
print(time.localtime(time.time()))


import urllib.request as request
# print(request.urlopen("https://www.baidu.com").read())

###   json re math decimal logging os

# print("任何其他人调用这个类都会执行到")

if __name__ == '__main__':
    # print("只有点击运行这个类的时候才会执行")
    pass


##起个别名  导入某包下的某模块
import package1.module1 as m1
print(m1.param1)


##这种方式可以导入包或者包下的某参数 某函数
from package1.module2 import param2 as p2
from package1.module2 import func1 as f1

print(p2)