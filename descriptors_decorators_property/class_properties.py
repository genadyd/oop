#  Properties

class Point:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def __checkValue(val):
        return isinstance(val, int) or isinstance(val, float)

    def __getCoordX(self):
        return self.__x

    def __setCoordX(self, x):
        if Point.__checkValue(x):
            self.__x = x
        else:
            raise ValueError('Data format isn`t properly ')

    def __deletePropX(self):
       print('Property deleting')
       del self.__x

    coordX = property(__getCoordX, __setCoordX, __deletePropX)  # var x processing use coordX descriptor


pt = Point(2, 4)
pt.coordX = 150  # set value
x = pt.coordX  # read value
print(x)
del pt.coordX
pt.coordX = 7
print(pt.coordX)