def swapCase(str):
    newStr = ''
    for i in str:
        if (i.islower()):
            newStr = newStr + i.upper()
        elif (i.isupper()):
            newStr = newStr + i.lower()

    return newStr

print(swapCase(input()))