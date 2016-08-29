from collections import Iterable

d = {'a': 1, 'b': 2, 'c': 3}

# dict默认迭代的是key
for key in d:
    print(key)

# 迭代value
for value in d.values():
    print(value)

# 迭代字符串
for ch in "ABC":
    print(ch)

# 如何判断一个对象是可迭代对象呢？方法是通过collections模块的Iterable类型判断
print(isinstance("abc", Iterable))
print(isinstance([1, 2, 3, 4, 5], Iterable))
print(isinstance(123, Iterable))

# 实现下标循环,使用enumerate
for i, value in enumerate(["A", "B", "C", "D", "E"]):
    print(i, value)

# 同时引用两个变量
for x, y in [(1, 1), (2, 4), (3, 9)]:
    print(x, y)
