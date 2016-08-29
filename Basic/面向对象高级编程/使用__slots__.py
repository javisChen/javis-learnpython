from types import MethodType


class Student(object):
    # 使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的：
    __slots__ = ("name", "age")



def set_age(self, age):
    self.age = age


def set_score(self, score):
    self.score = score



# 给实例绑定一个方法
s = Student()
# s.name = "javis"
# s.age = 25
s.score = 99
# print(s.age)

# 给一个实例绑定的方法，对另一个实例是不起作用的
s2 = Student()
# s2.name = "javis"
# s2.set_age = MethodType(set_age, s)
# s2.set_age(25)
# print(s2.age)

# 为了给所有实例都绑定方法，可以给class绑定方法
Student.set_score = set_score

# s.set_score(100)
# s2.set_score(99)
# print(s2.score)
# print(s.score)


class GraduateStudent(Student):
    pass

g = GraduateStudent()
g.score = 999
print(g.score)