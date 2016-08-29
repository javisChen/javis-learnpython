# 判断对象类型,使用type
import types

# print(type(123))
#
# print(type(123) == type(456))
# print(type(123) == int)
# print(type(123) == str)

# 判断一个对象是否函数
x = print(dir(123))


def fn():
    pass

print(type(fn) == types.FunctionType)
print(type(abs) == types.BuiltinFunctionType)
print(type(lambda x: x + x) == types.LambdaType)
print(type((x for x in range(10))) == types.GeneratorType)

# 或者
print(isinstance([1, 2, 3], (list, tuple)))


# dir()函数获取一个对象所有属性和方法
print(dir("ABC"))

# 仅仅把属性和方法列出来是不够的，配合getattr()、setattr()以及hasattr()，我们可以直接操作一个对象的状态
class MyObject(object):
    def __init__(self):
        self.x = 9

    def power(self):
        return self.x * self.x

obj = MyObject()

print(hasattr(obj, "x"))
print(hasattr(obj, "y"))
setattr(obj, "y", 10)
print(hasattr(obj, "y"))
print(getattr(obj, "y"))
getattr(obj, "z",000)

