class Demo:
    def disp(self):
        print('Inside disp with 0 parameters')
    def disp(self,a):
        print("Inside disp with 1 parameters")
    def disp(self,a,b):
        print("Inside disp with 2 parameters")

d = Demo()
d.disp() 
# gives error ,as in scripting languages method overloading is not allowed . 
# Only the last declared method will be considered

d.disp(10)  # gives error, for the same reason
d.disp(10,20)