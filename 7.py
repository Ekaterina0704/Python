i= (int(input("Введите год: ")))
if i%4==0 and i%100!=0 or i%400==0: 
    print("Это високосный год")
else: 
    print("Это невисокосный год")