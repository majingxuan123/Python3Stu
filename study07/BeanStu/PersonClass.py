class Person:
    def __init__(self, name, age, bag):
        self._name = name
        self._age = age
        self._bag = bag


    @property
    def name(self):
        if not hasattr(self, '_name'):
            return None
        return self._name

    @name.setter
    def name(self, name):
        print('set name')
        self._name = name

    @name.deleter
    def name(self):
        print('del name')
        del self._name

    @property
    def age(self):
        if not hasattr(self, '_age'):
            return None
        return self._age

    @age.setter
    def age(self, age):
        print('set age')
        self._age = age

    @age.deleter
    def age(self):
        print('del age')
        del self._age

    @property
    def bag(self):
        if not hasattr(self, '_bag'):
            return None
        return self._bag

    @bag.setter
    def bag(self, bag):
        print('set bag')
        self._bag = bag

    @bag.deleter
    def bag(self):
        print('del bag')
        del self._bag

    def __repr__(self):
        name = self.name if hasattr(self, '_name') else 'Unknown'
        age = self.age if hasattr(self, '_age') else 'Unknown'
        bag = self.bag if hasattr(self, '_bag') else 'Unknown'
        return f'Person: {name} {age} {bag}'

if __name__ == '__main__':
    p1 = Person('Tom', 18, 'Bag')
    print(p1.name)
    p1.name = 'Jerry'
    del p1.name

    print(p1)