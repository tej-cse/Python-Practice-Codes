'''
Strings are immutable : 
1.once we declare the string we cannot modify it, if we try to modify the string it will create new string.
2.If new String does not have any reference variable then it will be removed by garbage collector.

3.Python Internally uses String Interning

4.String Interning is the Process of Checking string Intern Pool
before creating any new object.

whenever we want to create new object, Python first will check string intern pool, whether that object already exist or not.

when the object already exist in the string intern records then address of existing object will be reused.
'''

s1 = 'Kodnest'
#Creates a new String object
#since no object refers to the returned string object ,  it will be removed by garbage collector
s1.upper()
#"Kodnest" will be printed
print(s1)

s1 = s1.upper()
# Now "KODNEST" will be printed
print(s1)



# like javaScript , python also have anything as charactere data type
# single character are also treated as string only


s3 = 'K'
#id() method is used to get the memory address
print(s3, id(s3))



s4 = 'Hello'
s5 = 'World'
print(s4, id(s4))
print(s5, id(s5))


#Retrieves a character from  string

#In python strings element can accessed through index unlike java
print(s4[0])
# -1 , means first element from back of string
print(s5[-1])


print('\ns1 ID of H: ' , id(s4[0]))
print('s5 ID of H: ' , id(s5[0]))

print('\ns4 ID of o: ', id(s4[-1]))
print('s5 ID of o: ', id(s5[1]))

print('\ns4 ID of o: ', id(s4[2]))
print('s4 ID of o: ', id(s4[3]))
print('s4 ID of o: ', id(s5[3]))
