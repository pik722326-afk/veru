# 📚 Полезные ссылки на статьи и разборы задач:
# 📘 Полная версия шпаргалки доступна в нашем тг канале: https://t.me/informatika_kege_itpy/362?comment=6532
# 📘 Разборы 16 номеров по информатике: https://t.me/informatika_kege_itpy/360?comment=1609

# region Место для вашего конспекта ⬇️
#Если вылазиет ошибка
#import sys
#sys.setrecursionlimit(10**8)

#Если очень долго считает

#from functools import *
#@lru_cache(None)


#for n in range(200):
#    F(n)

#-------------------------

#Разбор на уроке
"""
# № 21902 Открытый вариант 2025 (Уровень: Базовый)
'''
def F(n):
    if n >= 2025:
        return n
    if n < 2025:
        return n * 2 + F(n + 2)

print(F(82) - F(81))
'''


# № 21415 Досрочная волна 2025 (Уровень: Базовый)
'''
import sys
sys.setrecursionlimit(10**8)

def F(n):
    if n <= 5:
        return 1
    if n > 5:
        return n + F(n - 2)

print(F(2126) - F(2122))
# [Previous line repeated 996 more times]
# RecursionError: maximum recursion depth exceeded


# F(2126) = 2126 + F(2124)
# F(2124) = 2124 + F(2122) - F(2122)
print(2126 + 2124)
'''


# № 20906 Апробация 05.03.25 (Уровень: Базовый)
'''
import sys
sys.setrecursionlimit(10**8)

def F(n):
    if n == 1:
        return 1
    if n > 1:
        return n * F(n - 1)

print((F(2024) // 4 + F(2023)) // F(2022))
'''
# print((F(2024) / 4 + F(2023)) / F(2022))
#            ~~~~^~~
# OverflowError: integer division result too large for a float



# № 23756 Демоверсия 2026 (Уровень: Базовый)
'''
import sys
sys.setrecursionlimit(10**8)

def F(n):
    return 2 * (G(n - 3) + 8)

def G(n):
    if n < 10:
        return 2 * n
    if n >= 10:
        return G(n - 2) + 1

print(F(15548))
'''



# № 13297 Открытый курс "Слово пацана" (Уровень: Базовый)
'''
def F(n):
    if n == 3:
        return 1
    if n > 3:
        return 5 * F(n-1)+6 * G(n-1) - 3*n+8

def G(n):
    if n == 3:
        return 1
    if n > 3:
        return 6 * F(n - 1) + 5 * G(n - 1) + 3

print(F(9) + G(9))
'''


# № 10718 (Уровень: Средний)
'''
from functools import *
@lru_cache(None)
def F(n):
    if n < 3:
        return 2
    if n > 2 and n % 2 == 0:
        return 2 * F(n - 2) - F(n - 1) + 2
    if n > 2 and n % 2 != 0:
        return 2 * F(n - 1) + F(n - 2) - 2

for n in range(200):
    F(n)

print(F(170))
'''
"""


#КЕГЭ № 1020 (Уровень: Базовый)
"""
def F(n):
    if n <= 3:
        return 2
    if n > 3 and n % 2 == 0:
        return F(n // 2) + 5
    if n > 3 and n % 2 != 0:
        return F(n - 1) - F(n - 2)
print (F(20))
"""

#КЕГЭ № 23756 (Уровень: Базовый)
"""
import sys
sys.setrecursionlimit(10**8)

def F(n):
    return 2 * (G(n - 3) + 8)
def G(n):
    if n < 10:
        return 2 * n
    if n >= 10:
        return G(n - 2) + 1
print (F(15548))
"""

#КЕГЭ № 17635 (Уровень: Базовый)
"""
import sys
sys.setrecursionlimit(10**8)

def F(n):
    if n == 1:
        return 1
    if n > 1:
        return (n + 1) * F(n - 1)
print((F(2024) - 3 * F(2023)) // F(2022))
"""

#КЕГЭ № 699 (Уровень: Базовый)
"""
def F(n):
    if n <= 1:
        return 1
    if n > 1 and n % 2 == 0:
        return n * F(n - 1)
    if n > 1 and n % 2 != 0:
        return n + F(n - 2)
print(F(84))
"""

#КЕГЭ № 7818 (Уровень: Базовый)
"""
def F(n):
    if n >= 2073:
        return n + 3
    if n <= 2073:
        return n + F(n + 2) - F(n + 3)
print (F(2070)  +  F(2069))
"""

#КЕГЭ № 4266 (Уровень: Средний)
"""
def F(n):
    if n <= 2:
        return 2
    if n > 2:
        return F(n - 1) - 2 * F(n - 2)

print (F(37))
"""

#КЕГЭ № 17557 (Уровень: Базовый)
"""
import sys
sys.setrecursionlimit(10**8)

def F(n):
    if n == 1:
        return 1
    if n > 1:
        return 2 * n * F(n - 1)
print ((F(2024) // 16 - F(2023)) // F(2022))
"""


'''
Запустите бота: https://t.me/ilandroxxy_bot и нажмите кнопку: "📚 Получить конспект"
'''
# endregion Место для вашего конспекта ⬆️

# Домашка 16 номер: https://stepik.org/lesson/1038709/step/1?unit=1062775

# Практика 16 номер: https://stepik.org/lesson/1228671/step/1?unit=1242204
