import sys;
import os
import json

from trans.translate import Baidu_trans


def transJs(trans):
    f_new = open('../new_zh-CN.js', 'w+', encoding='utf-8')

    with open('zh-CN.js', 'r', encoding='utf8') as f:
        for line in f:
            print(line)
            if ((":" in line) and ('{' not in line)):
                first = line.find("'")
                end = line.rfind("'")
                left = line[:first];
                right = line[end:]
                transStr = line[first:end]
                trans_trans = trans.trans(transStr)
                tempOne = line.split(":")[0]
                tempTwo = line.split(":")[1].split(' ')
                for i in range(len(tempTwo)):
                    if ('\'' in tempTwo[i] and len(tempTwo[i]) > 1):
                        if (tempTwo[i][0] == '\''):
                            tempTwo[i] = tempTwo[i][0] + tempTwo[i][1:].capitalize()
                        else:
                            tempTwo[i] = tempTwo[i].capitalize()
                    else:
                        tempTwo[i] = tempTwo[i].capitalize()

                print(tempOne + ': ' + (' ').join(tempTwo))

                transStr = str(trans_trans["result"]["dst"])
                if (transStr.find("'") != -1):
                    transStr.replace("'", "\'")
                f_new.write(left + transStr +right)
            else:
                f_new.write(line)
                print()


if __name__ == '__main__':
    trans = Baidu_trans()
    transJs(trans)
