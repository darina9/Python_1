Ax = float(input('Введите координаты точки a по оси x:'))
Ay = float(input('Введите координаты точки a по оси y:'))
Bx = float(input('Введите координаты точки b по оси x:'))
By = float(input('Введите координаты точки b по оси y:'))
import math
distans = math.sqrt((Ax-Bx)**2+(Ay-By)**2)

print(f'Расcтояние между точками = {distans:.2f}')