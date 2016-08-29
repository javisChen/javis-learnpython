from functools import reduce

def f(x):
    return x * x

# map()传入的第一个参数是f，即函数对象本身。由于结果r是一个Iterator，Iterator是惰性序列，因此通过list()函数让它把整个序列都计算出来并返回一个list。
print(list(map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])))

#
print(list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])))


def add(x, y):
    return x * 10 + y

print(reduce(add, [1, 2, 3, 4, 5]))


def fn(x, y):
    return x * 10 + y


def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
print(reduce(fn, map(char2num, "135793")))

def str2int(s):
    # def fn(x, y):
    #     return x * 10 + y
    def char2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))
    # return reduce(fn, map(char2num, s))

print(str2int("12345"))

# 练习题

# 利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字
def normalize(L):
    return L[0:1].upper() + L[1:].lower()
L = ['JAViS', 'LSDASDqwqeSDdQWEQWSQqwe', 'eqwewAsASAdc']
print(list(map(normalize, L)))


# 请编写一个prod()函数，可以接受一个list并利用reduce()求积
def prod(L):
    return reduce(lambda x, y: x * y, L)

print(prod([3, 5, 7, 9]))


# 利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456
def str2float(L):
    if L.__contains__("."):
        return reduce(lambda x, y: x + "." + y, map(lambda array: array, L.split(".")))
    else:
        print("请输入浮点参数")
print(str2float('123.44456'))
