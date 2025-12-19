#Номер 1
"""print('1 2 3 4 5 6 7')
from itertools import permutations
table = '13 14 16 24 25 31 36 41 42 45 52 54 57 61 63 67 75 76'
graph = 'GD DG DE ED GE EG DF FD FA AF AB BA AC CA CB BC CE EC'
for p in permutations('ABCDEFG'):
    new_table = table
    for i in range(1, 7+1):
        new_table = new_table.replace(str(i), p[i-1])
    if set(new_table.split()) == set(graph.split()):
        print(*p)"""

# Номер 2
"""print('x y z w F')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                F = (x <= (z == w)) or (not(y <= w))
                if F == 0:
                    print(x, y, z, w, int(F))
"""
#Номер 5 -
#Номер 6
#Направо 90
#Повтори 3 [Направо 45 Вперёд 10 Направо 45]
#Направо 315 Вперёд 10
#Повтори 2 [Направо 90 Вперёд 10].
"""import turtle as t
t.screensize(5000, 5000)
t.left(90)
t.tracer(0)
s = 30
t.right(90 * s)
for i in range(3):
    t.right(45)
    t.forward(10 * s)
    t.right(45)
t.right(315)
t.forward(10 * s)
for i in range(2):
    t.right(90)
    t.forward(10 * s)
t.up()
for x in range(-50, 50):
    for y in range(-50, 50):
        t.goto(x * s, y * s)
        t.dot(2,'purple')
t.update()
t.done()"""

#Номер 16
#F(n) = 3, при n < 3
#F(n) = 2 n + 5 + F(n - 2), если n ≥ 3
#Чему равно значение выражения F(3027) - F(3023)?
"""def F(n):
    if n <= 3:
        return 3
    if n >= 3:
        return 2 * n + 5 + F(n - 2)

print (F(37))"""

#Номер 19-21
def F(s, n):
    if s >= 111 :
        return n % 2 == 0
    if n == 0:
        return 0
    h = [F(s + 1, n-1), F(s + 3, n-1), F(s * 4, n-1)]
    return any(h) if (n - 1) % 2 == 0 else all(h)  # else any(h)

print([s for s in range(1, 110 +1) if F(s, n=2)])
print([s for s in range(1, 110 +1) if F(s, n=3) and not F(s, n=1)])
print([s for s in range(1, 110 +1) if F(s, n=4) and not F(s, n=2)])
