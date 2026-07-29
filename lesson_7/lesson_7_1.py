class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def print_name(self):
    print(self.firstname, self.lastname)

class Student(Person):
    def __init__(self, fname, lname, no):
        super().__init__(fname, lname) #super() 就是呼叫父類別(Person)的 __init__
        self.no = no
  
  
    def print_no(self):
  	    print(self.no)
  
  
class Teacher(Person):
  pass


class GoodStudent(Student):
  pass


p1 = Person("John", "Doe")
p1.print_name()

x = Student("Mike", "Olsen", "002")
x.print_name()
x.print_no()

gs = GoodStudent("Andy", "Tseng", "001")
gs.print_name()
gs.print_no()