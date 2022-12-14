# Напишите программу, которая принимает на вход координаты точки (X и Y), 
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, 
# в которой находится эта точка.

def is_float(value):  # Проверка введенного значения на вещественное число
    try:
        float(value)
        return True
    except ValueError:
        return False

X = input('Введите координаты точки X: ')
Y = input('Введите координаты точки Y: ')


while is_float(X) == False or is_float(Y) == False or float(X) == 0 or float(Y) == 0:   # Проверка условий для введенных значений
    if is_float(X) == False or is_float(Y) == False:
        print('X и Y должны быть числами')
        X = input('Введите координаты точки X: ')
        Y = input('Введите координаты точки Y: ')
        continue
    if float(X) == 0 or float(Y) == 0:
        print('X и Y не могут быть равны 0')
        X = input('Введите координаты точки X: ')
        Y = input('Введите координаты точки Y: ')

X = float(X)
Y = float(Y)

if X > 0 and Y > 0:     # Выбор для введенных значений соответствующего ответа
    print('Точка с координатами X = %s и Y = %s находится в 1-й четверти плоскости'%(X, Y))
elif X < 0 and Y > 0:
    print('Точка с координатами X = %s и Y = %s находится в 2-й четверти плоскости'%(X, Y))
elif X < 0 and Y < 0:
    print('Точка с координатами X = %s и Y = %s находится в 3-й четверти плоскости'%(X, Y))
else:
    print('Точка с координатами X = %s и Y = %s находится в 4-й четверти плоскости'%(X, Y))

