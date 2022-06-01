

## a 是以追加模式打开  如果文件不存在就创建  如果存在就在文件末尾追加内容
## b  就是二进制
## + 以读写的方式打开  不能单独使用

##比如  a+

import time
##   r  是读取   rb 是读取二进制文件
file = open("url.txt","r")

## 指針跳到第二位   如果是中文的話   seek（1）就會報錯
# file.seek(2)
# file.tell()
print(file.readline())

file.close()
## w是写   wb 是写二进制
file1 = open("url.txt","w")
file1.writelines(time.time().__str__())
file1.close()


##

