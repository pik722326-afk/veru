# КИМ № 25037026
# № 2
#print ("x y z w")
"""for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F = y and (x or y) or (not(y or z)) or w
                if F == 0:
                    print (x, y, z, w, F )"""

# № 6
"""import turtle as t
t.screensize(5000, 5000)
t.tracer(0)
t.left(90)
s = 20
for i in range(2):
    t.fd(5 * s)
    t.left(90)
    t.backward(13 * s)
    t.left(90)
t.up()
t.backward(10 * s)
t.rt(90)
t.fd(9 * s)
t.left(90)
t.done()
for i in range(2):
    t.fd(11 * s)
    t.rt(90)
    t.fd (7 * s)
    t.rt(90)
t.up()
for x in range(-50, 50):
    for y in range(-50, 50):
        t.goto(x * s, y * s)
        t.dot (2, "purple")
t.update()
t.done()"""

"""import turtle as t
t.screensize(5000,5000)
t.tracer(0)
t.left(90)
s = 20
for i in range(2):
    t.fd(5 * s)
    t.left(90)
    t.backward(13 * s)
    t.left(90)
t.up()
t.backward(10 * s)
t.rt(90)
t.fd(9 * s)
t.left(90)
t.done()
for i in range(2):
    t.fd(11 * s)
    t.rt(90)
    t.fd (7 * s)
    t.rt(90)
t.up()
for x in range(-500, 500):
    for y in range(-500 ,500):
        t.goto(x * s, y * s)
        t.dot (2, "purple")
t.update()
t.done()"""

# № 13
"""from ipaddress import *
net = ip_network('192.168.32.48/255.255.255.240', 0)
cnt = 0
for ip in net:
    s = f'{ip:b}'
    if s.count('1') % 2 != 0:
        cnt += 1
print(cnt)
"""


# № 14
alp = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
def convert(n, b):
    r = ''
    while n > 0:
        r += alp[n % b]
        n //= b
    return r[::-1]
f = 2 * 729**333 + 2 * 243**334 - 81335 + 2 * 27**336 - 2 * 9**337 - 338
s = convert(f, 9)
s = s.count("0")
print (s)