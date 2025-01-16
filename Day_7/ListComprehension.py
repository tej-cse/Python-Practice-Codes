li1 = [1,2,3,4,5]

# print(li1)

# sq_li = []

# for i in li1:
#     sq_li.append(i**2)

# print(sq_li)

#List Comprehension
#[expression_to_return for i in iterable_object  condition _to_return_the_expression]

#When we have only if part then write it after for loop.
duplicate_li1 = [i for i in li1]
print(duplicate_li1)
print("----------------------")
even = [i for i in li1 if i%2 == 0]
print(even)
print("----------------------")
sq_list = [i**2 for i in li1]
print(sq_list)
print("----------------------")
new_li1 = [ele+2 for ele in li1]
print(new_li1)
print("----------------------")

# when we have if-else both write it before for loop

even_odd = ['even' if i%2==0 else 'Odd' for i in li1]
print(even_odd)

print("----------------------")


#Mutiple for loops inside list comprehension
li = [[10,20],[30,40],[50,60]]
new_li = [ele for sublist in li for ele in sublist]
print(new_li)