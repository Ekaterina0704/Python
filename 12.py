"""
оценки
"""
x = (int(input("Введите cумму чисел: ")))
y = (int(input("Введите произведение чисел: ")))
for i in range(x):
    for j in range(y):
        if x==i+j & y==i*j:
            print(i,j)  
