class Point:
    __count = 0
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not isinstance(cls.__instance, cls):
            cls.__instance = super(Point, cls).__new__(cls)
            print("Object created !!!!")
        else:
            print("Object of Point class not created !!!!")
        Point.__count += 1

    @staticmethod
    def getCount():
        return Point.__count


pt1 = Point()
pt2 = Point()
pt3 = Point()
pt4 = Point()
pt5 = Point()
pt6 = Point()
print(Point.getCount())
print(id(pt1), id(pt2), id(pt3), id(pt4), id(pt5), id(pt6))
