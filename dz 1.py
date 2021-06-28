time = int(input('Введите число'))
sec = 1
min = sec * 60
hour = min * 60
day = hour * 24
if time < min:
    print(str(time) + ' сек. ')
elif time < hour >= min:
    print(str(time // min) + ' мин. ' + str(time % min) + ' сек. ')
elif time < day >= hour:
    print(str(time // hour) + ' ч. ' + str(time % hour // min) + ' мин. ' + str(time % min) + ' сек. ')
else:
    print(str(time // day) + ' д. ' + str(time % day // hour ) + ' ч. ' + str(time % day % hour // min) + ' мин. ' + str(time % day % hour % min // sec) + ' сек. ' )