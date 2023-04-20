class Screen(object):
    @property
    def width(self):
        return self._width
    @property
    def height(self):
        return self._height
    @width.setter
    def width(self,value):
        self._width=value
    @height.setter
    def height(self,value):
        self._height=value
    @property
    def resolution(self):
        return self._width * self.height
s = Screen()
s.width=10
s.height=20
print(s.resolution)
        
    