class TestParent:

    index: int = 10
    name: str = "张三"

    #参数类型 :type
    def __init__(self, index: int, name: str):
        self.index = index
        self.name = name
        print("========== 测试父类 ==========")

    def __str__(self):
        return f"index:{self.index} name:{self.name}"

    def testFunction1(self):
        print("========== 测试父类方法 ==========")
        print(f"index:{self.index} name:{self.name}")
