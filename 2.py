# Задайте натуральное число N. Напишите программу, которая составит 
# список простых множителей числа N.


n = int(input("n = "))
spisok = []
d = 2
while d * d <= n:
    if n % d == 0:
        spisok.append(d)
        n = n // d
    else:
        d = d + 1
spisok.append(n) 
print(spisok) 