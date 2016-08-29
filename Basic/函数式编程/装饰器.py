# 定义一个能打印日志的decorator
import functools


# def log(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kw):
#         print("call %s()" % func.__name__)
#         return func(*args, **kw)
#
#     return wrapper
#
#
# @log
# def now():
#     print("2015-3-25")
# now()



# 由于log()是一个decorator，返回一个函数，
# 所以，原来的now()函数仍然存在，
# 只是现在同名的now变量指向了新的函数，
# 于是调用now()将执行新函数，即在log()函数中返回的wrapper()函数。
# wrapper()函数的参数定义是(*args, **kw)，
# 因此，wrapper()函数可以接受任意参数的调用。在wrapper()函数内，
# 首先打印日志，再紧接着调用原始函数。
# @log
# def now():
#     print("2015-3-25")
# now()

# 三层嵌套
def log(before="", after=""):
    def decorator(func, before=before, after=after):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print(before, func.__name__)
            func(*args, **kw)
            print(after, func.__name__)

        return wrapper

    if (isinstance(before, str) and isinstance(after, str)):
        return decorator
    else:
        return decorator(before, 'executed', '')


@log
def today():
    print('Aug 23')


today()
