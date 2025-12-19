cmt = 0
m = 0
import time
def countdown_timer(seconds):
    while seconds:
        mins, secs = divmod(seconds, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end='\r')  # Печатает таймер на одной строке
        time.sleep(1)
        seconds -= 1
        print(seconds,"секунд")
#        print ("Осталось",seconds,"секунд")

    print("Время вышло!")

# Запрос времени у пользователя
try:
    total_seconds =int(input("Введите время в секундах: "))
    countdown_timer(total_seconds)
except ValueError:
    print("Пожалуйста, введите целое число.")
for i in range(15005):
    cmt += 1
    print(cmt,"poiuytrewqasdfghjkl;'/.,bvcxz")


#import os
#os.system("shutdown /s /t 1")  # выключение через 10 секунд
"""b = 0
a = int(input())
for i in range(a):
    b = a - 1
    print (b)"""