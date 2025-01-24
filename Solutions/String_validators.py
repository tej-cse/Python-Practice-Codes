# isalnum(): 
# returns true , if the string contains alphabets or numbers only. 
# returns false, if string contains any other character , other than alphabets and numbers
print('Kodnest1234*'.isalnum()) #False
print('Kodnest'.isalnum()) #True

# isalpha():
# returns true, if the string contains alphabets only
print('code'.isalpha()) #True
print('Kodnest123'.isalpha()) #False


# isdigits():
# returns true, if the string contains digits only
print('12'.isdigit()) #True

print('apple'.islower())
print('apple'.isupper())


# any(): accepts a iterable object as argument
# return true, if any one element in the iterable object is true
# for empty iterable object it returns false
print(any([True,False,False]))
print(any(tuple([])))

# -----------------------------------------------------------------------------------------------

s = input()
print(any([i.isalnum() for i in s]))

print(any([i.isalpha() for i in s]))

print(any([i.isdigit() for i in s]))

print(any([i.islower() for i in s]))

print(any([i.isupper() for i in s]))