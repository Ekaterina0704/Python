a=int(input("Введите 1й эл-т прогрессии: ")) 
d=int(input("Введите разность: "))
n=int(input("Введите к-во элементов: "))  
list1=[]         
for i in range(n):
    c=a+i*d
    list1.append(c)
print(list1)    