from trans.translate import Baidu_trans
import os

trans = Baidu_trans()


def trans_ios(fileName):
    f_new = open('fileName' + '.bak', 'w+', encoding='utf-8')
    with open(fileName, 'r', encoding='utf8') as f:
        for line in f:
            print(line)
            if ((":" in line) and ('=' in line)):
                split = line.split("=")
                trans_trans = trans.trans(split[1])
                transStr = str(trans_trans["result"]["dst"])
                if (transStr.find("'") != -1):
                    transStr.replace("'", " ")
                f_new.write(transStr + '=' + split[0])
            else:
                f_new.write(line)
                print()


def trans_ios_tolang(fileName, toLang):
    f_new = open(fileName + "." + toLang, 'w+', encoding='utf-8')
    with open(fileName, 'r', encoding='utf8') as f:
        for line in f:
            if ('=' in line):
                split = line.split("=")
                trans_trans = trans.trans_to_lang(split[1], toLang)
                transStr = str(trans_trans["result"]["dst"])
                if (transStr.find("'") != -1):
                    transStr.replace("'", " ")
                fialStr = split[0] + '=' + transStr
                print(fialStr)
                f_new.write(fialStr + "\n")
            else:
                f_new.write(line)

if __name__ == '__main__':

    list = ["cht", "en", "jp", "kor", "th", "vie", "id", "tr", "de", "fra", "pt", "fil", "ara", "may", "ru"]
    for l in list:
        trans_ios_tolang("Localizable.strings", l)
