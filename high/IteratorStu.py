from collections.abc import Iterable

lst = [1,2,3,4,5,6,7]
dic = {"a":1,"b":2,"c":3,"d":4,"e":5}
print(isinstance(lst,Iterable))
print(isinstance("abc",Iterable))

iterObj = iter(lst)
print(isinstance(lst,Iterable))

print(iterObj.__next__())
print(iterObj.__next__())
