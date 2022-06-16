import os
import project0.util
import json


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

    @classmethod
    def checkWrite(self, id, name, java, python):
        fileName = os.getcwd() + "\\studentInfo.txt"
        write = []
        ##以这个格式打开之后 写入也是这个格式
        with open(fileName, "r", encoding="utf-8") as file:
            lines = file.readlines()
            for l in lines:
                ## 字符串转字典
                l_dic = eval(l)
                if (l_dic.get("id") == str(id)):
                    write.append({"id": id, "name": name, "java": java, "python": python})
                else:
                    write.append(l_dic)
        ##以这个格式打开之后 写入也是这个格式
        with open(fileName, "w+", encoding="utf-8") as file:
            for w in write:
                file.writelines(str(w)+"\n")


if __name__ == '__main__':
    fileName = os.getcwd()
    index = fileName.rfind("/") - 4
    fileName = fileName[:index] + "\\studentInfo.txt"

    DiskUtil.checkWrite(12,121,121,121);
