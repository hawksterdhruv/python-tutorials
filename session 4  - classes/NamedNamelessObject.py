class MyClass:

    def display(self):
        print('Good Morning')
c1 = MyClass()
c2 = MyClass()
c1.display()
MyClass().display()
c3 =c1
print (id(c1))
print (id(c2))
print (id(c3))

print(c1 is c2)
print(c1 is c3)

print(c1 is not  c2)
print(c1 is not c3)


