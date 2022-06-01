##with会自动释放资源 不需要自己close了
with open("url.txt","r") as file:
    print(file.readline())









class MyOpen:
    def __enter__(self):
        print("调用了enter")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("调用了exit")

    def show(self):
        print("调用了self")


with MyOpen() as testFile:
    testFile.show()