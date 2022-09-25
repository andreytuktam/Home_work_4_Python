# Задана натуральная степень k. Сформировать случайным образом список 
# коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

# Пример:

# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import randint as rd


k = int(input('k = '))

spisok = list()
for i in range(k, 0, -1):
    x = rd(-100, 100)
    if x > 0 and i != k:
        spisok.append(f'+{x}*x^{i}')
    else:
        spisok.append(f'{x}*x^{i}')

    x = rd(-100, 100)
if x > 0 and i != k:
    spisok.append(f'+{x}')
else:
    spisok.append(f'{x}')
spisok.append(' = 0')
print(''.join(spisok))

my_file = open("spisok_k.txt", "w+")
my_file.write(' '.join(spisok))
my_file.close()