from random import randint as rd

min=int(input("Введите минимум диапазона: ")) 
max=int(input("Введите максимум диапазона: "))
list1=[rd(1,10) for i in range(10)]
print(list1)
for i in list1:
    if max>i>min:
        print(i, end=" ")

