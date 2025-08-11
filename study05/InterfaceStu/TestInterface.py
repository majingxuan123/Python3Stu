from study05.InterfaceStu.AC import AC
from study05.InterfaceStu.GreenAC import GreenAC
from study05.InterfaceStu.XiaomiAC import XiaomiAC


# 多态
def acCool(ac: AC):
    ac.cool()


if __name__ == '__main__':
    GreenAC = GreenAC()
    XiaomiAC = XiaomiAC()

    acCool(GreenAC)
    acCool(XiaomiAC)
