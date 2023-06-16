n = int(input("Введите количество чисел в массиве: "))
a = int(input("Введите искомое число: "))
count=0
for i in range(n):
    x= int(input("Введите число массива:")) 
    if x==a:
        count+=1
print(count)    