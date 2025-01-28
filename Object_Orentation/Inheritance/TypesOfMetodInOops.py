class Student:
    def cook(self):
        print("Student is cooking")
    def play(self):
        print("Student is playing")

class Employee(Student):
    def work(self):
        print("Employee is working")
    
    def cook(self):
        print("Employee is cooking")

e = Employee()
e.play()

'''
work() -> Specialized Method .. present only in the child class
play() -> Inherited Mehtod .. present only in the parent class 
Cook() -> Overriden Method .. child change the implementation of method defined in parent class

'''
