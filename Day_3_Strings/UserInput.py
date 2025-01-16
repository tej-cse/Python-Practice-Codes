# By default , input() will always takes the input as a String.
# Whatever you enter, it will be treated as string

num1 = input('Enter the num1: ')
print('Value of num1 is: ', num1, '\nData type of num1 is: ', type(num1)) 
#type : <class 'str'>

num1 = int(input('Enter the num1: '))
print('Value of num1 is: ', num1, '\nData type of num1 is: ', type(num1))

# So we typecast the user input , in whatever datatype we want
# here, "int()" method is used to typecast the user input into "int" data type
num2 = int(input('Enter the num2: '))
print('Value of num2 is: ', num2, '\nData type of num2 is: ', type(num2))
#type : <class 'int'> 


#Adding two int variable , will give result as a int type
print(f'Addition of {num1} and {num2} is {num1+num2}')

#Substracting two int variable , will give result as a int type
print(f'Addition of {num1} and {num2} is {num1-num2}')

#Multiplying two int variable , will give result as a int type
print(f'Addition of {num1} and {num2} is {num1*num2}')

#Division result will always be float.
print(f'Division of {num1} and {num2} is {num1/num2}')


