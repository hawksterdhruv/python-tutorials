class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname):
      Person.__init__(self, fname, lname)

class Teacher (Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year

    def welcome(self):
        print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

 # Use the Person class to create an object, and then execute the printname method:
x = Person("John", "Doe")
x.printname()
y = Student("Mike", "Olsen")
y.printname()

z= Teacher("Nick", "Jackson", 2019)
z.printname()
z.welcome()

#If you add a method in the child class with the same name as a function in the parent class, the inheritance of the parent method will be overridden.