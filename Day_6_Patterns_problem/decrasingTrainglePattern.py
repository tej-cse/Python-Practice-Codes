rows = int(input("Enter value for row: "))

for i in range(rows):
    for j in range(i,rows): # or "for j in range(rows-i)"
        print("*",end=" ")
    print()