import os
import project0.util


class StudentSystemUtil:
    @staticmethod
    def checkInputStr(inputNum):
        # if (inputNum == 1 or inputNum == 2 or inputNum==3 or inputNum==4 or inputNum==5 or inputNum==6 or inputNum==7 or inputNum==0):
        # if (inputNum >= 0 and inputNum <= 7):
        if inputNum in [0, 1, 2, 3, 4, 5, 6, 7]:
            return True
        else:
            return False


class DiskUtil:
    @classmethod
    def insertStu(self, id, name, java, python):
        fileName = os.getcwd() + "\\studentInfo.txt"
        ##以这个格式打开之后 写入也是这个格式
        with open(fileName, "a", encoding="utf-8") as file:
            file.writelines(str({"id": id, 'name': name, "java": java, "python": python}) + "\n")


if __name__ == '__main__':
    DiskUtil.insertStu(1, "张三", "100", "90")
