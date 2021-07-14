#  Descriptors
class PointCoord:
    def __init__(self, name):
        self.__name = name

    def __get__(self, instance, owner):
        print('Get the val: '+self.__name)
        return instance.__dict__[self.__name]

    def __set__(self, instance, value):
        print('Set the val: ' + str(value) + ' to: ' + str(self.__name))
        instance.__dict__[self.__name] = value


class Point:
    coordX = PointCoord("__x")
    coordY = PointCoord("__y")

    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y


pt = Point(2, 4)
pt.coordX = 150  # set value
pt.coordY = 13  # set value
print([pt.coordX, pt.coordY])

# pt1 = Point(23, 45)
# pt1.coordX = 1234  # set value
# pt1.coordY = 1233  # set value
# print([pt1.coordX, pt1.coordY])
