# мин и макс вес арбуза
n = (int(input("Введите количество арбузов: ")))
count=0
max_waight=0
min_waight=1001
for i in range(n):
    x=int(input("Введите вес арбуза: "))
    if x>max_waight:
        max_waight=x
    if x<min_waight:
        min_waight=x            
print(min_waight, max_waight)         