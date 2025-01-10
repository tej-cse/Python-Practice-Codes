#if string is holding integer than it can be converted into int.
a = '30'
print(a,type(a))
b = int(a)
print(b,type(b))

# If varible is holding a String , then str to integer is not allowed
x = 'Kod'
print(x,type(x))

# y = int(x)
# print(y, type(y))


#Typecasting to float from str is only possible  if given input is float
#p = float(input('Enter float type data: ')) #12.22
#print(p, type(p))

#bool()
# any non zero value is treated as TRUE
# zero or empty string is treated as FALSE

q = 12
print(q, type(q))
q = bool(q)
print(q,type(q))
#true

q = ''
print(q,type(q))
q = bool(q)
print(q,type(q))
#false

q = 0
print(q,type(q))
q = bool(q)
print(q,type(q))
#false

'''
1. while converting int to bool for all non zero values we will get True
2. while converting int to bool for 0 and empty string we will get false
'''

print()