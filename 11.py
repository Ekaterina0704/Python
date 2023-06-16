"""
число фибоначчи
"""
n= (int(input("Введите число: ")))
x0=0
x1=1
x=0
i=2
while x<n:
    x= x0 +x1
    x0=x1
    x1=x
    i+=1
    if x>n:
        i=0
if i==0:
    print(-1)
else:
    print(i)