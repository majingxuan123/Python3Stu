from typing import Iterable


class Person:
    name = "我是学生"
    age = 10

    ##影响单个实例
    def __init__(self, name, age):
        self.name = name
        self.age = age

    ##类似java的toString方法  父类object就有
    def __str__(self):
        return "我叫{0}今年{1}岁了".format(self.name, self.age)

    # 将本实例输出
    def info(self):
        print(self.name, self.age, "岁了")


# 类名称   意思是 student 继承了person

## python 可以多继承   class Student(Person,Object):
class Student(Person):

    def __init__(self, name, age, stu_no):
        super().__init__(name, age)
        self.stu_no = stu_no

    def __dir__(self) -> Iterable[str]:
        return super().__dir__()

    def __add__(self, other):
        return self.name+other.name;

    def __len__(self):
        return len(self.name);

    # 将本实例输出
    def info(self):
        print(self.name, self.age, "岁了")

    ##方法是从属于“类对象”的方法。
    @classmethod
    def work1(cls):
        print("类方法", cls.age)

    ##Python中允许定义与“类对象”无关的方法，称为“静态方法”
    @staticmethod
    def work2():
        print("静态方法")


def test01():
    stu = Student("周杰伦", 20, 123)
    stu2 = Student("邓紫棋", 20, 123)
    print(dir(stu))
    print("________________特殊属性_________________")
    ##这样默认会调用stu的__str方法
    print(stu.__str__())
    ##输出stu的父类元组
    print(Student.__bases__)
    ##输出这个实例的所有属性
    print(stu.__dict__)
    ##输出这个类的各种方法
    print(Student.__dict__)
    ##类的层次结构
    print(Student.__mro__)
    print("________________特殊方法_________________")
    ##重写了里面的方法 可以实现两个类相加
    print(stu+stu2)
    ##重写了里面的len特殊方法
    print(stu.__len__())
    print(len(stu))


test01()
