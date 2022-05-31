import copy;


class Bag:
    pass


class Person:
    name = ""
    age = 0
    def __init__(self, name, age, bag):
        self.name = name
        self.age = age
        self.bag = bag


person1 = Person("zhoujielun", 20, Bag())
person2 = person1
print(id(person2) == id(person1))
print("person1  bag",id(person1.bag))
print("person2  bag",id(person2.bag))
##这个是浅拷贝  只拷贝person对象里面的值

person3 = copy.copy(person1)
# 会递归拷贝对象里面的所有子对象
person4 = copy.deepcopy(person1)
print(id(person3) == id(person1))
print("person3  bag",id(person3.bag))
