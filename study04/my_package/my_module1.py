from typing import Union

from study04.my_package.TestParent import TestParent


class testModule1(TestParent):
    index: int = 88

    def __init__(self):
        self.index = 88

    def __init__(self, index: int):
        self.index = index

    #返回值类型 ->(type)
    def __str__(self) -> (str):
        return f"index:{self.index}"

    def testImport01(self):
        print("导入了module1")

    # Union 用于告诉别人 这个list传入的不是str 就是int
    # 调用父类中的属性和方法
    def changeValue(self,list :list[Union[int,str]]):
        if str == type(list[0]):
            TestParent.name = list[0]
            index = list[1]
        elif int == type(list[0]):
            index = list[0]
            TestParent.name = list[1]