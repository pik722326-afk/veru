# 📚 Полезные ссылки на статьи и разборы задач:
# 📘 Полная версия шпаргалки доступна в нашем тг канале: https://t.me/informatika_kege_itpy/362?comment=6532
# 📘 Разборы 19-21 номеров по информатике: https://t.me/informatika_kege_itpy/360?comment=1802

# region Место для вашего конспекта ⬇️

#Шаблон для решения теории игры 19-21 номера:
"""def F(s, n):
    if s >= __ :
        return n % 2 == 0
    if n == 0:
        return 0
    h = [F(s __ , n-1), F(s __ , n-1), F(s __ , n-1)]
    return any(h) if (n - 1) % 2 == 0 else all(h)  # else any(h) - all Выйгрыш ani - проигрыш

print([s for s in range(1, __ +1) if F(s, n=2)])
print([s for s in range(1, __ +1) if F(s, n=3) and not F(s, n=1)])
print([s for s in range(1, __ +1) if F(s, n=4) and not F(s, n=2)])"""
#Шаблон решения 2 кучи
"""def F(a, s, n):
    if a + s >= __ : #+-*/ Смотреть по условию 
        return n % 2 == 0
    if n == 0:
        return 0
    h = [F(а__, s , n-1), F(a, s__, n-1), F(a__, s , n-1), F(a, s__, n-1)]
    return any(h) if (n - 1) % 2 == 0 else all(h)  # else any(h)

print([s for s in range(_, 1000+1) if F(7, s, n=2)]) Если куча убывает то от 1000 до значения победы 
print([s for s in range(1, __+1) if F(7, s, n=3) and not F(7, s, n=1)]) Если куча возрастает то от 1 до значения победы 
print([s for s in range(_, __+1) if F(7, s, n=4) and not F(7, s, n=2)])"""

#Пример решения задачи на 1 кучу (возрастание):
"""#Открытый вариант 2025 (Уровень: Базовый)
# 1 куча: +1, +4, *3 | s >= 67 | 1 ≤ s ≤ 66

# s - это кол-во камней в куче (то что ищем)
# n - это шаг нашей игры

# n = 1 - Петя первый ход
# n = 2 - Ваня первый ход
# n = 3 - Петя второй ход
# n = 4 - Ваня второй ход
def F(s, n):
    if s >= 67:
        return n % 2 == 0
    if n == 0:
        return 0
    h = [F(s + 1, n-1), F(s + 4, n-1), F(s * 3, n-1)]
    return any(h) if (n - 1) % 2 == 0 else all(h)  # else any(h)

print([s for s in range(1, 66+1) if F(s, n=2)])
print([s for s in range(1, 66+1) if F(s, n=3) and not F(s, n=1)])
print([s for s in range(1, 66+1) if F(s, n=4) and not F(s, n=2)])
"""

#Пример решения задачи на 1 кучу (убывание):
"""# № 23759 Демоверсия 2026 (Уровень: Базовый)
# 1 куча: -3, -5, /4 (до меньшего) | s <= 30 | s ≥ 31
from math import ceil, floor 
def F(s, n):
    if s <= 30:
        return n % 2 == 0
    if n == 0:
        return 0
    h = [F(s - 3 , n-1), F(s - 5 , n-1), F(floor(s / 4) , n-1)]
    return any(h) if (n - 1) % 2 == 0 else all(h)  # else any(h)

print([s for s in range(31, 1000) if F(s, n=2)])
print([s for s in range(31, 1000) if F(s, n=3) and not F(s, n=1)])
print([s for s in range(31, 1000) if F(s, n=4) and not F(s, n=2)])
"""

#Пример решения задачи на 2 кучи (возрастание):
"""# № 20907 Апробация 05.03.25 (Уровень: Базовый)
# 2 кучи: a+1, s+1, a*2, s*2 | a+s >= 81 | a=7 | 1 ≤ s ≤ 73
def F(a, s, n):
    if a + s >= 81 :
        return n % 2 == 0
    if n == 0:
        return 0
    h = [F(a+1, s , n-1), F(a, s+1, n-1), F(a*2, s , n-1), F(a, s*2, n-1)]
    return any(h) if (n - 1) % 2 == 0 else all(h)  # else any(h)

print([s for s in range(1, 73+1) if F(7, s, n=2)])
print([s for s in range(1, 73+1) if F(7, s, n=3) and not F(7, s, n=1)])
print([s for s in range(1, 73+1) if F(7, s, n=4) and not F(7, s, n=2)])
"""

#Пример решения задачи на 2 кучи (убывание):
"""# № 18268 (Уровень: Базовый)
# 2 кучи: a-3, s-3, a/2, s/2 (в большее) | a+s <= 72 | a = 50 | s > 22
from math import ceil
def F(a, s, n):
    if a + s <= 72:
        return n % 2 == 0
    if n == 0:
        return 0
    h = [F(a-3, s , n-1), F(a, s-3, n-1), F(ceil(a / 2), s , n-1), F(a, ceil(s / 2), n-1)]
    return any(h) if (n - 1) % 2 == 0 else all(h)  # else any(h)

print([s for s in range(23, 1000) if F(50, s, n=2)])
print([s for s in range(23, 1000) if F(50, s, n=3) and not F(50, s, n=1)])
print([s for s in range(23, 1000) if F(50, s, n=4) and not F(50, s, n=2)])
"""

#                         03.03.2026
#__________________________________________________________________________________

#№ 25358 ЕГКР 13.12.25 (Уровень: Базовый) 1 куча увеличение
"""def F(s, n):
    if s >= 125:
        return n % 2 == 0
    if n == 0:
        return 0
    h = [F(s + 2, n - 1), F(s + 4, n - 1), F(s * 2, n -1)]
    return any(h) if (n - 1) % 2 == 0 else all(h)
print ([s for s in range (1, 124+1) if F(s, n = 2)])
print ([s for s in range (1, 124+1) if F(s, n = 3) and not F(s, n = 1)])
print ([s for s in range (1, 124+1) if F(s, n = 4) and not F(s, n = 2)])"""

#№ 23759 Демоверсия 2026 (Уровень: Базовый) 1 куча вниз
"""# -3, -5, /4,|s <= 30|s >= 31|
from math import ceil, floor
def F(s, n):
    if s <= 30:
        return n % 2 == 0
    if n == 0:
        return 0
    h = [F(s - 3, n - 1), F(s - 5, n -1), F (floor(s / 4), n - 1)]
    return any(h) if (n - 1) % 2 == 0 else all(h)
print ([s for s in range(31, 1000) if F(s, n = 2)])
print ([s for s in range(31, 1000) if F(s, n = 3) and not F(s, n = 1)])
print ([s for s in range(31, 1000) if F(s, n = 4) and not F(s, n = 2)])"""

#№ 23565 Пересдача 03.07.25 (Уровень: Базовый) 1 уча вниз
"""# -3, -8, /3, |s <= 15| s >=16|
from math import ceil, floor
def F(s, n):
    if s <= 15:
        return n % 2 == 0
    if n == 0:
        return 0
    h = [F(s - 3, n - 1), F(s -8, n - 1), F(floor(s / 3), n - 1)]
    return any(h) if (n - 1) % 2 == 0 else all(h)
print ([s for s in range(16, 1000) if F(s, n = 2)])
print ([s for s in range(16, 1000) if F(s, n = 3) and not F(s, n = 1)])
print ([s for s in range(16, 1000) if F(s, n = 4) and not F(s, n = 2)])
"""

#№ 23378 Резервный день 19.06.25 (Уровень: Базовый) 1 куча вниз
"""#   -6, -3 /3| S <= 27|S >= 28|
from math import ceil, floor
def F(s, n):
    if s <= 27:
        return n % 2 == 0
    if n == 0:
        return 0
    h = [F(s - 3, n - 1), F(s - 6, n - 1), F(floor(s / 3), n -1)]
    return any(h) if (n - 1) % 2 == 0 else all(h)
print ([s for s in range(28, 1000) if F(s, n = 2)])
print ([s for s in range(28, 1000) if F(s, n = 3) and not F(s, n = 1)])
print ([s for s in range(28, 1000) if F(s, n = 4) and not F(s, n = 2)])"""

#№ 21905 Открытый вариант 2025 (Уровень: Базовый) 1 куча вверх
"""# +1 +4 *3 | s <= 65 | 1 ≤ S ≤ 66 |
def F(s, n):
    if s >= 67:
        return n % 2 == 0
    if n == 0:
        return 0
    h = [F(s + 1, n - 1), F(s + 4, n - 1), F(s * 3, n - 1)]
    return any(h) if (n - 1) % 2 == 0 else all(h)
print ([s for s in range (1, 66 + 1) if F(s, n = 2)])
print ([s for s in range (1, 66 + 1) if F(s, n = 3) and not F(s, n = 1)])
print ([s for s in range (1, 66 + 1) if F(s, n = 4) and not F(s, n = 2)])"""



#Пример решения задачи на 2 кучи (возрастание):
"""# № 20907 Апробация 05.03.25 (Уровень: Базовый)
# 2 кучи: a+1, s+1, a*2, s*2 | a+s >= 81 | a=7 | 1 ≤ s ≤ 73
def F(a, s, n):
    if a + s >= 81 :
        return n % 2 == 0
    if n == 0:
        return 0
    h = [F(a+1, s , n-1), F(a, s+1, n-1), F(a*2, s , n-1), F(a, s*2, n-1)]
    return any(h) if (n - 1) % 2 == 0 else all(h)  # else any(h)

print([s for s in range(1, 73+1) if F(7, s, n=2)])
print([s for s in range(1, 73+1) if F(7, s, n=3) and not F(7, s, n=1)])
print([s for s in range(1, 73+1) if F(7, s, n=4) and not F(7, s, n=2)])
"""

#№ 27774 Апробация 04.03.26 (Уровень: Базовый)
"""# 2 кучи: a+1, s+1, a*2, s*2 | a+s >= 207 | a=17 | 1 ≤ s ≤ 189
def F(a, s, n):
    if a + s >= 207:
        return n % 2 == 0
    if n == 0:
        return 0
    h = [F(a+1, s , n-1), F(a, s+1, n-1), F(a*2, s , n-1), F(a, s*2, n-1)]
    return any(h) if (n - 1) % 2 == 0 else all(h)

print ([s for s in range(1, 189+1) if F(17, s, n=2)])
print ([s for s in range(1, 189+1) if F(17, s, n=3) and not F(17, s, n=1)])
print ([s for s in range(1, 189+1) if F(17, s, n=4) and not F(17, s, n=2)])"""





