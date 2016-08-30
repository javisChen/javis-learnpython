from io import BytesIO
from io import StringIO

f = StringIO('Hello!\nHi!\nGoodbye!')
print(f.getvalue())
while True:
    s = f.readline()
    if s =="":
        break
    print(s.strip())

f = BytesIO()
f.write('中文'.encode('utf-8'))
print(f.getvalue())
