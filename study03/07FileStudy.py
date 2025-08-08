# r代表只读  w原有内容会被删除  文件会被我们覆盖写
# a 会被追加在文件之后
import time


def openFile(fileName):
    try:
        f = open(fileName, 'r', encoding='utf-8')
    except:
        print("文件不存在 已新建文件")
        f = open(fileName, 'w', encoding='utf-8')
    # 读所有
    print(f.read())
    # 读10字节
    print(f.read(10))
    # 读一行
    print(f.readlines())
    # 休眠10秒
    time.sleep(10)
    return f


def withOpenFile(filePath):
    # 使用withopen 会自动帮忙关闭
    with open(filePath, 'r', encoding='utf-8') as f:
        for line in f:
            print(line)
            # 关闭文件占用


def createFile(filePaht):
    f = open(filePaht, 'w', encoding='utf-8')
    f.write("hello world")
    f.flush()
    f.close()
