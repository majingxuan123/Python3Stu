from study04.my_package.TestParent import TestParent


class testModule2(TestParent):

    def __init__(self):
        super().__init__(99, "module2")


    def __str__(self):
        return super().__str__()

    def testImport02(self):
        print("导入了module2")