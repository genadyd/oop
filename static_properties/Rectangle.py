class Rectangle:

    def __init__(self, w=0, h=0):
        self.area = Rectangle.getArea(w, h)

    @staticmethod
    def getArea(w, h):
        return w * h


ar = Rectangle(3, 10)
print(ar.area)
ar1 = Rectangle(124, 345)
print(ar1.area)
# print(Rectangle.area)
