def mutate(string, position, character):
    li = list(string)
    # eg: s ='Kod'
    #     li = list(s) -> li = ['K','o','d]
    #     print(li)-> ['K','o','d]

    li[position] = character
    return ''.join(li)

string = input("enter a string:")
position,character = input().split()
#split the input string as a list of elements()
#then unpacking the list , so that 
# position = 0th index list value
# character = 1st index list value 
print(mutate(string, int(position), character))