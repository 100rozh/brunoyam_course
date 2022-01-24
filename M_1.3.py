a = float(input('Введите число: '))
b = float(input('Введите число: '))
maximum = (a > b) * a + (b >= a) * b
print('Максимальное число: ', maximum)