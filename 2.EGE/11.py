# 📚 Полезные ссылки на статьи и разборы задач:
# 📘 Полная версия шпаргалки доступна в нашем тг канале: https://t.me/informatika_kege_itpy/362?comment=6532
# 📘 Разборы 11 номеров по информатике: https://t.me/informatika_kege_itpy/360?comment=1496

# region Место для вашего конспекта ⬇️
'''
Запустите бота: https://t.me/ilandroxxy_bot и нажмите кнопку: "📚 Получить конспект"
'''
# endregion Место для вашего конспекта ⬆️

# Номер 11 (первый прототип - 1. sym, alp = byte)
'''
sym = 10
alp = 52   # alp <= 2**i

# i - это кол-во бит выделяемых на один символ
i = 6   #  2**6 = 64 >= alp

bit = sym * i
print(bit)  # 60 бит на один пароль

print(bit / 8)  # 7.5 -> 8
byte = 8  # 8 байт на один пароль

print((byte * 65_536) / 2**10)
'''


# https://education.yandex.ru/ege/inf/task/30431c9e-dfcf-41dc-8b5d-1c0fd87fcb2e
# (первый прототип - 1. sym, alp = byte)
'''
sym = 31
alp = 10 + 26
i = 6  # 2**6 >= alp

bit = sym * i
print(bit / 8)  # 23.25 -> 24
byte = 24

# user = byte + dop

user = (12 * 2**10) / 128
print(user - byte)  # 72
'''


# https://education.yandex.ru/ege/inf/task/a4132687-04dc-4ed6-85e0-76ebd94d668a
# (второй прототип - 2. sym, byte = alp)
'''
sym = 197

byte = (25 * 2**20) / 178_080
print(byte)  # 147.2057 -> 148 (отведено более 25 Мбайт памяти)
bit = 148 * 8

i = bit / sym
print(i)  # 6.0101 -> 7 (отведено более 25 Мбайт памяти)

print(f'Определите максимальную возможную мощность алфавита: {2**7}')
print(f'Определите минимально возможную мощность алфавита: {2**6+1}')

alp = 129  # i = 8

alp = 128  # i = 7
alp = 64  # i = 6

alp = 65  # i = 7
'''


# https://education.yandex.ru/ege/inf/task/b7bccef2-d2fe-4064-8fcd-69ea6cd792c2
# (второй прототип - 2. sym, byte = alp)
'''
sym = 172

byte = 54 * 2**20 / 356_984
print(byte)  # 158.6152 -> 159 (потребовалось не менее 54 Мбайт памяти)
bit = 159 * 8

i = bit / sym
print(i)  # 7.395 -> 8 (потребов алось не менее 54 Мбайт памяти)

print(f'Определите максимальную возможную мощность алфавита: {2**8}')
print(f'Определите минимально возможную мощность алфавита: {2**7+1}')
'''


# https://education.yandex.ru/ege/inf/task/90b2bc03-59cf-406d-b7b5-e2bca0b8580a
# (третий прототип - 3. alp, byte = sym)
'''
alp = 10 + 27
i = 6

byte = 12 * 2**10 / 3548
print(byte)  # 3.4633 -> 4 (необходимо более 12 Кбайт памяти)
bit = 4 * 8

sym = bit / i
print(sym)  # 5.3333 -> 5
'''


# Домашка 11 номер: https://stepik.org/lesson/1038676/step/1?unit=1062784

# Практика 11 номер: https://stepik.org/lesson/1209382/step/1?unit=1222617

