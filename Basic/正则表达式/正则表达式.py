import re

s = r"ABC\-001"
print(re.match(r"^\d{3}-\d{3,8}$", "010-12345"))
test = "用户输入的字符串"
if re.match(r"正则表达式", test):
    print("ok")
else:
    print("fail")

print("a b   c".split(" "))
print(re.split(r'\s+', 'a     b         c'))
print(re.split(r'[\s\,]+', 'a,b, ,,, c  d'))
# 注意到group(0)永远是原始字符串，group(1)、group(2)……表示第1、2、……个子串。
m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')
print(m.group(0))
print(m.group(1))
print(m.group(2))