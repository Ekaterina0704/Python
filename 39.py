n= int(input("Введите количество элементов в 1 списке: "))
list1=[int(i)for i in input().split()][:n]
m= int(input("Введите количество жлементов во 2 списке "))
list2=[int(i) for i in input().split()][:m]
print(list1)
print(list2)
for i in list1:
    if i not in list2:
        print(i, end=" ")