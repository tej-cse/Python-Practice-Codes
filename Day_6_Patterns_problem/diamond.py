row = 5

for i in range(row):
    for j in range(row-i):
        print("-",end="")
    
    for j in range(i):
        print("*",end="")
    
    for j in range(i+1):
        print("*",end="")

    print()

for i in range(1,row):
    for j in range(i+1):
        print("-",end="")
    
    for j in range(i,row-1):
        print("*",end="")
    
    for j in range(i,row):
        print("*",end="")

    print()
