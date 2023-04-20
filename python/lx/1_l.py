class Student(object):
    @property
    def birth(self):
        return self._birth
    @birth.setter
    def birth(self,value):
        self._birth = value
    @property
    def age(self):
        return 2022 - self._birth
    # @property
    # def score(self):
    #     return self._score
    # @score.setter
    # def score(self,value):
    #     if not isinstance(value,int):
    #         raise Exception
    #     if value < 0 or value > 100:
    #         raise Exception
        self._score= value
s = Student()
s.score =999
print(s.score)