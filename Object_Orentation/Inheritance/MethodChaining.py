'''
    Method Chaining is the process of calling one method from anoter method.
'''
class GrandParent:
    def cook(self):
        print("GrandParent can cook Biryani")

class Parent(GrandParent):
    def cook(self):
        print("Parent can cook Maggi")
        #super().cook()

class Child(Parent):
    def cook(self):
        print("child won't cook")
        super().cook()
        super(Parent, self).cook() # Grandparent class cook method will be called

c = Child()
c.cook()

