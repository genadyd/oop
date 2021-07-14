"""
get into class, object of another class, as param
"""


class Point:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    # overload standard method "__str__"

    def __str__(self):
        return f"({self.__x}, {self.__y})"


class Figure:
    def __init__(self, sp: Point, ep: Point, color: str = "red", width: int = 1):
        self._sp = sp
        self._ep = ep
        self._color = color
        self._width = width

    def draw(self):
        pass


class Line(Figure):
    __message_text = 'Line Draw: '

    def draw(self):
        print(f"{Line.__message_text} {self._sp}, {self._ep}, {self._color}, {self._width}")


class Rect(Figure):
    __message_text = 'Rect Draw: '

    def __init__(self, sp: Point, ep: Point or None, rect_size=[], color: str = "red", line_width: int = 1):
        self.__rect_height = rect_size[0]
        self.__rect_width = rect_size[1]
        super().__init__(sp, ep, color, line_width)

    def draw(self):
        print(f"{Rect.__message_text} {self._sp}, {self._color}, {self._width}, {[self.__rect_height, self.__rect_width]}")


line = Line(Point(34, 45), Point(12, 16))
line.draw()

rect = Rect(Point(123, 44), None, [35, 66])
rect.draw()
