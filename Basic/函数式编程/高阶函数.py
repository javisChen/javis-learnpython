print(abs(10))

print(abs)

x = abs(-10)
print(x)

f = abs
print(f)

f = abs
print(f(-10))

# 传入函数
# 既然变量可以指向函数，函数的参数能接收变量，那么一个函数就可以接收另一个函数作为参数，这种函数就称之为高阶函数。
# 一个最简单的高阶函数：
def add(x, y, f):
    return f(x) + f(y)

print(add(-5, 6, abs))