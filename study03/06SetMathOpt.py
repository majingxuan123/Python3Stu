##数学操作


s = {1,2,3,4}

s2 = {3,4,5,6,}

##  求s和s2的交集
print("求s和s2的交集:",s.intersection(s2))
print("求s和s2的交集:",s & s2)

print("s和s2的并集：",s.union(s2))
print("s和s2的并集：",s | s2)

print("s和s2的差集：",s.difference(s2))
print("s和s2的差集：",s - s2)

print("s和s2的对称差集：",s.symmetric_difference(s2))
print("s和s2的对称差集：",s ^ s2)
