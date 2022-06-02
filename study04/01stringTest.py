

str = "Python java c go javascript"

print("[j]  index ",str.index("j"))
print("[j]  rindex ",str.rindex("j"))


#找不到就返回-1
##find first appear
print("[y]  find ",str.find("o"))
##find last appear
print("[y]  rfind ",str.rfind("o"))

print("------字符串大小写------")
#大小写转换
print(str.upper())
print(str.lower())
##所有大写转化为小写、所有小写转化为大写
print(str.swapcase())
##第一个字符转化为大写 其他都是小写
print(str.capitalize())
#每个单词第一个字符转化为大写 其他的转化为小写
print(str.title())
print("------字符串对齐------")
str1 = "hello python"
##剧中  用*补全前后
print(str1.center(20,"*"))
##左对齐 右边用*补全  如果补输入*默认用空格
print(str1.ljust(20,"*"))
##左对齐 右边用*补全
print(str1.rjust(20,"*"))
#用0 填充
print(str1.zfill(20))
print("-8888".zfill(8))
print("------字符串分割------")
str3 = "pyhthon|java|c|go|javascript"
print(str3.split("|"))
##指定了最大拆分数之后的就不拆分了
print(str3.split("|",3))
##从右边开始拆分
print(str3.rsplit("|",3))
print("------字符串判断------")
str4 = "55522ss"
str5 = "python"
##是否全是数字和字母
print(str4.isalnum())
##是否全油十进制
print(str4.isdecimal())
#合法标识符  全英文没有数字和符号
print(str1.isidentifier())
##是否全是字母
print(str5.isalpha())

print("-------拼接---------")
print(1,2,3,4,5,6,sep="|")