class MyClass:
    def m1(self):
        print('in m1 method')

    def __init__(self):
        print('in constructor')

    def __del__(self):
        print('in destructor')
    # def __str__(self):
    #     return('string variable')


mc = MyClass()
print(mc)
mc.m1()

