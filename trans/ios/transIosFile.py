
from trans.translate import Baidu_trans
import os

trans = Baidu_trans()

def trans_ios(fileName):
    f_new = open('fileName'+'.bak', 'w+', encoding='utf-8')
    with open(fileName, 'r', encoding='utf8') as f:
        for line in f:
            print(line)
            if ((":" in line) and ('=' in line)):
                split = line.split("=")
                trans_trans = trans.trans(split[1])
                transStr = str(trans_trans["result"]["dst"])
                if (transStr.find("'") != -1):
                    transStr.replace("'", " ")
                f_new.write(transStr +'='+ split[0])
            else:
                f_new.write(line)
                print()

def trans_ios_tolang(fileName,toLang):
    f_new = open('fileName'+'.bak', 'w+', encoding='utf-8')
    with open(fileName, 'r', encoding='utf8') as f:
        for line in f:
            print(line)
            if ((":" in line) and ('=' in line)):
                split = line.split("=")
                trans_trans = trans.trans_to_lang(split[1],toLang)
                transStr = str(trans_trans["result"]["dst"])
                if (transStr.find("'") != -1):
                    transStr.replace("'", " ")
                f_new.write(transStr +'='+ split[0])
            else:
                f_new.write(line)
                print()

if __name__ == '__main__':
    files = print(os.listdir("./"))
    for f in files:
        if (".strings" in f):
            # trans_ios(f)
            trans_ios(f,"en")



