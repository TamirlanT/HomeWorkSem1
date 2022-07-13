x = int(input('Введите координаты x = '))
y = int(input('Введите координаты y = '))
if x > 0 and y > 0 :
    print ('Первая четверть')
elif x > 0 and y < 0 :
    print ('Вторая четверть')
elif x < 0 and y < 0 :
    print ('Третья четверть')
elif x < 0 and y > 0 :
    print ('Четвертая четверть')
else: print ('Координаты не должны быть равны нулю')