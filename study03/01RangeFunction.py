r = range(10);
# r = range(1,10);
# r = range(0,10,2);

print(r)
# 用于查看range对象中的整数序列
print(list(r))

print(10 not in r)
print(10 in r)

print("测试0～100偶数和")
ran = range(0, 100, 2);
sum = 0
for ra in ran:
    sum += ra
print(sum)

print("测试输出字符串")
for str in "Python":
    print(str)
