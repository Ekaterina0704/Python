n = [int(i) for i in input("Введите числа: ").split()]
count= 0
for i in range(len(n)-1):
    if n[i+1]>n[i]:
        count+=1
print(count)         