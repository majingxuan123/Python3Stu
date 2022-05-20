##集合不能重复
##方式1
s = {2, 3, 4, 5, 6, 7, 7}

s1 = {2, 4, 3, 5, 6, 7}
s2 = {2,4,6}
print("s==s1?",s == s1)
print("s2是s1的子集？",s2.issubset(s1))
print("s1是s2的超集？",s1.issuperset(s2))

print("s2和s1是否没有交集?" ,s2.isdisjoint(s1))
##方式2
set1 = set(range(6))
print(set1)
##定义空集合
nullSet = set()
print(type(nullSet))

print(set)
print(type(set))

s5 = { i*i for i in range(6)}
print("集合生成式：",s5)

print("===========以下是测试===========")
##判断是否存在
print(10 in s)

##set 中添加元素   set是无序的
s.add(80)
print(s)

##添加多个元素进去  将一个set添加进去
s.update({500,400,"400"})
print(type(s),s)

##删除某元素
##如果不存在 remove 会抛出异常
s.remove(500)
print(type(s),s)
##如果不存在不会抛出异常
s.discard(500)
print(type(s),s)

##删除一个任意元素
s.pop()
print(type(s),s)

##清空元素
s.clear()
print(type(s),s)
