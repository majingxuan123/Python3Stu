##集合不能重复
##方式1
s = {2, 3, 4, 5, 6, 7, 7, 8,9,10}
s1 = {2, 4, 3, 5, 6, 7}
s2 = {2, 4, 6,11}
print("s==s1?", s == s1)
print("s2是s1的子集？", s2.issubset(s1))
print("s1是s2的超集？", s1.issuperset(s2))
print("s2和s1是否没有交集?", s2.isdisjoint(s1))
print(f"差集测试:{s.difference(s1)}")

##方式2
set1 = set(range(6))
print(set1)
##定义空集合
nullSet = set()
print(type(nullSet))

print(set)
print(type(set))

s5 = {i * i for i in range(6)}
print("集合生成式：", s5)

print("=========== 判断存在 ===========")
##判断是否存在
print(10 in s)
print("=========== 添加 ===========")
##set 中添加元素   set是无序的
s.add(80)
print(s)
print("=========== 修改后 ===========")
##添加多个元素进去  将一个set添加进去
s.update({500, 400, "400"})
print(type(s), s)
print("=========== 删除某元素 如果不存在 remove 会抛出异常 ===========")
##删除某元素
s.remove(500)
print(type(s), s)
print("=========== 删除某元素 如果不存在不会抛出异常 ===========")
s.discard(500)
print(type(s), s)
print("=========== 随机取出一个元素（删除） ===========")
pop = s.pop()
print(f"取出的元素是：{pop}")
print("=========== 集合1删除所有集合2的内容 ===========")
print(f"删除前的内容{s}")
s.difference_update(s1)
print(f"删除后的内容{s}")
print("=========== 合并测试 ===========")
s3 = s1.union(s2)
print(f"合并后的内容{s3}")
##清空元素
s.clear()
print(type(s), s)
