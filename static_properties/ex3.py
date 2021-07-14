class Point:
    __count = 0

    def __init__(self):
        Point.__count += 1

    @staticmethod
    def getCount():
        return Point.__count


pt = Point()
pt1 = Point()
pt2 = Point()
print(pt.getCount(), Point.getCount())
