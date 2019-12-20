class A:
    def m1(self):
        print('this is m1 method from class A')
class B(A):
    def m2(self):
        print('m2 of class B')

obj1 = A()
obj2 = B()
obj1.m1()
obj2.m2()
obj2.m1()