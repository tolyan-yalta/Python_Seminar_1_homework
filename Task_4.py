# Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y).

def is_int(value):  # Проверка введенного значения на целе число
    try:
        int(value)
        return True
    except ValueError:
        return False

def is_interval(value): # Проверка диапазона чисел
    if is_int(value):
        if 0 < int(value) < 5:
            return True
        else:
            return False
    else:
        return False

number = input('Введите номер четверти на плоскости: ')

while is_int(number) == False or is_interval(number) == False:  # Проверка условий для введенного значения
    if is_int(number) == False:
        print('Введенное значение не целое число')
        number = input('Введите номер четверти на плоскости: ')
        continue
    elif 0 < int(number) < 5:
        break
    else:
        print('Номер четверти на плоскости может быть от 1 до 4')
        number = input('Введите номер четверти на плоскости: ')

number = int(number)
if number == 1: # Выбор для введенного значения соответствующего ответа
    print('Координпты точек по оси X от 0 до бесконечности')
    print('Координпты точек по оси Y от 0 до бесконечности')
elif number == 2:
    print('Координпты точек по оси X от 0 до минус бесконечности')
    print('Координпты точек по оси Y от 0 до бесконечности')
elif number == 3:
    print('Координпты точек по оси X от 0 до минус бесконечности')
    print('Координпты точек по оси Y от 0 до минус бесконечности')
else:
    print('Координпты точек по оси X от 0 до бесконечности')
    print('Координпты точек по оси Y от 0 до минус бесконечности')
