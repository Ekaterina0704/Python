"""
Задайте список из нескольких чисел. Напишите программу,
которая найдёт сумму элементов списка,
стоящих на нечётной позиции.
*Пример:*

- [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
"""
A = list(map(int, input().split()))
n = 1
sum=0
while n <len(A):
    sum=sum+A[n]
    n=n+2
print(sum)