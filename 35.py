 # проверить простое это число или нет

def num(array):
    for i in range(2,n//2+1):
        if array%i==0:
            return "NO"
        return "YES"
    
n=int(input())
print(num(n))
