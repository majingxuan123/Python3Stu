import os


class StudentSystemUtil:
    @staticmethod
    def checkInputStr(inputNum):
        # if (inputNum == 1 or inputNum == 2 or inputNum==3 or inputNum==4 or inputNum==5 or inputNum==6 or inputNum==7 or inputNum==0):
        # if (inputNum >= 0 and inputNum <= 7):
        if inputNum in [0, 1, 2, 3, 4, 5, 6, 7]:
            return True
        else:
            return False


##
##  用于写磁盘  模拟数据库
##
class DiskUtil:

    @classmethod
    # mode  true:升  false 降
    def sortStu(self, sortKey, mode):
        fileName = os.getcwd() + "\\studentInfo.txt"
        with open(fileName, "r", encoding="utf-8") as file:
            lines = file.readlines()
            lines.sort(key=lambda l: int(eval(l).get(sortKey)), reverse=mode)
            for line in lines:
                print(line)



    @classmethod
    def queryStu(self, stuInfo):
        fileName = os.getcwd() + "\\studentInfo.txt"
        with open(fileName, "r", encoding="utf-8") as file:
            lines = file.readlines()
            for line in lines:
                lineDic = eval(line)
                id = lineDic.get("id")
                name = lineDic.get("name")
                if str(id) == str(stuInfo) or str(name) == str(stuInfo):
                    return lineDic

    @classmethod
    def delStu(self, stuInfo):
        fileName = os.getcwd() + "\\studentInfo.txt"
        write = []
        needDelete = False
        ##以这个格式打开之后 写入也是这个格式
        with open(fileName, "r", encoding="utf-8") as file:
            lines = file.readlines()
            if lines.__len__() == 0:
                print("\033[0;31;40m{0}\033[0m".format("用户不存在"))
            else:
                for l in lines:
                    ## 字符串转字典
                    l_dic = eval(l)
                    if (l_dic.get("id") == str(stuInfo) or l_dic.get("name") == str(stuInfo)):
                        needDelete = True
                    else:
                        write.append(l_dic)
        if needDelete:
            ##以这个格式打开之后 写入也是这个格式
            with open(fileName, "w+", encoding="utf-8") as file:
                for w in write:
                    file.writelines(str(w) + "\n")
                print("删除成功")
        else:
            print("\033[0;31;40m{0}\033[0m".format("用户不存在"))

    @classmethod
    def updateStu(self, id, name, java, python):
        fileName = os.getcwd() + "\\studentInfo.txt"
        write = []
        ##以这个格式打开之后 写入也是这个格式
        with open(fileName, "r", encoding="utf-8") as file:
            lines = file.readlines()
            if lines.__len__() == 0:
                write.append({"id": id, "name": name, "java": java, "python": python})
            else:
                for l in lines:
                    ## 字符串转字典
                    l_dic = eval(l)
                    if (l_dic.get("id") == str(id) or l_dic.get("name") == str(name)):
                        write.append({"id": id, "name": name, "java": java, "python": python})
                    else:
                        write.append(l_dic)
        ##以这个格式打开之后 写入也是这个格式
        with open(fileName, "w+", encoding="utf-8") as file:
            for w in write:
                file.writelines(str(w) + "\n")

    @classmethod
    def checkWrite(self, id, name, java, python):
        fileName = os.getcwd() + "\\studentInfo.txt"
        write = []
        ##以这个格式打开之后 写入也是这个格式
        with open(fileName, "r", encoding="utf-8") as file:
            lines = file.readlines()
            if lines.__len__() == 0:
                write.append({"id": str(id), "name": name, "java": java, "python": python})
            else:
                insertFlag = True
                for l in lines:
                    ## 字符串转字典
                    l_dic = eval(l)
                    if (l_dic.get("id") == str(id)):
                        insertFlag = False
                        write.append({"id": str(id), "name": name, "java": java, "python": python})
                    else:
                        write.append(l_dic)
                if insertFlag:
                    write.append({"id": str(id), "name": name, "java": java, "python": python})

        ##以这个格式打开之后 写入也是这个格式
        with open(fileName, "w+", encoding="utf-8") as file:
            for w in write:
                file.writelines(str(w) + "\n")


def printDashboard(title):
    os.system('CLS')
    print("======================================================")
    print("====================\033[0;31;40m{0}\033[0m========================".format(title))
    print("======================================================")
    print("----------------------功能菜单-------------------------")
    print("1-录入学生")
    print("2-查询学生")
    print("3-删除学生")
    print("4-修改学生")
    print("5-排序")
    print("6-显示学生总数")
    print("7-显示学生信息")
    print("0-推出")
    print("------------------------------------------------------")
    inputStr = input("请选择:")
    try:
        inputNum = int(inputStr)
        if StudentSystemUtil.checkInputStr(inputNum):
            return inputNum
        else:
            return printDashboard("请输入正确的数字")
    except:
        return printDashboard("请输入正确的数字")


def deleteStudent():
    print("======================================================")
    studentInfo = input("请输入学生id 或 姓名:")
    if studentInfo:
        DiskUtil.delStu(studentInfo)
    else:
        print("======================================================")
        print("未查询到学生")
    if continueInput("删除"):
        deleteStudent()


def sortStudent():
    print("======================================================")
    studentInfo = input("按照python(1) 还是java(2) 排序？")
    if studentInfo == '1' or studentInfo == '2':
        sort = input("按照降序（1）还是升序（2）？")
        sortKey = "java" if studentInfo == '2' else "python"
        mode = True if sort == '1' else False
        DiskUtil.sortStu(sortKey, mode)
        if continueInput("排序"):
            sortStudent()

    else:
        print("请按照要求输入排序字段")


def updateStudent():
    print("======================================================")
    studentInfo = input("请输入学生id:")
    if studentInfo:
        stu = DiskUtil.queryStu(studentInfo)
        if stu:
            student = getUserInputStudent(False)
            DiskUtil.checkWrite(studentInfo, student["name"], student["javaScope"], student["pythonScope"])
        else:
            print("======================================================")
            print("未查询到学生")
    else:
        print("======================================================")
        print("未查询到学生")

    if continueInput("修改"):
        updateStudent()


## 传入id或者姓名查询用户
def searchStudent():
    print("======================================================")
    studentInfo = input("请输入学生id 或 姓名:")
    stuDic = DiskUtil.queryStu(studentInfo)
    if stuDic:
        print(stuDic)
    else:
        print("未查询到用户")
    if continueInput("查询"):
        searchStudent()


def getUserInputStudent(needId):
    student = {}
    while True:
        if needId:
            ## id
            stuId = input("请输入学生id:")
            if not stuId:
                print("\033[0;31;40m id不可为空！\033[0m")
                continue
            else:
                try:
                    ##给字典增加字段
                    student["stuId"] = int(stuId)
                except BaseException as e:
                    print(e)
                    print("\033[0;31;40m请输入正确格式的id\033[0m")

        studentName = input("请输入学生姓名:")
        if not studentName:
            print("\033[0;31;40m学生姓名不可为空！\033[0m")
            continue
        student["name"] = studentName

        javaScope = input("java得分:")
        try:
            if not javaScope:
                print("\033[0;31;40mjava得分不可为空！\033[0m")
                continue
            else:
                student["javaScope"] = int(javaScope)
        except:
            print("\033[0;31;40mjava得分格式有误\033[0m")
            continue

        pythonScope = input("python得分:")
        try:
            if not pythonScope:
                print("\033[0;31;40m python得分不可为空！\033[0m")
                continue
            else:
                student["pythonScope"] = int(pythonScope)
        except:
            print("\033[0;31;40m python得分格式有误\033[0m")
            continue
        break
    return student


def insertStudent():
    student = getUserInputStudent(True)
    DiskUtil.checkWrite(student["stuId"], student["name"], student["javaScope"], student["pythonScope"])
    if continueInput("新增"):
        insertStudent()


# 是否继续输入
def continueInput(name):
    print("======================================================")
    continueInput = input("是否继续{0}? y/n".format(name))
    if (continueInput == 'y'):
        return True
    elif (continueInput == 'n'):
        return False
    else:
        print("\033[0;31;40m 输入有误默认继续输入\033[0m")
        return True


def getInputStr(inputNum):
    # print("输入了{0}".format(inputNum))
    # 录入学生
    if inputNum == 1:
        insertStudent()
    # 2-查询学生
    elif inputNum == 2:
        searchStudent()
    elif inputNum == 3:
        deleteStudent()
    elif inputNum == 4:
        updateStudent()
    elif inputNum == 5:
        sortStudent()
    elif inputNum == 6:
        pass
    elif inputNum == 7:
        pass
    elif inputNum == 0:
        pass


##确认是否继续
def checkExitSystem(title="您确定要退出系统吗？  y/n"):
    inputStr = input(title)
    if ("n" == inputStr or "N" == inputStr):
        return False
    elif ("y" == inputStr or "Y" == inputStr):
        return True
    else:
        return checkExitSystem("请输入 y/n")


if __name__ == '__main__':
    while True:
        inputNum = printDashboard("学生管理菜单")
        if (0 == inputNum):
            exitSystem = checkExitSystem()
            # 退出程序
            if (bool(exitSystem)):
                break
        else:
            getInputStr(inputNum)
