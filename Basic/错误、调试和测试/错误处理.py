# try:
#     print("try...")
#     r = 10 / 2
#     print("result:", r)
# except ValueError as e:
#     print("Value Error:", e)
# except ZeroDivisionError as e:
#     print("except:", e)
# # 如果没有错误发生，可以在except语句块后面加一个else，当没有错误发生时，会自动执行else语句
# else:
#     print("no error")
# finally:
#     print("finally...")
# print("end")

#
#
import logging


def foo(s):
    return 10 / int(s)


def bar(s):
    return foo(s) * 2


def main():
    try:
        bar("0")
    except Exception as e:
        logging.exception(e)


main()
print("end")


#
# 如果要抛出错误，首先根据需要，可以定义一个错误的class，
# 选择好继承关系，然后，用raise语句抛出一个错误的实例：
class FooError(ValueError):
    pass


def foo(s):
    n = int(s)
    if n == 0:
        raise FooError("invalid value: %s" % s)
    return 10 / n

foo("0")