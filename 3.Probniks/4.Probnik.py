#Задание 1
"""print("1 2 3 4 5 6 7 8")
from itertools import permutations
table = '15 18 23 25 27 32 35 46 47 51 52 53 64 68 72 74 78 81 86 87'
graph = 'АБ БА АВ ВА КА АК БД ДБ ГД ДГ ЕД ДЕ ЕГ ГЕ ГВ ВГ ВЖ ЖВ ЖК КЖ'
for p in permutations('АБВГДЕЖК'):
    new_table = table
    for i in range(1, 8 + 1):
        new_table = new_table.replace(str(i), p[i - 1])
    if set(new_table.split()) == set(graph.split()):
        print(p)"""
"""Ответ: 18"""

#Задание 2
"""print ("x y z w")
for x in range(2):
    for y in range (2):
        for z in range (2):
            for  w in range (2):
                F = (y <= x) and w and (not (z))
                if F == 1:
                    print (x , y , z , w, F)"""
"""Ответ wxyz"""

#Задание 3
"""Ответ: 1164"""

#Задание 4
"""Ответ: 16"""

#Задание 5
"""alp = sorted("1234567890QWERTYUIOPASDFGHJKLZXCVBNM")
def convert(n, b):
    r = ""
    while n > 0:
        r += alp[n % b]
        n //= b
    return r[::-1]

for n in range(1, 10000):
    n2 = convert(n, 2)
    if n % 3 == 0:
        n2 = n2 + n2[-3:]
    else:
        a = n % 3
        a = a * 3
        a = convert(a, 10)
        n2 = n2 + a
    r = int(n2, 10)
    if 74 < r < 76:
        print(r)"""

"""Ответ 11"""

#Задание 6
"""import turtle as t
t.screensize(5000, 5000)
t.tracer(0)
t.left(90)

s = 30
for i in range(4):
    t.forward(20 * s)
    t.right(270)
t.up ()
t.forward(6 * s)
t.right(270)
t.forward(10 * s)
t.right(90)
t.down ()
for i in range(2):
    t.forward(20 * s)
    t.right(270)
    t.forward(24 * s)
    t.right(270)
t.up ()
for x in range(-50, 50):
    for y in range(-50, 50):
        t.goto(x * s, y * s)
        t.dot(2,'red')
t.update()
t.done()"""

"""Ответ 801"""

#Задание 7
"""Ответ: 10"""

#Задание 8
"""-"""

#Задание 9
"""cnt = 0
for s in open('9_1865.csv'):
    M = [int(x) for x in s.split(';')]
    copied1 = [x for x in M if M.count(x) == 1]
    copied2 = [x for x in M if M.count(x) == 2]
    if len(copied1) == 4 and len(copied2) == 2:
        if copied2[0] < (sum(copied1)/len(copied1)):
            cnt += 1
print(cnt)"""

#Задание 10
"""Ответ: 10"""

#Задание 11
"""Ответ 12 байт"""

#Задание 12
'''print(bin(400)[2:])
print(int('1101111',2))'''

"""Ответ 111"""

#Задание 13
"""from ipaddress import *
for mask in range(1,33):
    net = ip_network(f'195.23.86.50/{mask}',0)
    if '195.23.80.0' in str(net):
        print(net, net.netmask)"""
"""Ответ 2"""

#Задание 14
"""alp = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
for x in alp[:22]:
    A = int(f'63{x}59685', 22)
    B = int(f'17{x}53', 22)
    C = int(f'36{x}5', 22)
    if (A + B + C) % 21 == 0:
        print(min(x))
A = int(f'63{4}59685', 22)
B = int(f'17{4}53', 22)
C = int(f'36{4}5', 22)
print ((A + B + C) // 21)"""

"""Ответ: 729929407"""

#Задание 15
"""-"""

#Задание 16
"""import sys
sys.setrecursionlimit(10**8)
def F(n):
    if n == 1:
        return 1
    if n > 1:
        return n * F(n - 1)
print (F(2028) - F(2024))"""
"""Ответ - """
#Задание 17

#Задание 18
"""Ответ: 2407 1101"""

#Задание 19-21
"""def F(s, n):
    if s >= 184:
        return n % 2 == 0
    if n == 0:
        return 0
    h = [F(s + 1, n-1), F(s + 5, n-1), F(s * 4, n-1)]
    return any(h) if (n - 1) % 2 == 0 else all(h)  # else any(h)

print([s for s in range(1, 183+1) if F(s, n=2)])
print([s for s in range(1, 183+1) if F(s, n=3) and not F(s, n=1)])
print([s for s in range(1, 183+1) if F(s, n=4) and not F(s, n=2)])"""
#Ответ:
#[45]
#[40, 44]
#[39, 43]

#Задание 25
'''from fnmatch import *
for x in range(0, 10**8,6072):
    if fnmatch(str(x), '5*4?48'):
        print(x,x//6072)'''
#54648 9
#5064048 834
#5974848 984
#50604048 8334
#51514848 8484
#53184648 8759
#54854448 9034
#56524248 9309
#58194048 9584
#59104848 9734