"""
дан список чисел определить сколько в нем встречается различных чисел
"""
n = [int(i) for i in input("Введите числа: ").split()]
n= set(n)
print(len(n))


    