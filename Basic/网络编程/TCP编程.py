import socket

# 客户端
# 创建一个socket
import threading
from datetime import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 建立连接
s.connect(("www.sina.com.cn", 80))
# 发送数据
s.send(b"GET / HTTP/1.1\r\nHost: www.sina.com\r\nConnection: close\r\n\r\n")
buffer = []
while True:
    # 每次最多接收1k字节
    d = s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break

data = b"".join(buffer)
s.close()
header, html = data.split(b"\r\n\r\n", 1)
print(header.decode("utf-8"))
with open("sina.html", "wb") as f:
    f.write(html)

