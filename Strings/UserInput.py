# By default , input() will always takes an input as a String.
# Whatever you enter, it will be treated as string

num1 = input('Enter the num1: ')
print('Value of num1 is: ', num1, '\nData type of num1 is: ', type(num1)) 
#type : <class 'str'>


# So we typecast the user input , in whatever datatype we want
# here, "int()" method is used to typecast the user input into "int" data type
num2 = int(input('Enter the num2: '))
print('Value of num2 is: ', num2, '\nData type of num2 is: ', type(num2))
#type : <class 'int'> 


