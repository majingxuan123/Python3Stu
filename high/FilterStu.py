list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
f = filter(lambda x: x % 2 == 0, list1)
for i in f:
    print(i)
