"""
сдвинуть элементы списка на какое то количество элементов вправо
"""
data = [int(i) for i in input("Введите числа списка: ").split()]
step = (int(input("Введите число для сдвига: ")))
step=step%len(data)
data=[data[i-step] for i in range(len(data))]
print(data)

