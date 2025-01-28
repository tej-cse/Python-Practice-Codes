class Demo1:
    def __init__(self):
        self.x = 100

class Demo2:
    def __init__(self):
        self.x = 200

class Demo3(Demo2,Demo1):
    def __init__(self):
        self.x = 300

d3 = Demo3()
print(d3.x)