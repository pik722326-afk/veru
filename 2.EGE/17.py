# 📚 Полезные ссылки на статьи и разборы задач:
# 📘 Полная версия шпаргалки доступна в нашем тг канале: https://t.me/informatika_kege_itpy/362?comment=6532
# 📘 Разборы 17 номеров по информатике: https://t.me/informatika_kege_itpy/360?comment=1612

# region Место для вашего конспекта ⬇️
'''
Запустите бота: https://t.me/ilandroxxy_bot и нажмите кнопку: "📚 Получить конспект"
'''
# endregion Место для вашего конспекта ⬆️
# Как можно открывать файлы
'''
file = open('files/17.txt', mode='r')
print(file)  # <_io.TextIOWrapper name='files/17.txt' mode='r' encoding='UTF-8'>

M = []
for s in file:
    s = int(s)
    M.append(s)
print(M)

file.close()
'''

# Как надо открывать файлы
'''
with open('files/17.txt', mode='r') as file:
    M = []
    for s in file:
        s = int(s)
        M.append(s)
    print(M)
'''

# Как будем делать мы
'''
M = [int(s) for s in open('files/17.txt')]
print(M)
'''

# Три прототипа 17 номера
'''
# i  0  1  2  3  4
M = [1, 2, 3, 4, 5]

# 1. Под парой подразумеваются два идущих подряд элемента последовательности.
# 12 23 34 45
for i in range(len(M)-1):
    x, y = M[i], M[i+1]


# 2. Под тройкой подразумеваются три идущих подряд элемента последовательности.
# 123 234 345
for i in range(len(M)-2):
    x, y, z = M[i], M[i+1], M[i+2]


# 3. Под парой подразумеваются два различных элемента последовательности.
# 12 13 14 15
# 23 24 25
# 34 35
# 45
for i in range(len(M)):
    for j in range(i+1, len(M)):
        x, y = M[i], M[j]
'''

# № 25356 (Уровень: Базовый)
# Определите количество троек элементов последовательности,
# в которых ни один из трёх элементов не является четырёхзначным числом,
# а сумма элементов тройки больше максимального элемента последовательности, оканчивающегося на 30
'''
M = [int(s) for s in open('files/17.txt')]
A = [x for x in M if len(str(abs(x))) == 4]
B = [x for x in M if abs(x) % 100 == 30]
R = []
for i in range(len(M)-2):
    x, y, z = M[i], M[i+1], M[i+2]
    if (x in A) + (y in A) + (z in A) == 0:
        if (x + y + z) > max(B):
            R.append(x + y + z)
print(len(R), max(R))
'''

# № 24892 (Уровень: Базовый)
'''
M = [int(s) for s in open('files/17.txt')]
A = [x for x in M if x < 0 and len(str(abs(x))) == 4 and abs(x) % 9 == 0]
R = []
for i in range(len(M)-1):
    x, y = M[i], M[i+1]
    if (x < 0) + (y < 0) == 1:
        if (x + y) > max(A):
            R.append(x**2 + y**2)
print(len(R), min(R))
'''

# № 23376 Резервный день 19.06.25 (Уровень: Базовый)
'''
M = [int(s) for s in open('files/17.txt')]
A = [x for x in M if len(str(abs(x))) == 5]
B = [x for x in A if abs(x) % 100 == 37]
R = []
for i in range(len(M)-1):
    x, y = M[i], M[i+1]
    if (x in A) + (y in A) == 1:
        if (x + y) ** 2 > max(B) ** 2:
            R.append(x + y)
print(len(R), max(R))
'''

# № 21712 ЕГКР 19.04.25 (Уровень: Базовый)
'''
M = [int(s) for s in open('files/17.txt')]
A = [x for x in M if len(str(abs(x))) == 4 and abs(x) % 10 == 6]
B = [x for x in A if x > 0]
R = []
for i in range(len(M)-2):
    x, y, z = M[i], M[i+1], M[i+2]
    if (x in A) + (y in A) + (z in A) == 1:
        if (x + y + z) <= min(B):
            R.append(x + y + z)
print(len(R), max(R))
'''

# № 7718 (Уровень: Средний)

"""M = [int(s) for s in open('files/17.txt')]
R = []
for i in range(len(M)):
    for j in range(i + 1, len(M)):
        x, y = M[i], M[j]
        if ((x + y) % 18 == 0) + ((x * y) % 18 == 0) == 1:
            R.append(x + y)
print(len(R), max(R))"""

#Способ чтения файла
'''
file = open('files/17.txt', mode='r')
print(file)  # <_io.TextIOWrapper name='files/17.txt' mode='r' encoding='UTF-8'>

M = []
for s in file:
    s = int(s)
    M.append(s)
print(M)

file.close()
'''


# Правильные условия открытия файла
'''
with open('files/17.txt', mode='r') as file:
    M = []
    for s in file:
        s = int(s)
        M.append(s)
    print(M)
'''

# Как открывать файл для 17 номера:
'''
M = [int(s) for s in open('files/17.txt')]
print(M)
'''


# Рассмотрим три прототипа 17 номера
'''
# i  0  1  2  3  4
M = [1, 2, 3, 4, 5]

# 1. Под парой подразумевается два идущих подряд элемента последовательности.
# 12 23 34 45
for i in range(len(M)-1):
    x, y = M[i], M[i+1]

# 2. Под тройкой подразумевается три идущих подряд элемента последовательности.
# 123 234 345
for i in range(len(M)-2):
    x, y, z = M[i], M[i+1], M[i+2]
'''


# № 25356 (Уровень: Базовый)
'''
M = [int(s) for s in open('files/17.txt')]
A = [x for x in M if len(str(abs(x))) == 4]
B = [x for x in M if abs(x) % 100 == 30]
R = []
for i in range(len(M)-2):
    x, y, z = M[i], M[i+1], M[i+2]
    if (x in A) + (y in A) + (z in A) == 0:
        if (x + y + z) > max(B):
            R.append(x + y + z)
print(len(R), max(R))
'''


# № 23276 Основная волна 11.06.25 (Уровень: Базовый)
'''
M = [int(s) for s in open('files/17.txt')]
A = [x for x in M if len(str(abs(x))) == 4]
B = [x for x in M if abs(x) % 100 == 25]
R = []
for i in range(len(M)-2):
    x, y, z = M[i], M[i+1], M[i+2]
    if (x in A) + (y in A) + (z in A) <= 2:
        if (x + y + z) <= max(B):
            R.append(x + y + z)
print(len(R), max(R))
'''


# № 23201 Основная волна 10.06.25 (Уровень: Базовый)
'''
M = [int(s) for s in open('files/17.txt')]
A = [x for x in M if len(str(abs(x))) == 3]
B = [x for x in A if abs(x) % 10 == 7]
R = []
for i in range(len(M)-1):
    x, y = M[i], M[i+1]
    if (x in A) + (y in A) == 1:
        if (x + y) % min(B) == 0:
            R.append(x + y)
print(len(R), min(R))
'''


# № 23563 Пересдача 03.07.25 (Уровень: Базовый)
# Определите количество пар последовательности, в которых элементы не равны,
# а абсолютное значение их разности делится на минимальный положительный элемент
# последовательности, кратный 35. Гарантируется, что такой элемент последовательности есть.
# В ответе запишите количество найденных пар, затем максимальную из сумм элементов таких пар.
'''
M = [int(s) for s in open ("files/17.txt")]
B = [x for x in M if abs(x) % 35 == 0 and x > 0]
R = []
for i in range(len (M)-1):
    x, y = M[i], M[i+1]
    if x != y:
        if abs(x - y) % min(B) ==0:
            R.append(x+y)
print (len(R),max(R))
'''



# № 23757 Демоверсия 2026 (Уровень: Базовый)
# Определите количество пар последовательности, в которых только один из элементов
# является двузначным числом, а сумма элементов пары кратна минимальному двузначному
# элементу последовательности. В ответе запишите количество найденных пар, затем максимальную
# из сумм элементов таких пар. В данной задаче под парой подразумевается два идущих подряд
# элемента последовательности.

"""M = [int(x) for x in open('files/17.txt')]
A = [x for x in M if len(str(abs(x))) == 2]
R = []
for i in range(len(M)-1):
    x, y = M[i], M[i+1]
    if (x in A) + (y in A) == 1:
        if (x + y) % min(A) == 0:
            R.append(x + y)
print(len(R), max(R))"""



"""M = [int(x) for x in open('files/17_13088.txt')]
A = [x for x in M if len(str(abs(x))) == 4]
B = [x for x in M if x % 100 == 17]
C = [x for x in M if x % 5 == 0]
R = []
for i in range(len(M)-2):
    x, y, z = M[i], M[i+1], M[i+2]
    if (x in A) + (y in A) + (z in A) == 2:
        if (x in C) + (y in C) + (z in C) >=  1:
            if (x + y + z) > max(B):
                R.append(x + y + z)
print (len(R), max(R))"""


"""M = [int(x) for x in open('files/17_11949.txt')]
A = [x for x in M if len(str(abs(x))) == 2]
B = [x for x in M if x % 100 == 68]
R = []
for i in range(len(M)-3):
    x, y, z, w = M[i], M[i+1], M[i+2], M[i+3]
    if (x in A) + (y in A) + (z in A) + (w in A) == 1 or (x in A) + (y in A) + (z in A) + (w in A) == 4:
        if (x + y + z + w) >= max(B):
            R.append(x + y + z + w)
print (len(R), max(R))"""


"""M = [int(x) for x in open('files/17_11838.txt')]
A = [x for x in M if len(str(abs(x))) == 5]
B = [x for x in M if x % 100 == 50]
R = []
for i in range(len(M)-2):
    x, y, z = M[i], M[i+1], M[i+2]
    if (x in A) + (y in A) + (z in A) == 3 and x != y and x != z and y != z:
            if (x + y + z) <= max(B):
                R.append(x + y + z)
print (len(R), max(R))"""

# Домашка 17 номер: https://stepik.org/lesson/1038775/step/1?unit=1062778

# Практика 17 номер: https://stepik.org/lesson/1228675/step/1?unit=1242208
