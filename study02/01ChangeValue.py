a = 1

b = 2

a, b = 11, 20
# 交换a，b 和10，20的值
print("a:", a)
print("b:", b)

list1 = [11, 22, 33, 44]
list2 = [11, 22, 33, 44]
print("比较值相等")
print(list2==list1)
print("比较内存地址相等")
print(list2 is list1)
print(list2 is not list1)

#关系表达式  and
print("=========and")
print(a==10 and b == 10)
print("=========or")
print(a==10 or b == 10)
print("=========not  就是java的  取反 !")
print(not a==10 )
print("=========in")
print(a in list1 )
print(b in list1 )


