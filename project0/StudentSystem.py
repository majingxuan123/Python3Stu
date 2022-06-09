import os

import util.StudentSystemUtil as stuUtil


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
        if stuUtil.StudentSystemUtil.checkInputStr(inputNum):
            return inputNum
        else:
            return printDashboard("请输入正确的数字")
    except:
        return printDashboard("请输入正确的数字")


def insertStudent():
    while True:
        student = {}
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
        stuUtil.DiskUtil.insertStu(stuId, studentName, javaScope, pythonScope)


def getInputStr(inputNum):
    print("输入了{0}".format(inputNum))
    # 录入学生
    if inputNum == 1:
        insertStudent()
    elif inputNum == 2:
        pass
    elif inputNum == 3:
        pass
    elif inputNum == 4:
        pass
    elif inputNum == 5:
        pass
    elif inputNum == 6:
        pass
    elif inputNum == 7:
        pass
    elif inputNum == 0:
        pass


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
