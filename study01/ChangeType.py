name = "jaychou"
age = 18
balance = 20.12

print("age:" + str(age) + ",name:" + name)
print("age:", "age", "二进制输出：", bin(age))
print("age:", "age", "8进制输出：", oct(age))
print("age:", "age", "8进制输出：", hex(age))

print("float balance :" + str(balance) + ",name:" + name)

# float 转化int 会省略小数点后面的
print("int balance:" + str(int(balance)) + ",name:" + name)
