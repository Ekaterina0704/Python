n= int(input("Введите количество элементов в списке: "))
list1=[int(i)for i in input().split()][:n]
print(sum([int(list1[i-1]<list1[i]>list1[i+1]) for i in range(1,n-1)]))
