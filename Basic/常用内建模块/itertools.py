import itertools

# cycle()会把传入的一个序列无限重复下去：
natuals = itertools.cycle("ABC")
# for n in natuals:
#     print(n)

# count()会创建一个无限的迭代器，所以上述代码会打印出自然数序列
natuals = itertools.count(1)
# for n in natuals:
#     print(n)

# repeat()负责把一个元素无限重复下去，不过如果提供第二个参数就可以限定重复次数
ns = itertools.repeat("A", 3)
for n in ns:
    print(n)

# takewhile
natuals = itertools.count(1)
ns = itertools.takewhile(lambda x: x <= 10, natuals)
print(list(ns))


# chain
for c in itertools.chain("ABC", "XYZ"):
    print(c)


# groupby
for key, group in itertools.groupby('AAABBBCCAAA'):
    print(key, list(group))

for key, group in itertools.groupby('AaaBBbcCAAa', lambda c: c.upper()):
    print(key, list(group))