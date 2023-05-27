from sympy import *
import matplotlib.pyplot as plt
from numpy import *

def iter_diagram_parabolic(rr):
    inter = 30  # итерации
    if -0.25 < rr < 0:
        x_0 = [0.9, 2.8, 4.1]  # начальные точки
        predely_postroenia_paraboly = [-1, 5.5]
    if 0 < rr < 0.75:
        x_0 = [0.9, -1.5, -2.25]  # начальные точки
        predely_postroenia_paraboly = [-3, 2]
    if 0.75 < rr < 1.25:
        x_0 = [-2, -1.8, 0.95]  # начальные точки
        predely_postroenia_paraboly = [-3, 1.5]
        inter = 70
    r, x = symbols('r x')  # обозначили за символы


    def uravnenie1(r):  # объявляем первую систему
        return 1 - r * x ** 2


    reshenie = solve(uravnenie1(r) - x, x)  # решаем уравнение для нахождения неподвижных точек
    x_2 = reshenie[1].subs(r, rr)
    x_1 = reshenie[0].subs(r, rr)


    def ff(x):
        return 1 - rr * x ** 2


    def iter_thing(rr, x_2, x_0, iter):
        y = 0
        Y = []
        X = []
        for i in arange(1, iter, 1):
            X.append(x_0)
            Y.append(y)

            y = ff(x_0)
            X.append(x_0)
            Y.append(y)
            x_0 = y
        return X, Y


    x1 = arange(predely_postroenia_paraboly[0], predely_postroenia_paraboly[1], 0.001)
    if x_1 == 0:
        plt.title(f'Итерационная диаграмма \n отображения параболы $1-ax^2$ при a = {rr}')
        plt.plot(iter_thing(rr, x_2, x_0[0], inter)[0], iter_thing(rr, x_2, x_0[0], inter)[1], "r")
        y1 = [ff(x) for x in x1]
        plt.plot(x1, x1, 'g')
        plt.plot(x1, y1, 'b')
        plt.grid(True)
        plt.show()

    else:
        for k_0 in x_0:
            plt.title(f'Итерационная диаграмма \n отображения параболы $1-ax^2$ при a = {rr}')
            try:
                plt.plot(iter_thing(rr, x_2, k_0, inter)[0], iter_thing(rr, x_2, k_0, inter)[1], "r")
                y1 = [ff(x) for x in x1]
                plt.plot(x1, x1, 'g')
                plt.plot(x1, y1, 'b')
                plt.grid(True)
            except Exception:
                inter_new = 5
                plt.plot(iter_thing(rr, x_2, k_0, inter_new)[0], iter_thing(rr, x_2, k_0, inter_new)[1], "r")
                y1 = [ff(x) for x in x1]
                plt.plot(x1, x1, 'g')
                plt.plot(x1, y1, 'b')
                plt.grid(True)
        plt.show()
