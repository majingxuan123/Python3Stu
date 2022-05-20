
import keyword;


##输出 关键词
print(keyword.kwlist)
#打开文件  新增模式  如果文件不存在就创建、如果存在就增加
fp = open("/Users/majingxuan/Desktop/test.txt","a+")
#往文件里面输入
print("Hello World",file=fp)

print("Hello World")

#关闭文件流
fp.close()