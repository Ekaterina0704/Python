def degree(a,b):
    if b>0:
        return a*degree(a,b-1)   
    return 1

#a=int(input)
#b=int(input)
print(degree(2,5))