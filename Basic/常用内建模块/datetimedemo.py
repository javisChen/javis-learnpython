from datetime import datetime

# 获取当前时间
now = datetime.now()
print(now)

# 要指定某个日期和时间，我们直接用参数构造一个
dt = datetime(2015, 4, 19, 12, 20) # 用指定日期时间创建datetime
print(dt)
print(dt.timestamp())

# timestamp转换为datetime
t = 1429417200.0
print(datetime.fromtimestamp(t))

# str转换为datetime
cday = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
print(cday)

# datetime转换为str
now = datetime.now()
print(now.strftime('%a, %b %d %H:%M'))

# datetime加减
now = datetime.now()
print(now)