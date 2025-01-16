'''
    for control_variable in iterable_object:
'''
for i in 'Kodnest':
    print(i, end="-")

print()

for j in [10,20,30]:
    print(j+5)

for num in range(1,11): #Range parameter: start,end
    print(num)          #Range we will take value from start to end-1
                        #By default it will increment value by 1
                        
for num in range(5):    #If only one  parameter is specified, the range function  will treat it as end_value
     print(num)         # that is, the start default value will be taken as 0             

for num in range(11,21,2): #Range parameter: start,end,increment _value
    print(num,end=" ")

print()

for num in range(1,11):
    if(num % 2 == 0):
        print(num,end=" ")

print()

i = 0
while(i < 11):
    print(i,end=" ")
    i=i+1

print()
# WAP to print numbers from 1-10 , but if number is 6 then skip printing

for i in range(1,11):
    if(i == 6):
        continue
    print(i,end=" ")

print()
# WAP to print numbers from 1-10 , but if number is 5 then stop printing

for i in range(1,11):
    if(i == 5):
        break
    print(i,end=" ")

# pass

# pass is used to skip implementation
# we cant leave method or class or control construct empty
# or we place pass there , we dont want to give their implementation

def func():
    pass

class NewClass:
    pass