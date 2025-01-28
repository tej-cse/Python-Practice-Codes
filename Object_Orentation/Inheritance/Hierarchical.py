class Demo1:
    def disp1(self):
        print("Inside disp1 method")
    
class Demo2(Demo1):
    def disp2(self):
        print("Inside disp2 method")

class Demo3(Demo1):
    pass

obj1 = Demo2()
obj1.disp1()
obj1.disp2()

obj2 = Demo3()
obj2.disp1()