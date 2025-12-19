# Этот файл подготовлен для прорешивания задач из курса:
# Основы Python для успешной сдачи ЕГЭ по Информатике 2025 | itpy
# https://stepik.org/course/203477/promo
#ФИПИ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19-21, 22, 23, 25]
'''#1 Перевод по системам счисления
def convert(n, b):
    alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
    result = ''
    while n > 0:
        result += alphabet[n % b]
        n //= b
    return result[::-1]
#Системы счисления'''
'''def divisors(x):
    div = []
    for j in range(2, int(x**0.5)+1):  # не считая единицы и самого числа.
        if x % j == 0:
            div.append(j)
            div.append(x//j)
    return sorted(set(div))#Делители'''
'''#2 Проверка пароля
from random import randint, choice
from time import sleep
messages_error = [
    "Неправильный пароль, попробуйте снова: ",
    "Пароль введен неверно, повторите попытку: ",
    "Ошибка пароля, введите заново: ",
    "Пароль не подходит, попробуйте ещё раз: ",
    "Некорректный пароль, повторите ввод: ",
    "Пароль неверен, введите снова: ",
    "Пароль ошибочный, повторите попытку: ",
    "Введен неверный пароль, попробуйте ещё раз: ",
    "Пароль не распознан, введите заново: ",
    "Неправильный пароль, введите ещё раз: "
]
user = 'Женя'
password = 'qwerty'
pas = input('Введите пароль: ')
cnt = 0
while True:
    if pas == password:
        print('Пароль верный!', end=' ')
        break
    else:
        cnt += 1
        if cnt == 3:
            print('Пройдите проверку на робота решив пример.')
            a = randint(0, 100)
            b = randint(0, 100)
            x = int(input(f'{a} + {b} = '))
            if x == a + b:
                print('Проверка пройдена успешно.')
                cnt = 0
            else:
                print('Проверка не пройдена \n'
                      'Повторите попытку через 5 минут.')
                sleep(5 * 60)
        pas = input(choice(messages_error))
print(f'Добро пожаловать, {user}.')'''
# Номер 13
'''from ipaddress import *
R=[]
for mask in range(32+1):
    net = ip_network(f'163.232.136.60/{mask}', 0) #Находим адрес сети/кол-во единиц в маске
    if str(net) == f'163.232.136.0/{mask}': #Сравнием данный адрес сети с получившимся
        R.append(mask)
print(max(R))#маски'''
'''from ipaddress import *
cnt = 0
net = ip_network('136.36.240.16/255.255.255.248', 0)
for ip in net:
    b=bin(int(ip))[2:]
    if '101' not in str(b):
        cnt+=1
print(cnt)'''
#№15
'''#№15, 18595 (Уровень: Базовый)
def F(x, A1, A2):
    C = 48 <= x <= 94
    J = 83 <= x <= 100
    A = A1 <= x <= A2
    return (not(C or J)) <= (not A)


R = []
M = [x / 5 for x in range(35 * 5, 110 * 5)]
for A1 in M:
    for A2 in M:
        if all(F(x, A1, A2) for x in M):
            R.append(A2 - A1)
print(max(R)) #52.0 -> 52
#Ответ: 52'''
"""def F(x, A):
    return ((x & 52 != 0) and (x & 36 == 0)) <= (x & A != 0)
R = []
for A in range(1000):
    if all(F(x, A) == 1 for x in range(1000)):
        print(A)
        break"""
#КЕГЭ № 2356 (Уровень: Базовый)
"""def F(a1, a2, x):
    P = 10 <= x <= 45
    Q = 35 <= x <= 78
    A = a1 <= x <= a2
    return ((not P) <= Q) and (not A)


R = []
M = [x / 5 for x in range(1*5, 90*5)]
for a1 in M:
    for a2 in M:
        if all(F(a1, a2, x) == 0 for x in M):
            R.append(a2 - a1)
print(int(min(R)))"""
#КЕГЭ № 6750 Апробация 10.03.23 (Уровень: Базовый)
"""def F(x, y, A):
    return (x + y <= 32) or (y <= x + 4) or (y >= A)


R = []
for A in range(10000):
    if all(F(x, y, A) == 1 for x in range(100) for y in range(100)):
        R.append(A)
print(max(R))"""
#КЕГЭ № 17556 Основная волна 08.06.24 (Уровень: Базовый)
"""def F(A, x):
    B = 70 <= x <= 90
    return (x % A == 0) or (B <= (x % 22 != 0))


R = []
for A in range(1, 1000):
    if all(F(A, x) == 1 for x in range(1000)):
        R.append(A)
print(max(R))"""
#21.02.2025 16 номера
"""from functools import *#библиотека, чтобы использовать кеширование
import sys#библиотека, чтобы обойти максимальный барьер рекурсии
sys.setrecursionlimit(10000)#обход барьера рекурсии


@lru_cache()#вызывает значения из кэша, если видит знакомые значения F(n)
def F(n):
    if n <= 3:
        return n - 1
    if n > 3 and n % 2 == 0:
        return F(n - 2) + n/2 - F(n - 4)
    if n > 3 and n % 2 != 0:
        return F(n - 1) * n + F(n - 2)
for n in range(5000):#пробегаем функцию F(n) 5000 раз, чтобы положить ее значения в кэш
    F(n)
print(F(4952) + 2 * F(4958) + F(4964))"""
#№ 12248 ЕГКР 16.12.23 (Уровень: Базовый)
"""import sys
sys.setrecursionlimit(10000)
def F(n):
    if n<=3:
        return 1
    if n>3:
        return((n+3) * F(n-2))
print(F(2028)//F(2024))"""#Answer: 4120899
#№ 8953 Джобс 02.06.2023 (Уровень: Базовый)
"""import sys
sys.setrecursionlimit(10001)
def F(n):
    if n >=10000:
        return 1
    if n<10000 and n%2==0:
        return((F(n+3)+7))
    if n<10000 and n%2!=0:
        return((F(n+1)-3))
print(F(50)-F(57))"""#Answer: 11
#28.02.2025, номер 23
'''#1 https://education.yandex.ru/ege/task/1e0cb6b4-4bc0-4443-bd23-71dbb3d80d36
def F(a, b) :
    if a>=b or a==15:
        return a==b
    return F(a+1, b) + F(a*2, b) + F(a*3, b)
print(F(1, 11)*F(11,25))'''
#Homework: ex. 16 and ex.23 отрешать
#1.03.2025
#ex. 16:
#1 https://education.yandex.ru/ege/task/0d598bd3-2086-4746-b936-23280495eb32
'''def F(n):
    if n==0:
        return 1
    if n==1:
        return 3
    if n>1:
        return F(n-1) - F(n-2) +3*n
print(F(40)) #Answer: 126'''
#2 https://education.yandex.ru/ege/task/c230a1bb-96d8-43f4-b65a-3cb093eb1031
'''import sys
from functools import *
sys.setrecursionlimit(1000000)
@lru_cache(None)
def F(n):
    if n < 3:
        return 1
    if n > 2 and n % 2 == 0:
        return F(n - 1) * (n - 1)
    if n > 2 and n % 2 != 0:
        return F(n - 2) * (2 * n - 2)
for n in range(15000):
    F(n)
print(int((F(10048) - F(10045)) / F(10043))) #Answer: 4055050520424'''
#ex. 23:
#1 https://education.yandex.ru/ege/task/a21521c7-2b20-4e05-acde-e6fb294c94f8
'''def F(a, b):
    if a>=b or a==10:
        return a==b
    return F(a+1, b) + F(a*2, b)
print(F(1, 30))#Answer: 68'''
#2 https://education.yandex.ru/ege/task/c0707fa0-019f-4c29-815b-16b1d678b30e
'''def F(a, b):
    if a>=b or a==16:
        return a==b
    return F(a+2, b) + F(a+3, b) + F(a**2, b)
print(F(2, 25)*F(25, 42))#Answer: 12348'''
#7.03.2025
# №17:
'''# № 17636 Основная волна 19.06.24 (Уровень: Средний)
M = [int(x) for x in open('0. files/17.txt')]
A = [x for x in M if abs(x) % 10 == 3 and len(str(abs(x))) == 3]
R = []  # сюда будем складывать результаты
for i in range(len(M)-2):
    x, y, z = M[i], M[i+1], M[i+2]
    if (x in A) + (y in A) + (z in A) >= 1:
        if (x + y + z) < max(A):
            R.append(x + y + z)
print(len(R), max(R))'''
'''# № 17680 Пересдача 04.07.24 (Уровень: Базовый)
M = [int(x) for x in open('0. files/17.txt')]
A = [x for x in M if x > 0 and x % 41 == 0]
R = []
for i in range(len(M)-1):
    x, y= M[i], M[i+1]
    if x != y:
        if abs(x - y) % min(A) == 0:
            R.append(x + y)
print(len(R), max(R))'''
'''#https://education.yandex.ru/ege/task/75f1504f-3de9-4807-94ca-b08cea796a26
M = [int(x) for x in open('tasks/files/17.txt')]
R=[]
cnt=0
for i in range(len(M)-1):
    x, y = M[i], M[i+1]
    if x%3==0 or y%3==0:
        cnt+=1
        R.append(x+y)
print(cnt, max(R))#Answer:2802 1990'''
'''#https://education.yandex.ru/ege/task/5e46684b-8408-47c0-92e8-9065796469f1
M = [int(x) for x in open('tasks/files/17 (1).txt')]
A = [int(x) for x in M if len(str(x))==3 and x%10==5]
R=[]
cnt=0
for i in range(len(M)-1):
    x, y = M[i], M[i+1]
    if len(str(x))==3 or len(str(y))==3:
        if (x+y)%min(A)==0:
            cnt+=1
            R.append(x+y)
print(cnt, max(R))#Answer: 13 9500'''
'''#https://education.yandex.ru/ege/task/0091460b-16e1-429a-b515-24c27670d1e3
M = [int(x) for x in open('tasks/files/17 (2).txt')]
A = [int(x) for x in M if x%17==0]
R= []
cnt=0
for i in range(len(M)-1):
    x, y = M[i], M[i+1]
    if (x+y)>max(A):
        cnt+=1
        R.append(x+y)
print(cnt, max(R))#Answer: 5104 19930'''
'''#https://education.yandex.ru/ege/task/1c1fd299-2d3b-46e0-835d-a8416ecc37c8

M = [int(x) for x in open('tasks/files/17 (3).txt')]
A = [int(x) for x in M if len(str(abs(x)))==3 and abs(x)%10==8]
B = min(A)**2
R = []
cnt=0
for i in range(len(M)-2):
    x, y, z = M[i], M[i+1], M[i+2]
    if (x**2>B and y**2>B and z**2<=B) or (x**2>B and z**2>B and y**2<=B) or (y**2>B and z**2>B and x**2<=B):
        if len(str(abs(x))) == 3 or len(str(abs(y))) == 3 or len(str(abs(z))) == 3:
            cnt+=1
            R.append(x+y+z)
print(cnt, max(R))#Answer: 5312 20235'''
# №9:
'''#https://education.yandex.ru/ege/task/dcf64491-b2a9-43d3-8307-3d9aad5e7fe4
cnt=0
for s in open('tasks/files/9.txt'):
    M=[int(x) for x in s.split()]
    uncopied = [x for x in M if M.count(x) == 1]
    if len(uncopied) == len(M):
        chet = [x for x in M if x%2==0]
        nechet = [x for x in M if x%2!=0]
        if len(chet)>len(nechet):
            cnt+=1
print(cnt)'''
'''#https://education.yandex.ru/ege/task/d267e965-9720-4a8d-9578-674855b1bde7
cnt=0
for s in open('tasks/files/9 (1).txt'):
    M = [int(x) for x in s.split()]
    if sum(M)>100:
        cnt+=1
print(cnt)#Answer:2499'''
'''#https://education.yandex.ru/ege/task/7102b1d9-1aed-45d5-bb07-8fb3361ed445
n=0
for s in open('tasks/files/9 (1).csv'):
    M = sorted([int(x) for x in s.split(';')])
    copied = [x for x in M if M.count(x)==2]
    uncopied = [x for x in M if M.count(x)==1]
    if len(copied)==2 and len(uncopied) == 3:
        if ((M[0] + M[-1])**2) < (M[1]**2 + M[2]**2 + M[3]**2):
            n+=1
print(n)#Answer: 691'''
# №15:
'''#https://education.yandex.ru/ege/task/5ca88e8c-e0a3-4d20-aa86-d2fd4f4d3427
cnt=0
A = {24, 33, 41, 15, 18}
B = {3, 35, 41, 18, 9}
for x in range(0, 100):
    if not((x not in A) and (x not in B)):#((x in A) or (x in B))
        cnt+=1
print(cnt)#Answer: 8'''
'''#https://education.yandex.ru/ege/task/7e59bed3-2ef7-4f3c-989d-90518e9dde1d'''
'''#https://education.yandex.ru/ege/task/a63e2b19-84a3-44ac-aa0e-01fea94ebb05
def F(x, y, A):
    return (2*y>5*x) or (x*y<A) or (x>=22)
for A in range(1, 10000):
    if all(F(x, y, A)==1 for x in range(1, 100) for y in range(1, 100)):
        print(A)
        break#Answer: 1093'''
# №1:
'''from itertools import *
print('1 2 3 4 5 6 7 8 9')
table = '14 15 24 28 29 34 35 41 42 43 47 49 51 53 56 65 74 78 82 87 92 94'
graph = 'AK KA KB BK KC CK CD DC BD DB DE ED DG GD DH HD HG GH GF FG FE EF'
for p in permutations('ABCDEFGHK'):
    new_table = table
    for i in range(1, 9+1):
        new_table = new_table.replace(str(i), p[i-1])
    if set(graph.split()) == set(new_table.split()):
        print(*p)'''
'''#КЕГЭ № 6876 OpenFIPI (Уровень: Базовый)
from itertools import *
print('1 2 3 4 5 6 7 8')
table = '13 15 23 25 26 31 32 37 38 45 48 51 52 54 56 57 58 62 65 73 75 78 83 84 85 87'
graph = 'АГ ГА АЗ ЗА ЗЖ ЖЗ ЗВ ВЗ ЗБ БЗ ЖГ ГЖ ЖВ ВЖ ВД ДВ ДГ ГД ГЕ ЕГ ЕБ БЕ ВГ ГВ БГ ГБ'
for p in permutations('АБВГДЕЖЗ'):
    new_table=table
    for i in range(1, 8+1):
        new_table=new_table.replace(str(i), p[i-1])
    if set(graph.split()) == set(new_table.split()):
        print(*p)'''
'''#КЕГЭ № 1417 (Уровень: Базовый)
from itertools import *
print('1 2 3 4 5 6')
table = '12 13 15 16 21 25 31 34 35 36 43 46 51 52 53 61 63 64'
graph = 'АВ ВА ВГ ГВ ГА АГ ГБ БГ ГД ДГ ДЕ ЕД ДБ БД ЕБ БЕ АБ БА'
for p in permutations('АБВГДЕ'):
    new_table=table
    for i in range(1, 6+1):
        new_table = new_table.replace(str(i), p[i-1])
        if set(graph.split()) == set(new_table.split()):
            print(*p)#Answer: 56(5 и 6)'''
'''#КЕГЭ № 3638 (Уровень: Средний)
from itertools import permutations
print('1 2 3 4 5 6 7')
graph = 'АБ БА АВ ВА БВ ВБ ВД ДВ ВГ ГВ ВЕ ЕВ ДЕ ЕД ЕГ ГЕ ГК КГ ЕК КЕ'
table = '12 14 21 24 26 35 36 41 42 46 47 53 56 62 63 64 65 67 74 76'
for p in permutations('АБВГДЕК'):
    new_table = table
    for i in range(1, 7+1):
        new_table = new_table.replace(str(i), p[i-1])
        if set(graph.split()) == set(new_table.split()):
            print(*p)#Answer: 45'''
'''#КЕГЭ № 17620 Основная волна 19.06.24 (Уровень: Базовый)
from itertools import permutations
print('1 2 3 4 5 6 7')

graph = 'AF FA AB BA BF FB FE EF BD DB DE ED EC CE CG GC GD DG'
table = '12 15 16 21 23 24 32 36 37 42 47 51 56 61 63 65 73 74'
for p in permutations('ABCDEFG'):
    new_table = table
    for i in range(1, 7+1):
        new_table = new_table.replace(str(i), p[i-1])
        if set(graph.split()) == set(new_table.split()):
            print(*p)#Answer: 55'''
# №19-21:
#№ 19635 (Уровень: Базовый)
'''
from math import ceil, floor
def F(a, s, n):
    if a + s <= 100:
        return n % 2 == 0
    if n == 0:
        return 0
    h = [F(a-3, s-3, n-1), F(floor(a/2), s, n-1), F(a, floor(s/2), n-1)]
    return any(h) if (n-1) % 2 == 0 else all(h) #else any(h)
print([s for s in range(53, 1000) if F(48, s, 2)])
print([s for s in range(53, 1000) if F(48, s, 3) and not F(48, s, 1)])
print([s for s in range(53, 1000) if F(48, s, 4) and not F(48, s, 2)])
#Answer:
#19: 59
#20: 115, 229
#21: 124
'''
#КЕГЭ № 8506 Апробация 17.05 (Уровень: Базовый)
'''def F(s, n):
    if s >= 55:
        return n % 2 == 0
    if n == 0:
        return 0
    h = [F(s+1, n-1), F(s+4, n-1), F(s*3, n-1)]
    return any(h) if (n-1) % 2 == 0 else all(h) #else any(h)
print([s for s in range(1, 55) if F(s, 2)])
print([s for s in range(1, 55) if F(s, 3) and not F(s, 1)])
print([s for s in range(1, 55) if F(s, 4) and not F(s, 2)])'''
#23.05.2025
#23
'''def F(a, b):
    if a > b or a == 8:
        return 0
    elif a == b:
        return 1
    else:
        return F(a + 1, b) + F(a + 2, b) + F(a * 2, b)
print(F(3, 14) * F(14, 18))#360'''
#5
'''R = []
for N in range(1, 1000):
    N2 = bin(N)[2:]
    s = [int(x) for x in str(N2)]
    s1 = sum(s) % 2
    N3 = str(N2) + str(s1)
    s2 = [int(x) for x in N3]
    s3 = sum(s2) % 2
    N4 = N3 + str(s3)
    r = int(N4, 2)
    if r > 253:
        R.append(N)
print(min(R))#64'''
#14.1
'''alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
for x in alphabet[:21]:
    A = int(f'82934{x}2', 21)
    B = int(f'2924{x}{x}7', 21)
    C = int(f'67564{x}8', 21)
    if ((A + B + C) % 20) == 0:
        print((A+B+C)//20)
        break#72450445'''
#14.2
"""R = []
def convert(a, b):
    alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
    r = ''
    while a > 0:
        r += alphabet[a%b]
        a//=b
    return r[::-1]
for x in range(1, 2301):
    A = 7**350
    B = 7**150
    C = x
    if str(convert((A + B - C), 7)).count('0') == 200:
        R.append(x)
print(max(R))"""
#15
'''def F(x):
    B = 36 <= x <= 75
    C = 60 <= x <= 110
    A = a1 <= x<= a2
    return ((not(A)) <= (B == C))
M = [i for i in range(1, 111)]
R = []
for a1 in M:
    for a2 in M:
        if all(F(x) for x in M):
            R.append(a2 - a1)
print(min(R))#74'''
#11
'''from math import ceil
sym = 119
cnt = 125300
all_inf_byte = 23 * 2**20
inf_for_one_byte = ceil(all_inf_byte / cnt)
inf_for_one_bit = inf_for_one_byte * 2**3
i = ceil(inf_for_one_bit / sym)
alp = (2 ** (i-1))+1
print(alp)#4097'''
#13
'''cnt = 0
from ipaddress import *
net = ip_network('192.168.32.64/255.255.255.192', 0)
for ip in net:
    ip = f'{ip:b}'
    if ip[-3:] == '101':
        cnt+=1
print(cnt)#8'''
#9, https://education.yandex.ru/ege/task/0c156f32-0448-4aa9-a8c4-885a849fa93e
'''cnt = 0
for s in open('tasks/files/9.csv'):
    M = [int(x) for x in s.split(';')]
    copied = [x for x in M if M.count(x) == 2]
    uncopied = [x for x in M if M.count(x) == 1]
    if len(set(copied)) == 3 and len(uncopied) == 1:
        maxi = (sorted(copied))[-1]
        mini = (sorted(copied))[0]
        if uncopied[0] > mini and uncopied[0] < maxi:
            cnt+=1
print(cnt)#2004'''
#7, https://education.yandex.ru/ege/task/7832cb97-c76a-492e-82c1-cb1a4ed6a954
'''a = 1
b = 32000
c = 16
I = 1024000 * 5
t = I/(a*b*c)
print(t)#10'''
#13, КЕГЭ № 10577 (Уровень: Базовый)
"""
from ipaddress import *
R = []
for mask in range(32+1):
    net1 = ip_network(f'165.112.200.70/{mask}', 0)
    net2 = ip_network(f'165.112.175.80/{mask}', 0)
    if net1 == net2:
        R.append(mask)
print(max(R))
"""