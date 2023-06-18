list1=[int(i)for i in input().split()]
result={}
for elem in list1:
    if elem in result.keys():
        result[elem]+=1
    else:
        result[elem]=1
print(sum([i//2 for i in result.values()]))         
