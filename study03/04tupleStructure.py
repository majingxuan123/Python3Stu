##元组 数据结构

##元组是不可变的   也就是说改变它的值实际上是新建了一个
##可以改变元组中的可变类型  比如 group1中的那个数组 我可以往里面新增一个4

##最外面的小括号可以省略
group1 = ("pyahon", "java", "go",[1,2,3])
group1 = "pyahon", "java", "go"

group2 = tuple(("python", "java", "go"))
# 只有一个元素的话  最后也要加上逗号！
group3 = ("python",)
print(type(group1))
print(group1)

print("空列表",[])
print("空字典",{})
print("空元组",())
print("===========以下是测试===========")


def getTuple():
    print(group1[1])

    for item in group1:
        print(item)


getTuple()