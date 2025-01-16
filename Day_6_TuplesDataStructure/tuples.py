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
t2 = ()
t3 = ()