from functools import reduce


def lambdaStu(x):
    return x ** 2

def reduceStu(a,b):
    return a * b

if __name__ == '__main__':
    # 列表推导式
    lst = [(lambda x: x) (x) for x in range(10) ]
    print(lst)

    # 排序
    lst1 = [(1,20),(3,40),(2,30),(4,50)]
    lst1.sort(key=lambda x:x[1])
    print(lst1)

    # 映射
    numbers = [1,2,3,4,5,6]
    mapping1 = map(lambda x:x**2,numbers)
    print(list(mapping1))

    # 直接用方法也可以  map方法  对列表中每个对象都执行某个方法
    mapping2 = map(lambdaStu,numbers)
    print(list(mapping2))

    # 对list中累计 1*2*3*4*5*6
    lst3 = reduce(reduceStu,numbers)
    print(lst3)