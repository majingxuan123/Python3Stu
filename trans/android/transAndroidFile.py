import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element
from trans.translate import Baidu_trans
import os


def trans_xml(fileName, toLange):
    tree = ET.parse(fileName)
    root = tree.getroot()
    trans = Baidu_trans()
    for child in root:
        if (child.text != ""):
            try:
                print("++++++++{0}+++++++++".format(child.text))
                trans_trans = trans.trans_to_lang(child.text, toLange)
                child.text = trans_trans["result"]["dst"]
            except BaseException as e:
                print("tag:", child.tag)
                print("text:", child.text)
                print("attrib:", child.attrib)
                print("attrib:", child)
                print(e)
                pass
    tree.write(fileName + "." + toLange, encoding="utf-8", xml_declaration=True)


def trans_xml_tolang(fileName, tolang):
    tree = ET.parse(fileName)
    root = tree.getroot()
    trans = Baidu_trans()
    for child in root:
        if (child.text != ""):
            try:
                print("++++++++{0}+++++++++".format(child.text))
                trans_trans = trans.trans_to_lang(child.text, tolang)
                child.text = trans_trans["result"]["dst"]
            except BaseException as e:
                print("tag:", child.tag)
                print("text:", child.text)
                print("attrib:", child.attrib)
                print("attrib:", child)
                print(e)
                pass
    tree.write(fileName + ".bak", encoding="utf-8", xml_declaration=True)


if __name__ == '__main__':

    list = ["cht", "en", "jp", "kor", "th", "vie", "id", "tr", "de", "fra", "pt", "fil", "ara", "may", "ru", "spa"]
    for l in list:
        trans_xml("strings.xml", l)
