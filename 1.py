# Пользователь вводит число, Вам необходимо вывести число 
# Пи с той точностью знаков после запятой, 
# сколько указал пользователь(БЕЗ ИСПОЛЬЗОВАНИЯ МОДУЛЕЙ/БИБЛИОТЕК)

x = int(input("Сколько знаков после запятой: "))
p = 0
for k in range(x):
    y = (1 / (16 ** k)) * ((4 / (8 * k + 1)) - (2 / (8 * k + 4)) - 
                           (1 / (8 * k + 5)) - (1 / (8 * k + 6)))
    p += y
print(round(p, x))
