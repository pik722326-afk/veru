# 📚 Полезные ссылки на статьи и разборы задач:
# 📘 Полная версия шпаргалки доступна в нашем тг канале: https://t.me/informatika_kege_itpy/362?comment=6532
# 📘 Разборы 6 номеров по информатике: https://t.me/informatika_kege_itpy/360?comment=1466

# region Место для вашего конспекта ⬇️
# В начальный момент Черепаха находится в начале координат,
# её голова направлена вдоль положительного направления оси ординат,
# хвост опущен.

# Домашка №6 шаг 2 https://stepik.org/lesson/1038843/step/2?unit=1062794
"""# Направо 120 Повтори 8 [Вперёд 4 Направо 60]
import turtle as t
t.screensize(500, 500)
t.tracer(0)
t.left(90)
s = 20
t.right(120)
for i in range(8):
    t.forward(4 * s)
    t.right(60)
t.up()
for x in range(-100, 100):
    for y in range(-100, 100):
        t.goto(x * s, y * s)
        t.dot(3, 'red')
t.update()
t.done()"""
# Домашка №6 шаг 3 https://stepik.org/lesson/1038843/step/3?unit=1062794
"""# Повтори 2 [Вперёд 10 Направо 90 Вперёд 18 Направо 90]
#   Поднять хво
#   Назад 6 Направо 90 Вперёд 9 Налево 90
#   Опустить хвост
#   Повтори 2 [Вперёд 17 Направо 90 Вперёд 5 Направо 90]
# Cколько точек с целочисленными координатами будут находиться внутри пересечения фигур, 
# ограниченных заданными алгоритмом линиями, 
# включая точки на линиях
#       Ответ 66
import turtle as t
t.screensize(5000, 5000)
t.left(90)
t.tracer(0)
s = 30
for i in range(2):
    t.color('red')
    t.forward(10 * s)
    t.right(90)
    t.forward(18 * s)
    t.right(90)
t.up()
t.backward(6 * s)
t.right(90)
t.forward (9 * s)
t.left(90)
t.down()
for i in range(2):
    t.color('red')
    t.forward(17 * s)
    t.right(90)
    t.fd (5 * s)
    t.right(90)
t.up ()
for x in range(-50, 50):
    for y in range(-50, 50):
        t.goto(x * s, y * s)
        t.dot(2,'purple')
t.update()
t.done()"""
# Домашка №6 шаг 4 https://stepik.org/lesson/1038843/step/4?unit=1062794
"""#Повтори 2 [Вперёд 7 Направо 60 Вперёд 12 Направо 120]
# Поднять хвост
# Вперёд 7 Направо 60
# Опустить хвост
# Повтори 2 [Вперёд 5 Направо 120 Вперёд 10 Направо 60]
# не включая точки на границах этого пересечения.

import turtle as t
t.screensize(5000, 5000)
t.tracer(0)
t.left(90)
s = 20
for i in range(2):
    t.color('red')
    t.forward(7 * s)
    t.right(60)
    t.forward(12 * s)
    t.right(120)
t.up()
t.forward(7 * s)
t.right(60)
t.down()
for i in range(2):
    t.color('red')
    t.forward(5 * s)
    t.right(120)
    t.forward(10 * s)
    t.right(60)
t.up()
for x in range(-50, 50):
    for y in range(-50, 50):
        t.goto(x * s, y * s)
        t.dot(2,'purple')
t.update()
t.done()"""
# Домашка №6 шаг 5 https://stepik.org/lesson/1038843/step/5?unit=1062794
# Определите периметр
# области пересечения фигур,
# ограниченных заданными алгоритмом линиями.

#Повтори 10 [Вперёд 22 Направо 90 Вперед 16 Направо 90]
#Поднять хвост
#Вперед 1 Направо 90 Вперёд 1 Налево 90
#Опустить хвост
#Повтори 10 [Вперёд 72 Направо 90 Вперёд 79 Направо 90]

import turtle as t
t.screensize(5000, 5000)
t.tracer(0)
t.left(90)
s = 20
for i in range(10):
    t.color('red')
    t.forward(22 * s)
    t.rt(90)
    t.fd(16 * s)
    t.right(90)
t.up()
t.fd(1  * s)
t.right(90)
t.forward(1*s)
t.left(90)
t.down()
for i in range(10):
    t.color('red')
    t.forward(72 * s)
    t.rt(90)
    t.fd(79 * s)
    t.right(90)
t.up()
for x in range(-50, 50):
    for y in range (-50, 50):
        t.goto(x * s, y * s)
        t.dot(2, "purple")
t.update()
t.done()
# Домашка №6 шаг 7 https://stepik.org/lesson/1038843/step/7?unit=1062794
"""#Сколько точек с целочисленными координатами находятся внутри получившейся фигуры?
#Точки на внешних и внутренних линиях учитывать не нужно.
#Повтори 6 [Повтори 3 [Вперед 7 Направо 120] Направо 60]
import turtle as t
t.screensize(-5000, 5000)
t.tracer(0)
t.left(90)
s = 20
for i in range(6):
    for i in range(3):
        t.color('red')
        t.fd(7*s)
        t.right(120)
    t.rt(60)
t.up()
for x in range (-50, 50):
    for y in range (-50, 50):
        t.goto(x * s, y * s)
        t.dot(2, "purple")
t.update()
t.done()"""
# Домашка №6 шаг 8 https://stepik.org/lesson/1038843/step/8?unit=1062794
"""#Повтори 2 [Вперёд 8 Направо 90 Вперёд 18 Направо 90]
#Поднять хвост
#Вперёд 4 Направо 90 Вперёд 10 Налево 90
#Опустить хвост
#Повтори 2 [Вперёд 17 Направо 90 Вперёд 7 Направо 90]
#включая точки на линиях.
import turtle as t
t.screensize(5000, 5000)
t.tracer(0)
t.left(90)
s = 20
for i in range(2):
    t.forward(8 *s)
    t.right(90)
    t.fd(18 * s)
    t.right(90)
t.up()
t.fd(4 * s)
t.right(90)
t.fd(10 * s)
t.right(90)
t.down()
for i in range(2):
    t.color('red')
    t.forward(17 *s)
    t.right(90)
    t.fd(7 * s)
    t.right(90)
t.up()
for x in range(-50, 50):
    for y in range(-50, 50):
        t.goto(x * s, y * s)
        t.dot(2, "purple")
t.update()
t.done()"""
# Домашка №6 шаг 9 https://stepik.org/lesson/1038843/step/9?unit=1062794
"""import turtle as t
t.screensize(5000, 5000)
t.tracer(0)
t.left(90)
s = 20
for i in range (3):
    t.fd (10 * s)
    t.rt(120)
t.up ()
t.fd (10 * s)
t.rt(90)
t.fd (3 * s)
t.down()
for i in range (4):
    t.fd(10 * s)
    t.rt(90)
t.up()
for x in range(-50, 50):
    for y in range(-50, 50):
        t.goto (x * s, y * s)
        t.dot(2, "purple")
t.update()
t.done()"""
# Домашка №6 шаг 10 https://stepik.org/lesson/1038843/step/10?unit=1062794
"""import turtle as t
t.screensize(5000, 5000)
t.tracer(0)
t.left(90)
s = 20
for i in range (3):
    t.fd(7 * s)
    t.rt(90)
    t.fd(12 * s)
    t.rt(90)
t.up
t.fd(4 * s)
t.rt(90)
t.fd (6 * s)
t.lt(90)
t.down()
for i in range (4):
    t.fd(83 * s)
    t.rt(90)
    t.fd(77 * s)
    t.rt(90)
t.up()
for x in range (-100, 100):
    for y in range (-100, 100):
        t.goto(x * s, y * s)
        t.dot (2, "purple")
t.update()
t.done()"""
# Домашка №6 шаг 12 https://stepik.org/lesson/1038843/step/12?unit=1062794
"""#Направо 315
# Повтори 7 [Вперёд 12 Направо 45 Вперёд 6 Направо 135]
import turtle as t
t.screensize(5000, 5000)
t.tracer(0)
t.left(90)
s = 20
t.rt(315)
for i in range (7):
    t.fd(12 * s)
    t.rt(45)
    t.fd(6 * s)
    t.rt(135)
t.up()
for x in range (-100, 100):
    for y in range (-100, 100):
        t.goto (x * s, y * s)
        t.dot(2, "purple")
t.update()
t.done()"""
# Домашка №6 шаг 13 https://stepik.org/lesson/1038843/step/13?unit=1062794
"""#Повтори 4 [Вперёд 12 Направо 90]
# Направо 30
# Повтори 3 [Вперёд 8 Направо 60 Вперёд 8 Направо 120]
import turtle as t
t.screensize(5000,5000)
t.tracer(0)
t.left(90)
s = 20
for i in range (4):
    t.fd (12 * s)
    t.rt(90)
t.rt(30)
for i in range (3):
    t.fd(8 * s)
    t.rt(60)
    t.fd(8 * s)
    t.rt(120)
t.up()
for x in range (-50,50):
    for y in range (-50,50):
        t.goto(x * s, y * s)
        t.dot (2, "purple")
t.update()
t.done()"""
# Домашка №6 шаг 14 https://stepik.org/lesson/1038843/step/14?unit=1062794
#Повтори 2 [Вперёд 13 Направо 90 Вперёд 20 Направо 90]
#Поднять хвост
#Вперёд 8 Направо 90 Назад 3 Налево 90
#Опустить хвост
#Повтори 2 [Вперёд 16 Направо 90 Вперёд 8 Направо 90]
#Определите, сколько точек с целочисленными координатами будут находиться внутри объединения фигур, ограниченного
#заданными алгоритмом линиями, включая точки на линиях.
#Ответ 411
import turtle as t
t.screensize(5000,5000)
t.tracer(0)
t.left(90)
s = 20
for i in range (2):
    t.fd(13 * s)
    t.rt(90)
    t.fd(20 * s)
    t.rt(90)
t.up()
t.fd(8 * s)
t.rt(90)
t.backward(3)
t.left(90)
t.down()
for i in range (2):
    t.fd(16 * s)
    t.rt(90)
    t.fd(8 * s)
    t.rt(90)
t.up()
for x in range(-50, 50):
    for y in range(-50 ,50):
        t.goto(x * s, y * s)
        t.dot (2, "purple")
t.update()
t.done()
# Домашка №6 шаг 15 https://stepik.org/lesson/1038843/step/15?unit=1062794
"""import turtle as t
t.screensize(5000,5000)
t.tracer(0)
t.left(90)
s = 20
for i in range (9):
    t.fd (22 * s)
    t.rt(90)
    t.fd (6 * s)
    t.rt(90)
t.up()
t.fd(1 * s)
t.rt(90)
t.fd(5 * s)
t.left(90)
t.down()
for i in range(2):
    t.fd(17 * s)
    t.rt(90)
    t.fd(7 * s)
    t.rt(90)"""




#Обяснение

# № 23743 Демоверсия 2026 (Уровень: Базовый)

# В начальный момент Черепаха находится в начале координат,
# её голова направлена вдоль положительного направления оси ординат,
# хвост опущен.

# Черепахе был дан для исполнения следующий алгоритм.
# Повтори 2 [Вперёд 14 Налево 270 Назад 12 Направо 90]
# Поднять хвост
# Вперёд 9 Направо 90 Назад 7 Налево 90
# Опустить хвост
# Повтори 2 [Вперёд 13 Направо 90 Вперёд 6 Направо 90]

"""import turtle as t  # Подключение библиотеки с коротким именем t
t.screensize(5000, 5000)  # Для ползунков по холсту
t.tracer(0)  # Отключает анимацию отрисовки / мгновенная отрисовка
t.left(90)  # Необходимо сделать по условию, чтобы черепаха смотрела "вверх"
s = 30  # Переменная ответственная за масштаб фигур

# Повтори 2 [Вперёд 14 Налево 270 Назад 12 Направо 90]
for i in range(2):
    t.forward(14 * s)
    t.left(270)
    t.backward(12 * s)
    t.right(90)

t.up()  #  Поднять хвост

# Вперёд 9 Направо 90 Назад 7 Налево 90
t.fd(9 * s)
t.rt(90)
t.bk(7 * s)
t.lt(90)

t.down()  # Опустить хвост

t.color('blue')  # меняем цвет второй фигуры

# Повтори 2 [Вперёд 13 Направо 90 Вперёд 6 Направо 90]
for i in range(2):
    t.forward(13 * s)
    t.right(90)
    t.forward(6 * s)
    t.right(90)

# Тут отрисовываем точки:
t.up()
for x in range(-50, 50):  # Перебираем координаты точек
    for y in range(-50, 50):
        t.goto(x * s, y * s)  # Прыгаем в конкретную координату
        t.dot(3, 'red')  # Рисуем точку красного цвета и толщиной 3

t.update()  # Для корректной работы t.tracer()
t.done()  # Для того, чтобы зафиксировать окно отрисовки
"""



'''
Запустите бота: https://t.me/ilandroxxy_bot и нажмите кнопку: "📚 Получить конспект"
'''
# endregion Место для вашего конспекта ⬆️

# endregion Домашка: ******************************************************************
# #
# #
# region Урок: ********************************************************************
"""

"""
# Домашка 6 номер: https://stepik.org/lesson/1038843/step/1?unit=1062794

# Практика 6 номер: https://stepik.org/lesson/1157714/step/1?unit=1169951
