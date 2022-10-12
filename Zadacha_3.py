a=int(input('Введите координаты точки X :'))
b=int(input('Введите координаты точки Y :'))
if a>0 and b>0:
    print('1-я четверть')
elif a<0 and b>0:
    print('2-я четверть')
elif a<0 and b<0:
    print('3-я четверть')
elif a>0 and b<0:
    print('4-я четверть')
elif a==0 or b==0 :
    print('неверный ввод')