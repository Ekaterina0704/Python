"""
факториал числа
"""
n= (int(input("Введите число: ")))
a=1
result=1
while a<=n:
    result=result*a
    a+=1
print("Факториал числа", n, "=", result)
