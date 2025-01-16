'''
1. Dictionary is muttable.
2. It can store hetrogeneous as well as homogeneous objects
1. In dictionary we cannot store duplicate keys. But duplicate values are allowed.
'''

d1 = {'name':'Priya','age':27,'phone':23456,'age':29}
print(d1,type(d1)) #{'name': 'Priya', 'age': 29, 'phone': 23456} <class 'dict'>

#In dic we cannot store duplicate keys.
d1["name"] = "Pooja"
print(d1) #{'name': 'Pooja', 'age': 29, 'phone': 23456}

#In dict we can store duplicate values.
marks = {"sci":84,"Maths":85} #Allowed

for i in d1.keys():
    print(i,end="")

print()

for i in d1.values():
    print(i,end="")

print()

for i in d1.items():
    print(i) # output is a tuple , each tuple contains the key : value pair