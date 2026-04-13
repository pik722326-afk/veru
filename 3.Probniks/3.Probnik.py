# 1

"""
print('1 2 3 4 5 6 7')
from itertools import permutations
table = '14 17 23 25 27 32 35 36 37 41 46 52 53 56 63 64 65 71 72 73'
graph = 'AD DA AG GA DB  BF FB EF FE EC BD BE EB CE EG GE FC CF CG GC'
for p in permutations('ABCDEFG'):
    new_table = table
    for i in range(1, 7+1):
        new_table = new_table.replace(str(i), p[i-1])
    if set(new_table.split()) == set(graph.split()):
        print(*p)"""

#Ответ 25


# 2
'''print('x y z w')
for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                F = (x or not(y)) and not(y==z) and not(w)
                if F == 1:
                    print(x,y,z,w)'''
#Ответ xzyw


# 5
'''
def convert(n,b):
    r = ''
    while n >0:
        r += str(n%b)
        n //= b
    return r[::-1]
R = []
for n in range(1,10000):
    m = convert(n,3)
    if n % 3 == 0:
        m1 = m + m[-3:]
    else:
        n1 = (n%3)*3
        n2 = convert(n1,3)
        m1 = m + n2
    r = int(m1,3)
    if r > 150:
        R.append(n)
print(min(R))'''
#Ответ 9


# 6
"""
import turtle as t
t.screensize(5000,5000)
t.left(90)
t.tracer(0)
s = 30
for i in range(4):
    t.forward(10*s)
    t.right(270)
t.up()
t.forward(3*s)
t.right(270)
t.forward(5*s)
t.right(90)
t.down()
for i in range(2):
    t.forward(10*s)
    t.right(270)
    t.forward(12*s)
    t.right(270)
t.up()
for x in range(-50,50):
    for y in range(-50,50):
        t.goto(x*s,y*s)
        t.dot(4, "red")
t.update()
t.done()"""
#Ответ 216


# 13
'''from ipaddress import *
for mask in range(1,33):
    net = ip_network(f'111.118.179.50/{mask}',0)
    if "111.118.178.0" in str(net):
        print(net, net.netmask)'''
#Ответ 254


# 15
"""
def F(A,x,y):
    return (x < A) or (3*y + 2*x >120) or (A >y)
for A in range(1,10000):
    if all(F(A,x,y) for x in range(1,100) for y in range(1,100)):
        print(A)
        break"""
#Ответ 25


# 16
'''
import sys
sys.setrecursionlimit(10**8)
def F(n):
    if n == 1:
        return 1
    if n > 1:
        return n-1 + F(n-1)
print(F(2024)-F(2022))'''
#Ответ 4045


# 19 - 21
"""
def F(s,n):
    if s >= 473:
        return n%2 == 0
    if n == 0 :
        return 0
    h = [F(s+1,n-1), F(s+5, n-1), F(s*4,n-1)]
    return any(h) if (n-1)%2 == 0 else all(h)

print([s for s in range(1,472) if F(s,n=2)])
print([s for s in range(1,472) if F(s,n=3) and not F(s,n=1)])
print([s for s in range(1,472) if F(s,n=4) and not F(s,n=2)])"""
# 19 [118]
# 20 [113, 117]
# 21 [112]


# 23
'''
def F(a,b):
    if a >= b or a == 13:
        return a == b
    return F(a+1,b) + F(a+2,b) + F(a*3,b)

print(F(3,8)*F(8,18))'''
#Ответ 200