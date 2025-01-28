class Student:
    college_name = "Kodnest"

    def get_info(self):
        print('college Name is: ', Student.college_name)

    @classmethod
    def change_name(cls, new_name):
        cls.college_name = new_name
    
s1 = Student()
s1.get_info() #college Name is:  Kodnest

Student.change_name('Code') # Changin the value of static variable using a static method
s1.get_info() # college Name is:  Code