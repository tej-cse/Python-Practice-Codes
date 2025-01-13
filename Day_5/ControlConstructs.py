'''
    1.Conditional: if-else, if-elif
    2.Looping: for, while
    3.Jumping: break, continue, pass
'''

def checkAge(age):
    if(age > 18):
        print('Age is greater than 18')
    else:
        print('Age is not greater than 18')

#checkAge(18)
#checkAge(19)

# WAP to display 'Child' if age is in below 18
# display 'Adult' if age is above 18
# display 'senior citizen' if age is above 65.

def checkType(age):
    if(age > 65):
        print('Senior Citizen')
    elif(age > 18): # else if
        print('Adult')
    else:
        print('Child')

age = int(input("Enter the age: "))
checkType(age)