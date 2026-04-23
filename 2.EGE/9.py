# 📚 Полезные ссылки на статьи и разборы задач:
# 📘 Полная версия шпаргалки доступна в нашем тг канале: https://t.me/informatika_kege_itpy/362?comment=6532
# 📘 Разборы 9 номеров по информатике: https://t.me/informatika_kege_itpy/360?comment=1472

# region Место для вашего конспекта ⬇️
'''
Запустите бота: https://t.me/ilandroxxy_bot и нажмите кнопку: "📚 Получить конспект"
'''
# endregion Место для вашего конспекта ⬆️

"""
for s in open('files/9.csv'):
    M = [int(x) for x in s.split(';')]
        
# Домашка 9 номер: https://stepik.org/lesson/1038670/step/1?unit=1062777
#повторяющееся число строки больше, чем среднее арифметическое её неповторяющихся чисел.
# Практика 9 номер: https://stepik.org/lesson/1228674/step/1?unit=1242207
cnt = 0
for s in open('files/9.csv'):
    M = [int(x) for x in s.split(';')]
    copied1 = [x for x in M if M.count(x) == 1]
    copied3 = [x for x in M if M.count(x) == 3]
    if len(copied3) == 3 and len(copied1) == 3:
        cnt += 1
    if copied3[0] >= cum (copied1/len copied1):

sum m +=ф copied1[0]
        cnt += 1
"""
#№ 25348 (Уровень: Базовый)
# Откройте файл электронной таблицы, содержащей в каждой строке семь целых чисел.
# Определить количество строк таблицы, для которых выполнены оба условия:
# - в строке одно число повторяется трижды, остальные числа различны;
# - максимальное число строки не повторяется.
# В ответе запишите только число.
'''
cnt = 0
for s in open('files/9.csv'):
    M = [int(x) for x in s.split(',')]
    copied3 = [x for x in M if M.count(x) == 3]
    copied1 = [x for x in M if M.count(x) == 1]
    if len(copied3) == 3 and len(copied1) == 4:
        # if max(M) in copied1:
        if M.count(max(M)) == 1:
            cnt += 1
print(cnt)
'''


# Откройте файл электронной таблицы, содержащей в каждой строке пять натуральных чисел.
# Определите количество строк таблицы, содержащих числа, для которых выполнены оба условия:
# квадрат наибольшего значения больше произведения остальных чисел;
# сумма двух наибольших значений как минимум вдвое больше суммы остальных значений в строке.
'''
cnt = 0
for s in open('files/9.csv'):
    M = [int(x) for x in s.split(',')]
    M = sorted(M)
    if max(M) ** 2 > M[0] * M[1] * M[2] * M[3]:
        if M[-1] + M[-2] >= (2 * (M[0] + M[1] + M[2])):
            cnt += 1
print(cnt)
'''


# Откройте файл электронной таблицы, которая содержит в каждой строке семь натуральных чисел.
# Определите количество строк таблицы, для чисел которых выполнены все условия:
# в строке есть число, которое повторяется трижды
# в строке ровно 5 различных значений
# сумма чисел в строке меньше 502
'''
cnt = 0
for s in open('files/9.csv'):
    M = [int(x) for x in s.split(';')]
    copied3 = [x for x in M if M.count(x) == 3]
    if len(copied3) > 0:
        if len(set(M)) == 5:
            if sum(M) < 502:
                cnt += 1
print(cnt)
'''


# Определите количество строк таблицы, содержащих числа, для которых
# выполнено только одно из условий:
# в строке только одно число повторяется дважды, а остальные не повторяются;
# в строке среднее арифметическое чётных чисел отличается от среднего
# арифметического нечётных чисел более чем на 50.
'''
cnt = 0
for s in open('files/9.csv'):
    M = [int(x) for x in s.split(',')]
    flag = 0
    copied2 = [x for x in M if M.count(x) == 2]
    copied1 = [x for x in M if M.count(x) == 1]
    if len(copied2) == 2 and len(copied1) == 4:
        flag += 1
    chet = [x for x in M if x % 2 == 0]
    nechet = [x for x in M if x % 2 != 0]
    if len(chet) == 0:
        avg2 = 0
    else:
        avg2 = sum(chet) / len(chet)
    if len(nechet) == 0:
        avg1 = 0
    else:
        avg1 = sum(nechet) / len(nechet)
    if abs(avg2 - avg1) > 50:
        flag += 1
    if flag == 1:
        cnt += 1
print(cnt)
'''


# https://education.yandex.ru/ege/inf/task/622b91cc-fe32-4b92-9127-6137aae32039
# Откройте файл электронной таблицы, содержащей в каждой строке пять натуральных чисел.
# Определите количество строк таблицы, для чисел которых выполнены оба условия:
# в строке все числа различны;
# сумма двух наибольших чисел строки не больше суммы трёх её оставшихся чисел.
'''
cnt = 0
for s in open('files/9.csv'):
    M = [int(x) for x in s.split(';')]
    copied1 = [x for x in M if M.count(x) == 1]
    M = sorted(M)
    if len(copied1) == len(M):
        if M[-1]+M[-2] <= M[0]+M[1]+M[2]:
            cnt += 1
print(cnt) #1922
'''


# https://education.yandex.ru/ege/inf/task/2f370a43-39d3-4557-97a3-920195435a5d
# Откройте файл электронной таблицы, содержащей в каждой строке пять натуральных чисел.
# Определите количество строк таблицы, содержащих числа, для которых выполнены оба условия:
# в строке все числа различны;
# утроенная сумма минимального и максимального чисел строки не меньше, чем удвоенная сумма трёх её оставшихся чисел.
'''
cnt = 0
for s in open('files/9 (1).csv'):
    M = [int(x) for x in s.split(';')]
    M = sorted(M)
    # copied1 = [x for x in M if M.count(x) == 1]
    # if len(copied1) == 5:
    if len(set(M)) == 5:
        if (M[0] + M[-1]) * 3 >= (M[1] + M[2] + M[3]) * 2:
            cnt += 1
print(cnt)#Answer: 7695
'''


# https://education.yandex.ru/ege/inf/task/c51900be-b855-4ffb-97d5-8402bb52ffd8
# Откройте файл электронной таблицы, содержащей в каждой строке четыре натуральных числа.
# Определите количество строк таблицы, содержащих числа, для которых выполнены оба условия:
# наибольшее из четырёх чисел меньше суммы трёх других;
# четыре числа нельзя разбить на две пары чисел с равными суммами.
"""
from itertools import permutations
cnt = 0
for s in open('files/9.csv'):
    M = [int(x) for x in s.split(';')]
    if max(M) < sum(M) - max(M):
        if all(p[0] + p[1] != p[2] + p[3] for p in permutations(M)):
            cnt += 1
print(cnt)"""


# № 27764 Апробация 04.03.26 (Уровень: Базовый)
# Откройте файл электронной таблицы, содержащий в каждой строке пять натуральных чисел.
# Определите количество строк таблицы, для которых выполнены оба условия:
# - в строке все числа различны;
# - удвоенная сумма максимального и минимального чисел строки равна сумме оставшихся трёх её чисел.

"""
cnt = 0
for s in open("files/9.ods"):
    M = [int(x) for x in s.split(",")]
    # copied1 = [x for x in M if M.count(x) == 1]
    # if len(copied1) == 5:
    if len(M) == len(set(M)):  # - в строке все числа различны;
        M = sorted(M)
        if (max(M) + min(M)) * 2 == (M[1] + M[2] + M[3]):
           # cnt = cnt + 1
           cnt += 1
print(cnt)"""


 #№ 27287 (Уровень: Базовый)

# В файле электронной таблицы в каждой строке записаны семь целых чисел.
# Определите наибольшее повторяющееся число в строке таблице с наименьшим номером, для которой выполнены оба условия:
# – в строке два разных числа повторяются трижды, одно число не повторяется;
# – неповторяющееся число не больше минимального из повторяющихся чисел строки.
# В ответе запишите абсолютное значение полученного результата.
"""
for s in open("files/9.ods"):
    M = [int(x) for x in s.split(",")]
    copied1 = [x for x in M if M.count(x) == 1]
    copied3 = [x for x in M if M.count(x) == 3]
    if len(copied3) == 6 and len(copied1) == 1:
        if copied1[0] >= min(copied3):
            print(max(copied3))
             break
"""


# № 25348 ЕГКР 13.12.25 (Уровень: Базовый)
# Откройте файл электронной таблицы, содержащей в каждой строке семь целых чисел.
# Определить количество строк таблицы, для которых выполнены оба условия:
# - в строке одно число повторяется трижды, остальные числа различны;
# - максимальное число строки не повторяется.
# В ответе запишите только число.
'''
cnt = 0
for s in open("files/9.ods"):
    M = [int(x) for x in s.split(",")]
    copied1 = [x for x in M if M.count(x) == 1]
    copied3 = [x for x in M if M.count(x) == 3]
    if len(copied3) == 3 and len(copied1) == 4:
        if max(M) not in copied3:
            cnt += 1 
print (cnt)
   '''

#КЕГЭ № 17550 Основная волна 08.06.24 (Уровень: Базовый)
#Откройте файл электронной таблицы, содержащей в каждой строке
# шесть натуральных чисел. Определите количество строк таблицы,
# содержащих числа, для которых выполнены оба условия:
#– в строке только одно число повторяется трижды, остальные числа различны;
#– квадрат суммы всех повторяющихся чисел строки больше
# квадрата суммы всех её неповторяющихся чисел.
"""cnt = 0
for s in open("files/9_17550.csv"):
    M = [int(x) for x in s.split(";")]
    copied1 = [x for x in M if M.count(x) == 3]
    copied2 = [x for x in M if M.count(x) == 1]
    if len(copied1) == 3 and len(copied2) == 3:
        if sum(copied1) ** 2 > sum(copied2) ** 2:
            cnt += 1
print (cnt)
"""

#КЕГЭ № 12463 (Уровень: Базовый)
#– в строке есть одно число, которое повторяется четыре раза,
# – есть другое число, которое повторяется дважды,
# – остальные три числа различны;
# – среднее арифметическое трёх неповторяющихся чисел
# строки не меньше наибольшего из повторяющихся в строке чисел.
"""cnt = 0
for s in open("files/9_12463.csv"):
    M = [int(x) for x in s.split(",")]
    copied1 = [x for x in M if M.count(x) == 4]
    copied2 = [x for x in M if M.count(x) == 2]
    copied3 = [x for x in M if M.count(x) == 1]
    if len(copied1) == 4 and len(copied2) == 2 and len(copied3) == 3:
        if sum(copied3) / len(copied3) >= max(copied1[0], copied2[0]):
            cnt += 1
print (cnt)"""


#КЕГЭ № 11946 (Уровень: Средний)
#– в строке есть одно число, которое повторяется трижды,
# остальные четыре числа различны;
#– числа в строке расположены в порядке неубывания.
"""cnt = 0
for s in open("files/9_11946.csv"):
    M = [int(x) for x in s.split(";")]
    copied1 = [x for x in M if M.count(x) == 3]
    copied2 = [x for x in M if M.count(x) == 1]
    if (len(copied1) == 3 and len(copied2) == 4) + (M == sorted(M)) <= 1:
            cnt += 1
print (cnt)
"""

#КЕГЭ № 10026 (Уровень: Средний)
#– числа в строке расположены в порядке возрастания;
#– в строке есть повторяющиеся числа.
"""cnt = 0
n = 0
for s in open("files/9_10026.csv"):
    M = [int(x) for x in s.split(";")]
    copied1 = [x for x in M if M.count(x) >= 2]
    cnt += 1
    if (len(copied1) > 0) + (sorted(M) == M) >= 1:
        n += cnt
print (n)"""

#КЕГЭ № 9696 (Уровень: Средний)
#— только одно число встречается в строке дважды
#— сумма двух самых больших чисел строки более
# чем в два раза больше суммы двух самых малых
#— максимальное число строки не кратно минимальному
"""cnt = 0
for s in open("files/9_9696.csv"):
    M = [int(x) for x in s.split(";")]
    copied1 = [x for x in M if M.count(x) == 2]
    copied2 = [x for x in M if M.count(x) == 1]
    if max(M) % min(M) != 0:
        M = sorted(M)
        if (M[-1] + M[-2]) > (M[0]+M[1]) * 2:
            if len(copied1) == 2 and len(copied2) == 2:
                cnt += 1
print (cnt)"""

#КЕГЭ № 8554 (Уровень: Средний)
#– Ровно три числа заканчиваются цифрой 3;
#– Квадрат суммы положительных чисел меньше
# квадрата суммы отрицательных чисел.
"""cnt = 0
for s in open("files/9_8554.csv"):
    M = [int(x) for x in s.split(";")]
    a = [x for x in M if abs(x) % 10 == 3]
    b = [x for x in M if x > 0]
    c = [x for x in M if x < 0]
    if len(a) == 3 and sum(b)**2 < sum(c)**2:
        cnt += 1
print (cnt)"""


#КЕГЭ № 11830 (Уровень: Средний)
#– в строке есть два числа, каждое из которых повторяется дважды,
#остальные три числа различны;
#– произведение всех повторяющихся чисел строки
#более чем вдвое превосходит произведение неповторяющихся чисел.
cnt = 0
from math import prod
for s in open("files/9_11830.csv"):
    M = [int(x) for x in s.split(";")]
    copied1 = [x for x in M if M.count(x) == 2]
    copied2 = [x for x in M if M.count(x) == 1]
    if prod(copied1) > prod(copied2) * 2:
        if len(copied1) == 4  and len(copied2) == 3:
            cnt += 1
print (cnt)

#КЕГЭ № 9778 Основная волна 20.06.23 (Уровень: Средний)
cnt = 0
for s in open("files/9_9778.csv"):
    M = [int(x) for x in s.split(";")]
    cnt += 1
    copied1 = [int (x) for x in M if M.count(x) == 2]
    copied2 = [int (x) for x in M if M.count(x) == 1]
    if len(copied1) == 2  and len(copied2) == 4:
        if copied1[0] >= sum(copied2) / len(copied2) :
            print (cnt)
            break








