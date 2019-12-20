class Base:
    def __init__(self):
        # Protected member
        self._a = 2             #protected member
        self.__c = "GeeksforGeeks"    #private member


# Creating a derived class
class Derived(Base):
    def __init__(self):
        # Calling constructor of
        # Base class
        Base.__init__(self)
        print("Calling protected member of base class: ")
        print(self._a)


obj1 = Derived()
obj2 = Base()
print(obj2._a)
print(obj1.__c)
