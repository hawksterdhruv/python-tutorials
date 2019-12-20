x,y = 15,25
class MyClass:
    x,y = 10,20  #class variables

    def add(self, x, y):
        print(x + y)             #accessing local variables
        print(self.x + self.y)   #accessing class variables
        print(globals()['x'] + globals()['y'])             #accessing global variables
    def mul(self):
        print(self.x*self.y)


mc = MyClass()
mc.add(2,3)
mc.mul()

