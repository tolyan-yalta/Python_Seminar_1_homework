# Напишите программу, которая принимает на вход цифру, обозначающую день недели, 
# и проверяет, является ли этот день выходным.

def is_int(value):  # Проверка введенного значения на целое число
    try:
        int(value)
        return True
    except ValueError:
        return False

def is_interval(value): # Проверка диапазона чисел
    if is_int(value):
        if 0 < int(value) < 8:
            return True
        else:
            return False
    else:
        return False

number = input('Введите цифру, обозначающую день недели: ')

while is_int(number) == False or is_interval(number) == False:  # Проверка условий для введенного значения
    if is_int(number) == False:
        print('Введенное значение не целое число')
        number = input('Введите день недели: ')
        continue
    elif 0 < int(number) < 8:
        break
    else:
        print('День недели может быть от 1 до 7')
        number = input('Введите день недели: ')

number = int(number)

if 1 <= number <= 5:
    print('Нет, это не выходной')
else:
    print('Да, это выходной')


