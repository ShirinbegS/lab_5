import matplotlib.pyplot as plt
import numpy as np
from math import *

def f(x):
    return cos(x+x**3) #задала функцию

x = np.linspace(-10, 10, 10) #список точек от -3 до 3 (1000 точек)
y1 = [f(i) for i in x] #список точек функции из варианта
y2 = [-0.9 for i in x] #касательная в точке 0

plt.title('Вариант 11') #заголовок
plt.xlabel('x') #ось абцисс
plt.ylabel('y') #ось ординат
plt.grid() #включение сетки
plt.plot(x, y1, label='(x**2)*(atan(x))') #построение функции
plt.plot(x, y2, 'r', label='Касательная') #построение касательной
plt.text(0.785, -0.9, 'точка касания') #аннотация
plt.text(-6, -0.9, 'точка касания') #аннотация
plt.legend() #легенда
plt.show()