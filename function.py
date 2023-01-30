# f(x) = -12x^4*sin(cos(x)) - 18x^3+5x^2 + 10x - 30

# 1. Определить корни
# 2. Найти интервалы, на которых функция возрастает
# 3. Найти интервалы, на которых функция убывает
# 4. Построить график
# 5. Вычислить вершину
# 6. Определить промежутки, на котором f > 0
# 7. Определить промежутки, на котором f < 0

# -----------------------------------------------------
# 1. График показывает, что функция имеет бесконечное множество корней.
# 2,3. Интервалов, на которых функция возрастает и убывает - бесконечное множество.
#      Интервал x=[-10,10].
# 4. Графики для интервалов x=[-10,10] и x=[-100,100] построены.
# 5. Минимальное и максимальное значение функции находится в бесконечности.
#      Для интервала x=[-10,10] показал.
# 6. Функция множество раз меняет значение относительно нуля.
#      Указать все невозможно.


import numpy as np
import matplotlib.pyplot as plt


a, b, c, d, e = -12, -18, 5, 10, -30
x1 = np.arange(-10, 10, 0.01)
x2 = np.arange(-100, 100, 0.01)

# Для промежуточных точек:
x3 = np.arange(-7.5, -5, 0.01)
x4 = np.arange(-5, -3, 0.01)
x5 = np.arange(2.5, 5, 0.01)
x6 = np.arange(7.5, 10, 0.01)


def func(x):
    function = a*x**4*np.sin(np.cos(x)) + b*x**3 + c*x**2 + d*x + e
    return function


# Минимальное значение func на интервале для х 
def find_min(xx):    
    min_y = func(xx[0])
    min_x = xx[0]
    for i in xx:
        if func(i) < min_y:
            min_y = round(func(i), 2)
            min_x = round(i, 2)
    min_xy = [min_x, min_y]
    return min_xy

# Максимальное значение func на интервале для х 
def find_max(xx):
    max_y = func(xx[0])
    max_x = xx[0]
    for i in xx:
        if func(i) > max_y:
            max_y = round(func(i), 2)
            max_x = round(i, 2)
    max_xy = [max_x, max_y]
    return max_xy


def drawing_func(x1, x2):
    plt.figure(figsize=(7,7))
    plt.subplot(2,1,1)
    x_range_down1 = np.arange(max_for_ten[0], point1[0], 0.01)
    x_range_down2 = np.arange(point2[0], -2.5, 0.01)
    x_range_down3 = np.arange(point3[0], min_for_ten[0], 0.01)
    x_range_up1 = np.arange(point1[0], point2[0], 0.01)
    x_range_up2 = np.arange(min_for_ten[0], point4[0], 0.01)
    x_range_straight = np.arange(-2.5, point3[0], 0.01)
    # plt.plot(x1, f2(x1))
    plt.plot(x_range_down1, func(x_range_down1), 'r', label="Убывание")
    plt.plot(x_range_up1, func(x_range_up1), 'b', label="Возрастание")
    plt.plot(x_range_down2, func(x_range_down2), 'r')    
    plt.plot(x_range_down3, func(x_range_down3), 'r')
    plt.plot(x_range_up2, func(x_range_up2), 'b')
    plt.plot(x_range_straight, func(x_range_straight), label="Малые колебания")    
    plt.plot(min_for_ten[0], min_for_ten[1], 'ro')
    plt.text(min_for_ten[0] + 0.5, min_for_ten[1], f'min(x) = {min_for_ten[0]}')
    plt.plot(max_for_ten[0], max_for_ten[1], 'ro')
    plt.text(max_for_ten[0] + 0.5, max_for_ten[1], f'max(x) = {max_for_ten[0]}')
    plt.grid()
    plt.legend()
    plt.title('x=[-10;10]')
    plt.subplot(2,1,2)
    plt.plot(x2, f2(x2))
    plt.grid()
    plt.title('x=[-100;100]')
    plt.show()

f2 = np.vectorize(func)
min_for_ten = find_min(x1)
max_for_ten = find_max(x1)
print(f'Наименьшее значение функции на интервале [-10,10]: {min_for_ten}')
print(f'Наибольшее значение функции на интервале [-10,10]: {max_for_ten}')

# Находим координаты точек перегибов:
point1 = find_min(x3)
point2 = find_max(x4)
point3 = find_max(x5)
point4 = find_max(x6)
drawing_func(x1, x2)