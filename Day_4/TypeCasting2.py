# print(int('12.22')) 
# gives error

print(float('22.22'))
# can be typecasted

print(int(12.26))
#12 will be output

#Taking float value from user and converting it into int 
value = int(float(input('Enter price Float value: ')))
print(value, type(value))