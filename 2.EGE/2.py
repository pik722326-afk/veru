# 📚 Полезные ссылки на статьи и разборы задач:
# 📘 Полная версия шпаргалки доступна в нашем тг канале: https://t.me/informatika_kege_itpy/362?comment=6532
# 📘 Разборы 2 номеров по информатике: https://t.me/informatika_kege_itpy/360?comment=1461

# region Место для вашего конспекта ⬇️
print ("x y z w") #Выводим названия перименных
for x in range(2): #Проверяем каждые переменные на соотвецтвие
    for y in range (2):
        for z in range (2):
            for  w in range (2):
                F = ((y <= w) == (x <= (not z))) and (x or w)#Преобразуем формулу
                if F == 1: #Выводим значение F которые нам нужны
                    print (x , y , z , w, F) #Выводим перименные
for x in range(2):
    for y in range (2):
        for z in range (2):
            for  w in range (2):
                F = ((y <= w) == (x <= (not z))) and (x or w)
                if F == 0:
                    print (x , y , z , w, F)
'''((y → w) ≡ (x → ¬z)) ∧ (x ∨ w)'''
#Номер 1 (x∨¬y)∧¬(y≡z)∧¬w
#(x or (not y)) and (not(y == z)) and (not w)

#Номер 2 (х→y)∨¬(w→z)
#(x<= y) or (not(w <= z))

'''
print('x y z w')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                F = (not (x <= w)) or (y <= z) or (not (y))
                if F == 0:
                    print(x, y, z, w, int(F))
'''

'''(x ∧ ¬y) ∨ (y ≡ z) ∨'''

'''¬(x → w) ∨ (y → z) ∨ ¬y'''
""'y ∧ (x ∨ z) ∨ ¬(y ∨ z) ∨ w"'

"(y → ¬(x → z)) ∨ w"

"""""(x ∧ ¬y) ∨ (x ≡ z) ∨ w"""""

"""¬(x → z) ∨ (y ≡ w) ∨ y"""

"""" ¬(x ∨ y) ∧ ¬w ∨ ¬(z ∨ w) ∧ y"""
'''F = (not (x or y)) and (not w) or (not (z or w)) and y'''




'''
Запустите бота: https://t.me/ilandroxxy_bot и нажмите кнопку: "📚 Получить конспект"
'''
# Место для вашего конспекта ⬆️


print('x y z w')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                F = (x or y) and (not(y == z)) and (not w)
                if F == 1:
                    print(x, y, z, w)
'''
from tkinter import image_names

# Решу ЕГЭ № 18483 (Уровень: Базовый)
'''
print('x y z w F')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                F = ((y <= w) == (x <= (not z))) and (x or w)
                if F == 0:
                    print(x, y, z, w, int(F))

for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                F = ((y <= w) == (x <= (not z))) and (x or w)
                if F == 1:
                    print(x, y, z, w, int(F))
'''
# № 20569 (Уровень: Базовый)
'''
print('x y z w F')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                F = ((w <= z) == (x <= (not y))) and (x or z)
                if F == 0:
                    print(x, y, z, w, int(F))

for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                F = ((w <= z) == (x <= (not y))) and (x or z)
                if F == 1:
                    print(x, y, z, w, int(F))
'''


# Домашка 2 номер: https://stepik.org/lesson/1038536/step/1?unit=1062771

# Практика 2 номер: https://stepik.org/lesson/1152671/step/1?unit=1164793 '''
