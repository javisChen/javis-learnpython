from collections import Iterable, Iterator

# 可以使用isinstance()判断一个对象是否是Iterable对象
print(isinstance([], Iterable))
print(isinstance([], Iterable))
print(isinstance("abc", Iterable))
print(isinstance((x for x in range(10)), Iterable))
print(isinstance(100, Iterable))

# 可以使用isinstance()判断一个对象是否是Iterator对象
print("=============================================")
print(isinstance((x for x in range(10)), Iterator))
print(isinstance([], Iterator))
print(isinstance({}, Iterator))
print(isinstance('abc', Iterator))

x = iter((12, 3, 45, 6))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
