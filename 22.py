n = int(input("Введите количество чисел в 1м массиве: "))
m = int(input("Введите количество чисел в 2м массиве: ")) 
a=list()
for i in range(n):
    x= int(input("Введите значения 1го массива:")) 
    a.append(x)
for i in range(m):
    x= int(input("Введите значения 2го массива:")) 
    a.append(x)
a=set(a)
a=list(a)    
print(sorted(a))    