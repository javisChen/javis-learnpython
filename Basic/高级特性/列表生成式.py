import os

print(list(range(1, 11)))


# 生成[1x1, 2x2, 3x3, ..., 10x10]
# 方法1:
L = []
for i in range(1, 11):
    L.append(i * i)
print(L)

# 方法2:
print([x * x for x in range(1, 11)])

# 筛选出偶数
print([x * x for x in range(1, 11) if x % 2 == 0])

# 使用两层循环可以生成全排列
print([m + n for m in "ABC" for n in "XYZ"])

# 列出当前目录下的所有文件和目录名
print([d for d in os.listdir(".")])

# 同时迭代key和value
d = {'x': 'A', 'y': 'B', 'z': 'C'}
print([k + "=" + y for k, y in d.items()])

# 把一个list中所有的字符串变成小写
L = ['Hello', 'World', 'IBM', 'Apple']
print([s.lower() for s in L])

# 把list中英文转换为小写
L = ['Hello', 'World', 18, 'Apple', None]
print([s.lower() for s in L if isinstance(s, str)])
