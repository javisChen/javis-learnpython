# class Hello(object):
#     def hello(self, name='world'):
#         print('Hello, %s.' % name)

def fn(self, name='world'): # 先定义函数
    print('Hello, %s.' % name)


# 可以通过type()函数创建出Hello类
# 要创建一个class对象，type()函数依次传入3个参数：
# class的名称；
# 继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；
# class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上。
Hello = type("Hello", (object,), dict(hello=fn))

h= Hello()
h.hello()

# metaclass
class ListMetaclass(type):
    # __new__()方法接收到的参数依次是：
    # 当前准备创建的类的对象；
    # 类的名字；
    # 类继承的父类集合；
    # 类的方法集合。
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)


# 当我们传入关键字参数metaclass时，
# 魔术就生效了，它指示Python解释器在创建MyList时，
# 要通过ListMetaclass.__new__()来创建，在此，我们可以修改类的定义
class MyList(list, metaclass=ListMetaclass):
    pass

L = MyList()
L.add(1)
L.add(1)
L.add(1)
L.add(1)
print(L)
