from decimal import Decimal;

name = "周杰伦"
name = "厦门周杰伦"
print(name)

company = "测试公司"



print("标识", id(name))
print("类型", type(name))
print("值", name)
print("=================================")

print(type(company) == str)
print(type(name) == str)
print(type(company) == Decimal)


print(type(company) is type(name))
print(type(company) == type(name))

print("=================================")



print(Decimal("1.1") + Decimal("2.2"))
l1 = 1.1
l2 = 2.2
print(Decimal(l1+"")+Decimal(l2+""))
print("=================================")

