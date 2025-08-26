class PersonTest:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 当获取属性的时候就会执行当前方法
    def __getattribute__(self, item):
        if item == 'name':
            return 'Tom'
        else:

            #  return self.name 不能这样写 只能写下面的方法
            return object.__getattribute__(self, item)

    def __setattr__(self, key, value):
        if key == 'name':
            object.__setattr__(self, key, value)
            # raise AttributeError('name is readonly')
        else:
            object.__setattr__(self, key, value)

if __name__ == '__main__':
    p = PersonTest('JAY', 18)
    print(p.name)
    print(p.age)
