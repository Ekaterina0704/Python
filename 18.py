n = int(input("Введите количество чисел в массиве: "))
a = int(input("Введите число для сравнения: "))
result=0
change=0
min=1000000
for i in range(n):
    x= int(input("Введите число массива:")) 
    change= abs(x-a)
    if change<min:
        min=change
        result = x 
print(result)    