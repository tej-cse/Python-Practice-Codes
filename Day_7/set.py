'''
1. In set we can store Homogeneous as well as Heterogeneous data.
2. Set is an Unordered Collection of data.
3. Set does not support indexing of data.
4. In Set we cannot store duplicates.
5. Sets are Muttable.
'''

s1 = {10,True,'Kodnest',10,20,55.44}

print(s1,type(s1)) # {True, 20, 55.44, 'Kodnest', 10} <class 'set'>
# print(s1[0]) -> will throw error

#add(): used to add an element in the set
s1.add(500)
print(s1) #{True, 20, 500, 'Kodnest', 55.44, 10}

#.remove() : will remove the specified element
s1.remove(55.44)
print(s1) #{True, 20, 500, 'Kodnest', 10}

# .pop(): without index will delete and return one random element from the set.
s1.pop() # "True" is randomly 
print(s1) #{20, 500, 10, 'Kodnest'}

#del s1[2] -> error

#will delete the complete the set object
del s1