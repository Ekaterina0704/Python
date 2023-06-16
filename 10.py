"""
монетки
"""
n = (int(input("Введите количество монет: ")))
count1=0
count0=0
for i in range(n):
    x=int(input("Введите орел или решка: "))
    if x==1:
        count1+=1
    else:
        count0+=1
if count0>count1:
    print(count1)  
else:
    print(count0)        