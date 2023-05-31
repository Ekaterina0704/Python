"""
Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.
385916 -> yes
123456 -> no

"""
i= (int(input("Введите номер билета: ")))
if i//100000+i//10000%10+i//1000%10==i//100%10+i//10%10+i%10: 
    print("Счастливый билет!")
else: 
    print("Несчастливый билет(")