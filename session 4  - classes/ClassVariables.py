i,j = 15,25
class MyClass:
    a,b = 10,20  #class variables

    def add(self, x, y):
        print(x + y)             #accessing local variables
        print(self.a + self.b)   #accessing class variables
        print(i + j)             #accessing global variables
    def mul(self):
        print(self.a*self.b)


mc = MyClass()
mc.add(2,3)
mc.mul()

