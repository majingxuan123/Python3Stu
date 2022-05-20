from decimal import Decimal;

name = "周杰伦"
name = "厦门周杰伦"
print(name)

print("标识", id(name))
print("类型", type(name))
print("值", name)

print(Decimal("1.1") + Decimal("2.2"))


l1 = 1.1
l2 = 2.2
print(Decimal(l1+"")+Decimal(l2+""))