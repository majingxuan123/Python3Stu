from study05.InterfaceStu.AC import AC


class GreenAC(AC):

    name = "格力空调"

    def cool(self):
        print(f"{self.name}正在制冷")

    def hot(self):
        print(f"{self.name}正在制热")