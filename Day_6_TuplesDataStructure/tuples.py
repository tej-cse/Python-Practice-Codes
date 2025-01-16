'''
1.In tuple we can store Homogeneous as well as Heterogeneous Data.
2.In tuples we can store Duplicates.
3.Tuples are orderd collection of Data.
4.Tuples are Immutable: once we declare the tuple we cannot modify it.
'''

tupl1 = (10,22.55,'Kodnest',True,10)
print(tupl1)

#tup1.remove(55) , will throw error
#del tup1[2] , will throw error

print(tupl1[2]) # will print 'Kodnest'

#deletes the complete tup1 object
del tupl1


t1 = (1,2,3)
t2 = (4,5,6)
t3 = t1 + t2
print(t3) # (1,2,3,4,5,6)

#Create a Singleton Tuple:
tup = (10,)
print(tup, type(tup)) # (10,) <class 'tuple'>

#if we want to declare a tuple with single element , that is a singleton tuple
# you should give a comma after the the element
# otherwise it will be considered as Integer , not as tuple




new_tup = (10,20,30,40)
#ele1 = new_tup[0]

#Unpacking of tuple
ele1,ele2,ele3,ele4 = new_tup
print('Value of ele1',ele1)

