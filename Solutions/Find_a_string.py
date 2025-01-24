def find(str,fstr): 
    lenF = len(fstr)
    lenS = len(str)
    count = 0
    
    for i in range(lenS-lenF+1):
        if(str[i:lenF+i] == fstr):
            count = count + 1

    return count


str = input()
fstr = input()
print("count: ",find(str,fstr))