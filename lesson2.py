# Class attributes

class Person:
    GENDER = "m"

    def __init__(self):
        self.__name = "Genady" """this is private attribute"""
        self.__age = 177
        self.address = 'Ehgjhg kjljkl jhjh 34'
        print("Object creating here =================")

    def __checkNumber(value=''):
        if isinstance(value, int) or isinstance(value, float):
            return True
        return False

    def setAge(self, value=''):
        if Person.__checkNumber(value):
            self.__age = value
            print('Changed')
        else:
            print('Type Error')
            return False

    def __getattribute__(self, item):  # method reload
        if item == "_Person__name":
            return "This is private"
        else:
            return object.__getattribute__(self, item)

    def __setattr__(self, key, value):
        if key == 'GENDER':
            print('CONST')
        else:
            self.__dict__[key] = value
        # print(key)


person = Person()

"""get private attr opportunity"""
print(person._Person__name)  # print "This is private"
"""get private attr opportunity"""
person.setAge()  # Print "Type Error"
person.setAge(44)  # Print "Changed"
print(person._Person__age)  # print 117
# get public attribute
print(person.address)  # print address var value
person.GENDER = 'w'
print(person.GENDER)
