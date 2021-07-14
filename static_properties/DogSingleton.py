class Dog:
    __instance = None
    __counter = 0
    __msg = ''

    def __init__(self):
        self.age = 33

    def __new__(cls, *args, **kwargs):
        if cls.__counter < 5:
            cls.__instance = super(Dog, cls).__new__(cls)
            cls.__counter += 1
            print('obj created')
        else:
            cls.__instance = None
            print('obj is not created')

    def setAge(self, val=15):
        self.age = val

    @staticmethod
    def getInstance():
        return Dog.__instance


prefix = 1
objects_collection = {}
while True:
    inst_name = 'dog' + str(prefix)
    d = Dog()
    print(d)
    i = Dog.getInstance()
    if isinstance(i, Dog):
        objects_collection[inst_name] = Dog.getInstance()
        prefix += 1
    else:
        break
print(len(objects_collection))
