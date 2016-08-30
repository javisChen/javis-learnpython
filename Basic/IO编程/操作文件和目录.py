import os

print("当前系统:", os.name)
# windows不提供
# print("获取详细系统信息:", os.uname())
# 获取环境变量的值
print(os.environ)

# 查看当前目录的绝对路径:
print(os.path.abspath("."))
# 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来:
# print(os.path.join('/Test', 'text.txt'))
# 然后创建一个目录:
# os.mkdir('/Test/text.txt')
# 删除一个目录:
# os.rmdir("/Test")
# 拆分路径
# print(os.path.split("/Test/text.txt"))
# 文件重命名
# os.rename("/Test/text.txt", "test.txt")