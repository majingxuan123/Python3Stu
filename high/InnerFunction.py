print("=========================== map")
m = map(lambda x: x * x, [1, 2, 3, 4, 5])
for i in m:
    print(i)
print("====")
m1 = map(lambda a,b: a+b, [1, 3,5,7,9],[2,4,6,8,10])
for i in m1:
    print(i)


print("=========================== reduce")
from functools import reduce

i = reduce(lambda x, y: x + y, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(f"sum is :{i}")

str = reduce(lambda x,y:x+y,["aa","bb","cc"],"dd")
print(f"str is :{str}")

print("=========================== filter")
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
f = filter(lambda x: x % 2 == 0, list1)
for i in f:
    print(i)

print("================= sort")
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list1.sort(reverse=True)
print(list1)

