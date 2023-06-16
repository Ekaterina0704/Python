 # последовательность в обратном порядке
def reverse(n):
    if n==0:
        return " "
    k=input()
    return reverse(n-1)+ f'{k}' 

n=int(input())
print(reverse(n))
