# 📚 Полезные ссылки на статьи и разборы задач:
# 📘 Полная версия шпаргалки доступна в нашем тг канале: https://t.me/informatika_kege_itpy/362?comment=6532
# 📘 Разборы 27 номеров по информатике: https://t.me/informatika_kege_itpy/360?comment=7007

#№ 23209 Основная волна 10.06.25 (Уровень: Базовый)
'''from math import dist
def center(cl):
    R = []
    for p in cl:
        summa = 0
        for g in cl:
            summa += dist(p, g)
        R.append([summa, p])
    return min(R)[1]
clusterA = [[], []]
clusterB = [[], [], []]
for s in open('27_A_23209.txt'):
    s = s.replace(',', '.')
    x, y = [float(x) for x in s.split()]
    if x > 5:
        clusterA[0].append([x, y])
    if x < 5:
        clusterA[1].append([x, y])
for s in open('27_B_23209.txt'):
    s = s.replace(',', '.')
    x, y = [float(x) for x in s.split()]
    if y > 21 and x > 6 and x < 16:
        clusterB[0].append([x, y])
    if y < 21 and y > 12 and x > 6 and x < 16:
        clusterB[1].append([x, y])
    if y < 12 and x > 6 and x < 16:
        clusterB[2].append([x, y])
print(center(clusterA[0]))#[6.9663606, 19.2156207]
print(center(clusterA[1]))#[3.9100466, 6.6396418]
PxMAX = int(6.9663606 * 10000)
PyMAX = int(19.2156207 * 10000)
print(center(clusterB[0]), len(clusterB[0]))#[12.1302947, 23.4222296] 75
print(center(clusterB[1]), len(clusterB[1]))#[8.4874654, 18.9031256] 131
print(center(clusterB[2]), len(clusterB[2]))#[12.2170442, 7.2915548] 397
Qx = int(abs((12.1302947 - 12.2170442) * 10000))
Qy = int(abs((23.4222296 - 7.2915548) * 10000))
print(PxMAX, PyMAX, Qx, Qy)#Answer: 69663 192156 867 161306'''

