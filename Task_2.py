# Напишите программу для проверки истинности утверждения
#  ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z 
# для всех значений предикат.

print('X', 'Y', 'Z', '¬(X ⋁ Y ⋁ Z)', '¬X ⋀ ¬Y ⋀ ¬Z', sep='\t')
x = y = z = 0
list_left = []
list_right = []
while x < 2:
    while y < 2:
        while z < 2:
            print(x, y, z, sep='\t', end='\t    ')

            temp1 = not (bool(x) or bool(y) or bool(z))
            print(temp1, sep='\t', end='\t    ')
            list_left.append(temp1)
           
            temp2 = not bool(x) and not bool(y) and not bool(z)
            print(temp2, sep='\t')
            list_right.append(temp2)

            z += 1
        z = 0
        y += 1
    y = 0
    x += 1

if list_left == list_right:
    print('Выражение ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z проверено и верно')
else:
    print('Выражение ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z проверено и не верно')
