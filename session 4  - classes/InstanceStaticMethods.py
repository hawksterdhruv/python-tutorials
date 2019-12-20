class MyClass:
    def m1(self):
        print('instance method')
    @staticmethod
    def m2():
        print('static method')
mc = MyClass()
mc.m1()
MyClass().m2()

