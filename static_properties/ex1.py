class Point:
    count = 0
    count1 = 22


pt = Point()
pt1 = Point()
pt2 = Point()
print(Point.count1)
Point.count1 = 33  # change property in Class and in all object
pt1.count1 = 44  # change property in one object
pt.count = 10  # change property in one object (var count, this is only "pt" object var )
print(pt.count1, pt1.count1, pt2.count1)
