'''
1. In List we can store Homogeneous as well as Hetrogeneous Data.
2. In List we can store duplicate values.
3. List is an ordered collection of data. That is the order of insertion will be same in ouput as the order in which values  were inputted or added.
4. List is Mutable: once we declare the list we can modify it.
'''

li1 = [10,20,44.45,True,'Kodnest',20]
print(li1, type(li1))

#Syntax: append(value) 
# will add element ar the end of the list
li1.append(300)
print(li1)

#Syntax: insert(index,element):
# will add the element at  specified index
li1.insert(1,15)

#remove(ele): Removes the first occurence of the specified ele.
li1.remove(20)
print(li1)

# in and not in operator
print(2000 in li1)# False
print('Kodnest' in li1)# True

#pop(): without  argument will delete and return last element from list
removed_ele = li1.pop()
print(removed_ele) #300
print(li1)

#pop(index): with argument will delete the element at specified index, and return the removed element.
removed_ele =li1.pop(4)
print(removed_ele)
print(li1)

#del keyword:
# will not return anything , since its a keyword  not a function.
del li1[1]
print(li1)

del li1 # will delete the complete list object from the memory . Since its no argument is provided
print(li1) #Error: name 'li1' is not defined