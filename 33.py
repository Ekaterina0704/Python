 #заменить максимальные значения списка на минимальные
n= int(input("Введите количество элементов в списке"))
a=list()
max=0
min=1000
for i in range(n):
    x=int(input("Введите элемент"))
    a.append(x)
    if x>max:
        max=x
    if x<min:
        min=x
print(max, min) 
print(a)

b=list()
for i in a:
    if i==max:
        b.append(min)
    else:
        b.append(i) 
print(b)       
