import math 
a= (int(input("Введите количество  учеников в 1 классе")))
b= (int(input("Введите количество учеников во 2 классе ")))
c= (int(input("Введите количество учеников в 3 классе ")))
print(math.ceil(a/2)+math.ceil(b/2)+math.ceil(c/2))
# result= a//2+a%2+b//2+b%2+c//2+c%2