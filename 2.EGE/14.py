# 📚 Полезные ссылки на статьи и разборы задач:
# 📘 Полная версия шпаргалки доступна в нашем тг канале: https://t.me/informatika_kege_itpy/362?comment=6532
# 📘 Разборы 14 номеров по информатике: https://t.me/informatika_kege_itpy/360?comment=1535

# region Место для вашего конспекта ⬇️

#Урок
"""
#https://education.yandex.ru/ege/task/fbfb743a-c36a-4cbc-9d9e-dcb76c353dda
#Ответ 21

M = []
for n in range(1, 10000):
    s = f'{n:b}'
    if n % 2 != 0:
        s = '1' + s[:-2] + '10'
    else:
        s = '10' + s[2:] + '1'
    r = int(s, 2)
    if n >= 33:
        M.append(r)
print(min(M))
'''


# https://education.yandex.ru/ege/task/71189626-0f31-4380-b790-94a173acd59a
'''
def convert(n, b):
    r = ''
    while n > 0:
        r += str(n % b)
        n //= b
    return r[::-1]

M = []
for n in range(1, 10000):
    s = convert(n, 7)
    z = ''
    for x in s:
        if x in '13579':
            z += str(int(x) + 1)
        else:
            z += x
    summa = sum([int(x) for x in z])
    # summa = sum(map(int, z))
    z = convert(summa, 7) + z
    if z[0] in '13579':
        z = z[0] + z
    r = int(z, 7)
    if r > 2000:
        M.append(r)
print(min(M))
'''


# https://education.yandex.ru/ege/task/11a28b89-356d-4baa-8ab4-3684fa4c1752
'''
def convert(n, b):
    r = ''
    while n > 0:
        r += str(n % b)
        n //= b
    return r[::-1]

M = []
for n in range(1, 10000):
    s = convert(n, 3)
    if n % 3 == 0:
        z = ''
        for x in s:
            z += x * 2
    else:
        s = s.replace('0', '*')
        s = s.replace('1', '+')
        s = s.replace('2', '0')
        s = s.replace('*', '1')
        s = s.replace('+', '2')
        z = ''
        for x in s:
            z += x * 2
    r = int(z, 3)
    print(r)
    if r > 120:
        M.append(n)
print(min(M))
'''


# № 23752 Демоверсия 2026 (Уровень: Базовый)
'''
alp = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
def convert(n, b):
    r = ''
    while n > 0:
        r += alp[n % b]
        n //= b
    return r[::-1]

n = 2*2187**2020 + 729**2021 - 2*243**2022 + 81**2023 - 2*27**2024 - 6561
s = convert(n, 27)
print(s.count('0'))  # Количество значащих нулей
print(len(s) - s.count('0'))  # Количество ненулевых цифр
print(len([x for x in s if x > '9']))  # количество цифр с числовым значением, превышающим 9.
'''


# № 17869 Демоверсия 2025 (Уровень: Базовый)
'''
alp = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
def convert(n, b):
    r = ''
    while n > 0:
        r += alp[n % b]
        n //= b
    return r[::-1]

n = 3*3125**8 + 2*625**7 -4*625**6 +3*125**5 - 2*25**4 - 2025
s = convert(n, 25)
print(s.count('0'))
'''


# № 17870 Демоверсия 2025 (Уровень: Базовый)
'''
alp = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
def convert(n, b):
    r = ''
    while n > 0:
        r += alp[n % b]
        n //= b
    return r[::-1]

for x in range(1, 2030):
    n = 7**170 + 7**100 - x
    s = convert(n, 7)
    if s.count('0') == 71:
        print(x)
'''

# № 23753 Демоверсия 2026 (Уровень: Базовый)
'''
M = []
alp = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
for x in alp[:29]:
    A = int(f'923{x}874', 29)
    B = int(f'524{x}6152', 29)
    if (A +  B) % 28 == 0:
        M.append((A +  B) // 28)
print(max(M))
'''


# № 6575 (Уровень: Базовый)

#Значение выражения 766**66 + 15**13 - 22 записали в системе счисления с основанием 13.
#Сколько раз в этой записи встречается цифра С?
alp = sorted("0123456789QWERTYUIOPASDFGHJKLZXCVBNM")
def converted (n, b):
    r = ''
    while n > 0:
        r = alp [n % b] + r
        n //= b
    return r
f = 766**66 + 15**13 - 22
s = converted(f, 13)
s = s.count("C")
print(s)
"""

#Решение

# № 17555 Основная волна 08.06.24 (Уровень: Базовый)
"""
k = []
alp = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
def convert(n, b):
    r = ''
    while n > 0:
        r += alp[n % b]
        n //= b
    return r[::-1]
for x in range(1, 2030):
    n = 7**91 + 7**160 - x
    s = convert(n, 7)
    if s.count('0') == 70:
        k.append(x)
print (max(k))
"""

# № 227 (Уровень: Базовый)
"""
alp = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
def convert(n, b):
    r = ''
    while n > 0:
        r += alp[n % b]
        n //= b
    return r[::-1]
f = 4**2015 + 2**2015 - 15
s = convert(f, 2)
s = s.count("1")
print (s)"""


#Домашка от жени
"1"
# № 17555 Основная волна 08.06.24 (Уровень: Базовый)
"""
k = []
alp = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
def convert(n, b):
    r = ''
    while n > 0:
        r += alp[n % b]
        n //= b
    return r[::-1]
for x in range(1, 2030 + 1):
    n = 7**91 + 7**160 - x
    s = convert(n, 7)
    if s.count('0') == 70:
        k.append(x)
print (max(k))
"""
"2"
"""alp = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
def convert(n, b):
    r = ''
    while n > 0:
        r += alp[n % b]
        n //= b
    return r[::-1]
f = 3 * 3125 ** 9 +2 * 625 ** 8 - 4 * 625 ** 7 + 3 * 125 ** 6 - 2 * 25 ** 5 - 2024
f = convert(f, 25)
if f [0] != "0":
    f = f.count('0')
print (f)"""
"""
M = []
alp = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
for x in alp[:32]:
    A = int(f'931{x}964', 32)
    B = int(f'4{x}51{x}1', 32)
    C = int(f'2861{x}637', 32)
    if (A + B + C) % 31 == 0:
        M.append(x)

A = int('931C964', 32)
B = int('4C51C1', 32)
C = int('2861C637', 32)

print ((A + B + C) // 31)"""

"""M = []
alp = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
for x in alp[:19]:
    A = int (f'98897{x}21', 19)
    B = int (f'2{x}923', 19)
    if (A + B) % 18 == 0:
        M.append(x)
c = max(M)
print ((int(f'98897{c}21', 19)+ int (f'2{c}923', 19)) // 18)"""

"""alp = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
def convert(n, b):
    r = ''
    while n > 0:
        r += alp[n % b]
        n //= b
    return r[::-1]
for x in range(1, 2030 + 1):
    f = 6 ** 260 + 6 ** 160 + 6 ** 60 - x
    s = convert(f, 6)
    if s.count('0') == 202:
        print(x)
        break"""

#№ 28935 ЕГКР 18.04.26 (Уровень: Базовый)
"""
alp = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
for x in alp[:23]:
    A = int(f'761{x}035', 23)
    B = int(f'338{x}932', 23)
    if (A + B) % 22 == 0:
        print(min(x))
        
A = int(f'761{8}035', 23)
B = int(f'338{8}932', 23)
print ((A + B) // 22)"""


# КЕГЭ № 17633 Основная волна 19.06.24 (Уровень: Базовый)

# Значение арифметического выражения 6**260 + 6**160 + 6**60 – х,
# где х – целое положительное число, не превышающее 2030, записали в 6-ричной системе счисления.

# Определите наименьшее значение х, при котором количество нулей в 6-ричной записи числа,
# являющегося значением данного арифметического выражения, равно 202.
'''
alp = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')

def convert(n, b):
    r = ''
    while n > 0:
        r = alp[n % b] + r
        n //= b
    return r

RES = []
for x in range(1, 2030):
    n = 6**260 + 6**160 + 6**60 - x
    s = convert(n, 6)
    if s.count('0') == 202:
        RES.append(x)
print(min(RES))
'''

# № 23753 Демоверсия 2026 (Уровень: Базовый)  КИРИЛЛ
# Операнды арифметического выражения записаны в системе счисления с основанием 29.

# 923x874_29 + 524x6152_29

# В записи чисел переменной x обозначена неизвестная цифра из алфавита 29-ричной системы счисления.
# Определите наибольшее значение x, при котором значение данного арифметического выражения кратно 28.
# Для найденного x вычислите частное от деления значения арифметического выражения на 28
# и укажите его в ответе в десятичной системе счисления.
"""RES =[]
alp = sorted("QWERTYUIOPASDFGHJKLZXCVBNM0123456789")

def convert(n,b):
    r = ""
    while n > 0:
        r = alp[n%b] 
        n//=b
    return r[::-1]

for x in alp[:29]:
    p = int(f'923{x}874', 29)
    m = int(f'524{x}6152', 29)
    if (p+m) % 28 == 0:
        RES.append((p+m)//28)
print(max(RES))"""

# № 21413 Досрочная волна 2025 (Уровень: Базовый)  ДИМА
# Операнды арифметического выражения записаны в системе счисления с основанием 21.

# 82934x2_21 + 2924xx7_21 +67564x8_21

# В записи чисел переменной x обозначена неизвестная цифра из алфавита 21-ричной системы счисления.
# Определите наименьшее значение x, при котором значение данного арифметического выражения кратно 20.
# Для найденного значения x вычислите частное от деления значения
# арифметического выражения на 20 и укажите его в ответе в десятичной системе счисления.

'''
RES = []
alp = sorted("0123456789QWERTYUIOPASDFGHJKLZXCVBNM")

for x in alp[:21]:
    A = int(f'82934{x}2', 21)
    B = int(f'2924{x}{x}7', 21)
    C = int(f'67564{x}8', 21)
    if (A  + B + C) % 20 == 0:
        RES.append((A + B + C)//20)
print(min(RES))
'''

# № 23198 Основная волна 10.06.25 (Уровень: Базовый)  КИРИЛЛ

# Значение арифметического выражения 9**150 + 9**30 – x, где
# x – целое положительное число, не превышающее 3000, записали в девятеричной системе счисления.
# Определите наименьшее значение x, при котором в девятеричной записи числа,
# являющегося значением данного арифметического выражения, содержится ровно 122 нуля.
# В ответе запишите число в десятичной системе счисления.
'''
RES = []

alp = sorted("0123456789QWERTYUIOPASDFGHJKLZXCVBNM")


def convert(n, b):
    r = ""
    while n > 0:
        r += alp[n % b]
        n //= b
    return r[::-1]


for x in range(1, 3000):
    p = 9 ** 150 + 9 ** 30 - x
    s = convert(p, 9)
    if s.count("0") == 122:
        RES.append(x)
print(min(RES))
'''

# № 21900 Открытый вариант 2025 (Уровень: Базовый)   ДИМА
# Значение арифметического выражения 7**350 + 7**150 – x, где x – целое положительное число,
# не превышающее 2300, записали в семеричной системе счисления.
# Определите наибольшее значение x, при котором в семеричной записи числа,
# являющегося значением данного арифметического выражения, содержится ровно 200 нулей.

'''
RES = []
alp = sorted("0123456789QWERTYUIOPASDFGHJKLZXCVBNM")


def convert(n, b):
    r = ""
    while n > 0:
        r += alp[n % b]
        n //= b
    return r[::-1]


for x in range(1, 2300):
    A = 7 ** 350 + 7 ** 150 - x
    s = convert(A, 7)
    if s.cound("0") == 200:
        RES.append(x)
print(max(RES))
'''

# № 21709 ЕГКР 19.04.25 (Уровень: Базовый)

# Значение арифметического выражения 4210 + 4110 – x, где x – целое положительное число, не превышающее 3000,
# записали в четверичной системе счисления. Определите наименьшее значение x, при котором в четверичной записи числа,
# являющегося значением данного арифметического выражения, содержится наибольшее количество нулей.

# В ответе запишите число в десятичной системе счисления.

RES = []

"""
def convert(n, b):
    r = ''
    while n > 0:
        r += str(n % b)
        n //= b
    return r[::-1]


for x in range(1, 3000 + 1):
    n = 4 ** 210 + 4 ** 110 - x
    s = convert(n, 4)
    RES.append(s.count('0'))

    if s.count('0') == 105:
        print(x)
        # 1024
        # 2048

print(max(RES))"""
'''
Запустите бота: https://t.me/ilandroxxy_bot и нажмите кнопку: "📚 Получить конспект"
'''
# endregion Место для вашего конспекта ⬆️

# Домашка 14 номер: https://stepik.org/lesson/1038703/step/1?unit=1062210

# Практика 14 номер: https://stepik.org/lesson/1227100/step/1?unit=1240618
