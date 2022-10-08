# Напишите программу, которая принимает на вход координаты двух точек 
# и находит расстояние между ними в 2D пространстве.

def is_float(value):  # Проверка введенного значения на вещественное число
    try:
        float(value)
        return True
    except ValueError:
        return False

X1, Y1 = map(str, input('Введите координаты первой точки X1 и Y1: ').split())

while is_float(X1) == False or is_float(Y1) == False:   # Проверка условий для введенных значений
    if is_float(X1) == False or is_float(Y1) == False:
        print('X1 и Y1 должны быть числами')
        X1, Y1 = map(str, input('Введите координаты первой точки X1 и Y1: ').split())

X1 = float(X1)
Y1 = float(Y1)

X2, Y2 = map(str, input('Введите координаты первой точки X2 и Y2: ').split())

while is_float(X2) == False or is_float(Y2) == False:   # Проверка условий для введенных значений
    if is_float(X2) == False or is_float(Y2) == False:
        print('X2 и Y2 должны быть числами')
        X2, Y2 = map(str, input('Введите координаты первой точки X2 и Y2: ').split())

X2 = float(X2)
Y2 = float(Y2)

distance = round(((X2 - X1) ** 2 + (Y2 - Y1) ** 2) ** 0.5, 2)

print('Расстояние между точками равно ', distance)


