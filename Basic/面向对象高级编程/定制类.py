# __str__()返回用户看到的字符串
# ，而__repr__()返回程序开发者看到的字符串，
# 也就是说，__repr__()是为调试服务的
class Student(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "Student object (name: %s)" % self.name

    __repr__ = __str__


s = Student("javis")
print(s)


# __iter__
class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1  # 初始化两个计数器a，b

    def __iter__(self):
        return self

    def __next__(self):

        self.a, self.b = self.b, self.a + self.b  # 计算下一个值
        if self.a > 100000:
            raise StopIteration()
        return self.a

    def __getitem__(self, item):
        if isinstance(item, int):
            a, b = 1, 1
            for x in range(item):
                a, b = b, a + b
            return a
        if isinstance(item, slice):
            start = item.start
            stop = item.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L


print(Fib()[0:5])


# __getattr__
# 当调用不存在的属性时，比如score，Python解释器会试图调用__getattr__(self, 'score')来尝试获得属性
# 返回函数也是完全可以的
class Student(object):

    def __init__(self):
        self.name = 'Michael'

    def __getattr__(self, attr):
        if attr == "score":
            return 99
        if attr == "age":
            return lambda: 25
        raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)

s = Student()
print(s.score)
# print(s.abs)

# 利用完全动态的__getattr__
class Chain(object):

    def __init__(self, path=""):
        self.__path = path

    def __getattr__(self, path):
        return Chain("%s/%s" % (self.__path, path))

    def __str__(self):
        return self.__path

    __repr__ = __str__


print(Chain().status.user.timeline.list)

# __call__
class Student(object):
    def __init__(self, name=""):
        self.name = name

    def __call__(self):
        print('My name is %s.' % self.name)

s = Student("javis")
s()

# 我们需要判断一个对象是否能被调用，能被调用的对象就是一个Callable对象
# 通过callable()函数，我们就可以判断一个对象是否是“可调用”对象。
print(callable(None))
