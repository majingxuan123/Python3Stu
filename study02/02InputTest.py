from decimal import Decimal;

inputStr = input("fil现在多少刀? \n")
print(inputStr)
d = Decimal(inputStr) * Decimal("6.55");
print("价值人民币"+str(d));



