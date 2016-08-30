import os

# 打开文件, r表示读, rb读二进制
# read()方法读取文件的全部内容
with open('/text.txt', 'r') as f:
    for line in f.readlines():
        print(line.strip())
try:
    f = open('/text.txt', 'r', encoding="gbk", errors="ignore")
    print(f.read())
finally:
    if f:
        f.close()

# 写入文件
with open('/text.txt', 'w') as f:
    f.write("hello world")

