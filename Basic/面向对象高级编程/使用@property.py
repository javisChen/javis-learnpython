# 在绑定属性时，如果我们直接把属性暴露出去，
# 虽然写起来很简单，但是，没办法检查参数，导致可以把成绩随便改：

class Student(object):
    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError("socre must be integer")
        if value < 0 or value > 100:
            raise ValueError("score must between 0 - 100")
        self.__score = value

    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    @property
    def age(self):
        return 2015 - self._birth


s = Student()
# 实际转化为s.set_score(60)
s.score = 100
# 实际转化为s.get_score()
s.birth = 100
print(s.score)
print(s.age)


# 练习
class Screen(object):
    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, width):
        self._width = width

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, height):
        self._height = height

    @property
    def resolution(self):
        return self._width * self._height


s = Screen()
s.width = 100
s.height = 768
print(s.resolution)
assert s.resolution == 786432, "1024 * 768 = %d ?" % s.resolution
