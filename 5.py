# Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.

spisok = []
spisok1 = []
spisok2 = []
spisok3 = []
spisok4 = []

my_file = open("mnogochlen_1.txt", "w+")
my_file.write("2 * x**2 + 4 * x + 5 = 0")
my_file.close()

my_file_2 = open("mnogochlen_2.txt", "w+")
my_file_2.write("6 * x**2 + 14 * x + 34 = 0")
my_file_2.close()

my_file = open("mnogochlen_1.txt", "r")

line = my_file.readline().split()
while line:
    spisok.extend(line)
    line = my_file.readline().split()
print(spisok)

my_file.close()

for i in spisok:
    try:
        spisok2.append(int(i))
    except ValueError:
        spisok2.append(i)
print(spisok2)

my_file_2 = open("mnogochlen_2.txt", "r")

line_1 = my_file_2.readline().split()
while line_1:
    spisok1.extend(line_1)
    line_1 = my_file_2.readline().split()
print(spisok1)

my_file_2.close()

for i in spisok1:
    try:
        spisok3.append(int(i))
    except ValueError:
        spisok3.append(i)
print(spisok3)

for i in range(len(spisok2)):
    if type(spisok2[i]) == int and type(spisok3[i]) == int:
        spisok4.append(str(spisok2[i] + spisok3[i]))
    else:
        spisok4.append(spisok2[i])
print(spisok4)

my_file = open("mnogochlen_sum.txt", "w+")
my_file.write(' '.join(spisok4))
my_file.close()

