class Point:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y


# check the class father (default "object")
print(issubclass(Point, object))
