#Номер 13
'''
# Номер 13 https://education.yandex.ru/ege/task/b6ff76ad-5608-4e7d-833d-dced5a6e2479
from ipaddress import *
for mask in range(1, 32+1):
    net = ip_network(f"111.81.27.208/{mask}", 0)
    print (net, net.netmask)
# Ответ-192,  111.81.27.192
'''
#13 задание Школа
"""
'''from ipaddress import *
cnt = 0
net = ip_network('192.168.32.176/255.255.255.240', 0)
for ip in net:
    if f'{ip:b}'.count('1') % 2 != 0:
        cnt += 1
print(cnt)'''#Answer: 8

'''from ipaddress import *
R = []
net = ip_network('191.128.66.83/255.192.0.0', 0)
print(net[-2])'''#Answer: 191.191.255.254

'''from ipaddress import *
cnt = 0
net = ip_network('252.67.33.87/255.248.0.0', 0)
for ip in net:
    if f'{ip:b}'[16:].count('1') / f'{ip:b}'[:16].count('1') > 2:
        cnt += 1
print(cnt)'''#Answer: 17
'''from ipaddress import *
net = ip_network('45.172.106.203/255.255.252.0', 0)
print(net[-2])'''#Answer: 45.172.107.254
'''from ipaddress import *
cnt = 0
net = ip_network('172.16.192.0/255.255.192.0', 0)
for ip in net:
    if f'{ip:b}'.count('1') % 5 != 0:
        cnt += 1
print(cnt)'''#Answer: 13003
'''from ipaddress import *
cnt = 0
net = ip_network('192.168.160.0/255.255.224.0', 0)
for ip in net:
    if f'{ip:b}'.count('1')==19:
        cnt+=1
print(cnt)'''#Answer: 13
'''from ipaddress import *
cnt = 0
net = ip_network('123.222.0.192/255.255.255.224', 0)
for ip in net:
    if f'{ip:b}'.count('0') == f'{ip:b}'.count('1'):
        cnt += 1
print(cnt)'''#Answer: 10
'''from ipaddress import *
cnt = 0
net = ip_network('123.222.111.192/255.255.255.192', 0)
for ip in net:
    if f'{ip:b}'[24:].count('1') % 3 != 0:
        cnt += 1
print(cnt)'''#Answer: 43
"""

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
#   Поднять хвост
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

#Домашка по срезам
#3.5 Домашка: Строки str(). https://stepik.org/lesson/1309454/step/1?unit=1324570
#Номер 5
"""#abcdefghijklmnop
a = input()
for x in a [0::2]:
    print (x)"""
#Номер 6
"""z = 0
a = input()
for x in a [0::1]:
    z += int(x)
print(z)"""
#Номер 7
"""a = input()
R = 0
V = 0
for x in a:
    if x == "+" :
        R += 1
    else :
        R += 0
    if x == "*" :
        V += 1
print ("Символ + встречается",R,"раз")
print ("Символ * встречается",V,"раз")"""
#Номер 8
"""# https://stepik.org/lesson/1309454/step/8?unit=1324570
#общее количество символов в строке;
#исходную строку, повторенную 3 раза;
#первый символ строки;
#первые три символа строки;
#последние три символа строки;
#строку в обратном порядке;
#строку с удаленным первым и последним символом.
a = input()
b = ""
summ = 0
len (a)
print (len(a))
c = a * 3
print (c)
print (a[0])
print (a[0:3])
print (a[-3:])
c = a[::-1]
print (c)
print (a[1:-1])
# Вводные (abcdefghijklmnopqrstuvwxyz)
# Ответ
#26
#abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz
#a
#abc
#xyz
#zyxwvutsrqponmlkjihgfedcba
#bcdefghijklmnopqrstuvwxy"""
#Номер 10
"""#третий символ этой строки;
#предпоследний символ этой строки;
#первые пять символов этой строки;
#всю строку, кроме последних двух символов;
#все символы с четными индексами;
#все символы с нечетными индексами;
#все символы в обратном порядке;
#все символы строки через один в обратном порядке, начиная с последнего

a = input()
v = ""
print (a[2])
print (a[-2])
print (a[0:5])
print (a[0:-2])
print (a[0::2])
print (a[1::2])
c = a [::-1]
print (c)
for i in range(len(a) - 1, -1, -2):
    v += a[i]
print(v)
#Вводные (abcdefghijklmnopqrstuvwxyz)
# Вывод 
#c
#y
#abcde
#abcdefghijklmnopqrstuvwx
#acegikmoqsuwy
#bdfhjlnprtvxz
#zyxwvutsrqponmlkjihgfedcba
#zxvtrpnljhfdb"""

# Функция convert
"""
alp = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
def convert(n, b):
    r = ''
    while n > 0:
        r += alp[n % b]
        n //= b
    return r[::-1]
n = 10**9
print(convert(n, 2))  # 111011100110101100101000000000
print(int('111011100110101100101000000000', 2))  # 10**9

print(convert(n, 8))  # 7346545000
print(int('7346545000', 8))  # 10**9

print(convert(n, 16))  # 3B9ACA00
print(int('3B9ACA00', 16))  # 10**9

print(convert(n, 3))  # 2120200200021010001
print(int('2120200200021010001', 3)) # 10**9 
"""

#КЕГЭ № 8506 Апробация 17.05 (Уровень: Базовый)
"""
def F(s, n):
    if s >= 55 :
        return n % 2 == 0
    if n == 0:
        return 0
    h = [F(s + 1 , n-1), F(s +4, n-1), F(s * 3, n-1)]
    return any(h) if (n - 1) % 2 == 0 else all(h)  # else any(h)

print([s for s in range(1, 66 +1) if F(s, n=2)])
print([s for s in range(1, 66 +1) if F(s, n=3) and not F(s, n=1)])
print([s for s in range(1, 66 +1) if F(s, n=4) and not F(s, n=2)])
"""



#КЕГЭ № 17638 Основная волна 19.06.24 (Уровень: Базовый)
"""
def F(s, n):
    if s >= 39 :
        return n % 2 == 0
    if n == 0:
        return 0
    h = [F(s + 1, n-1), F(s + 3, n-1), F(s * 2, n-1)]
    return any(h) if (n - 1) % 2 == 0 else all(h)  # else any(h)

print([s for s in range(1, 39 +1) if F(s, n=2)])
print([s for s in range(1, 39 +1) if F(s, n=3) and not F(s, n=1)])
print([s for s in range(1, 39 +1) if F(s, n=4) and not F(s, n=2)])"""

#КЕГЭ № 8594 (Уровень: Базовый)
#https://stepik.org/lesson/1038794/step/4?unit=1062789
def F(a, s, n):
    if a * s >= 455 : #+-*/ Смотреть по условию
        return n % 2 == 0
    if n == 0:
        return 0
    h = [F(a + 1, s , n-1), F(a, s + 1, n-1), F(a * 2, s , n-1), F(a, s * 2, n-1)]
    return any(h) if (n - 1) % 2 == 0 else all(h)  # else any(h)

print([s for s in range(1, 90+1) if F(5, s, n=2)])
print([s for s in range(1, 90+1) if F(5, s, n=3) and not F(5, s, n=1)])
print([s for s in range(1, 90+1) if F(5, s, n=4) and not F(5, s, n=2)])

