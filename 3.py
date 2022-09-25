# Задайте последовательность чисел. Напишите программу, которая 
# выведет список неповторяющихся элементов исходной последовательности.

from random import randint


spisok = []
for i in range(10):
    spisok.append(randint(0, 10))
print(spisok)


def itog_spisok(spisok):
    spisok2 = []
    for x in spisok:
        if x not in spisok2:
            spisok2.append(x)
    return spisok2

print(itog_spisok(spisok))