class Demo1:
    def disp(self):
        print("Inside disp in demo1")

class Demo2:
    def disp(self):
        print("Inside disp in demo2")

class Demo3(Demo1,Demo2):
    pass

d3 = Demo3()

d3.disp()
