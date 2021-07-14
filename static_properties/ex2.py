class Point:
    __count = 0  # static var

    def __init__(self):
        Point.__count += 1

    def getCount(self):
        return self.__count


pt = Point()
pt1 = Point()
pt2 = Point()
print(pt.getCount(), Point.getCount(pt), Point.getCount(Point))
