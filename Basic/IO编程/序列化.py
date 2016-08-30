import json
import pickle

# 把对象序列化
d = dict(name="javis", age=20, score=88)
print(pickle.dumps(d))

# f = open("dump.txt", "wb")
# pickle.dump(d, f)
# f.close()

# 反序列化
f = open("dump.txt", "rb")
d = pickle.load(f)
f.close()
print(d)

# Json
d = dict(name="javis", age=20, score=88)
print(json.dumps(d))

#
json_str = '{"age": 20, "score": 88, "name": "Bob"}'
print(json.loads(json_str))


#
class Student(object):

    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score


# 专门写一个方法转换函数
def dict2student(d):
    return Student(d['name'], d['age'], d['score'])


s = Student("javis", 20, 88)
print(json.dumps(s, default=lambda obj: obj.__dict__))
