class Animal(object):
    def run(self):
        print("Animal is running...")


class Dog(Animal):

    def __len__(self):
        return 100

    def run(self):
        print('Dog is running...')

    def eat(self):
        print('Eating meat...')


class Cat(Animal):

    def run(self):
        print('Cat is running...')


class Tortoies(Animal):

    def run(self):
        print('Tortoies is running...')


class Timer(object):
    def run(self):
        print("Start...")


#
def run_twice(animal):
    animal.run()
    animal.run()

print(Dog().__len__())