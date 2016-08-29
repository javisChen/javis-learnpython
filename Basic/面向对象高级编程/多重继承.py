# 动物
class Animal(object):
    pass


# 大类
# 哺乳类
class Mammal(Animal):
    pass


# 鸟类
class Bird(Animal):
    pass


# 功能类
class RunnableMixin(object):
    def run(self):
        print("Running...")


class FlyableMixin(object):
    def fly(self):
        print("Flying...")


# 肉食和植食
class CarnivorousMixIn(object):
    pass


class CarnivorousMixIn(object):
    pass


# 动物子类(狗、鸟...)
class Dog(Mammal, RunnableMixin):
    pass


class Bat(Mammal, RunnableMixin):
    pass


class Parrot(Bird, FlyableMixin):
    pass


class Ostrich(Bird, FlyableMixin):
    pass
