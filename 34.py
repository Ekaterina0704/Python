text=input().lower().split()
result=set()
values="уеэёоаыяию"
for i in text:
    count=0
    for j in i:
        if j in values:
            count+=1
    result.add(count)    
if len(result)==1:
    print("парам пам-пам")
else:
    print("пам парам")    