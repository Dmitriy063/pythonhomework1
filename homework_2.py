# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
x = input('Введите 0 или 1: ')
y = input('Введите 0 или 1: ')
z = input('Введите 0 или 1: ')
if (not (x or y or z) == (not (x) and not (y) and not (z))):
    print("True")
else:
    print("False")
