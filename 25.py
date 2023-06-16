word = input("Введите текст: ").split()  
result={}     
for i in word:
    if i in result:
        print(f"{i}_{result[i]}", end= " ")
        result[i]+=1
    else:
        print (i,end=" ")    
        result[i]=1