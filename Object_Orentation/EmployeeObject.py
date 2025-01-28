class Employee:
    company_name = 'code' # class based variable , like static variable
    def __init__(self, name, age, desig ):
        self.name = name
        self.age = age
        self.desig = desig
    
    def getDetails(self):
        print("Employee Name: ", self.name)
        print("Employee Age: ", self.age)
        print("Employee Designation: ", self.desig)
    
    def login(self, time):
        print(f'{self.name} logged in at {time}')

    def logout(self, time):
        print(f'{self.name} logged out at {time}')
    
    def work(self, hours):
        print(f'{self.name} wroked for {hours}')


e1 = Employee("Tesuj",5,"SDE")
e2 = Employee("Ak",24,"SRE")
e3 = Employee("Pk",25,"Manager")
e4 = Employee("Rk",26,"Developer")

e1.getDetails()
e1.login("22:20")
e1.logout("10:20")
e1.work("8 hours")

print("\n------------------------------------\n")


e2.getDetails()
e2.login("10:20")
e2.logout("18:30")
e2.work("8 hours 10 minutes")

print("\n------------------------------------\n")


