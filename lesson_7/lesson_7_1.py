class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
    def __init__(self, fname, lname, no):
        super().__init__(fname, lname)
        self.no = no
  
  
    def printno(self):
  	    print(self.no)
  
  
class Teacher(Person):
  pass


class GoodStudent(Student):
  pass


p1 = Person("John", "Doe")
p1.printname()

x = Student("Mike", "Olsen", "002")
x.printname()
x.printno()

gs = GoodStudent("Andy", "Tseng", "001")
gs.printname()
gs.printno()