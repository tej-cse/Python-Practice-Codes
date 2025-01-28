class MathOperations:
    # @staticmethod -> this is called as decorator
    # for making a method static , this decorator must be defined above the method definition
    # "self" parameter is not required to static methods
    @staticmethod
    def add_numbers(a, b):
        return a+b
    
    def calci(self):
        pass

# static method can be called by just using class name , without creating any object
result = MathOperations.add_numbers(5, 3)
print(result)

# static methods like static variable can also be called , using object reference variable(same is true in java) 
math_op = MathOperations()
print(math_op.add_numbers(10,5))