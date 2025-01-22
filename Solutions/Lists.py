li = []
n = int(input())
for i in range(n):
    command,*values = input().split()
     # split() method -> split the input taking delimiter as space
     # and returns a List of elements

    values = list(map(int,values))
    # each elements of values list will be converted into "integer"
    # map will return a iterable object
    # so we convert it , into a "list" using list()
    
    if (command == 'insert'):
        li.insert(values[0], values[1])
    elif (command == 'remove'):
        li.remove(values[0])
    elif (command == 'append'):
        li.append(values[0])
    elif (command == 'sort'):
        li.sort()
    elif (command == 'pop'):
        li.pop()
    elif (command == 'reverse'):
        li.reverse()
    elif (command == 'print'):
        print(li)