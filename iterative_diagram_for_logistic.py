import matplotlib.pyplot as plt
from numpy import *
from stable_and_periodic_points import stable_point_logistic
def iter_diagram_logistic(rr):
        x1 = stable_point_logistic(rr)[0][1]
        r = rr
        def ff(x):
                return r * x * (1 - x)
        if x1 == 0:
                b = 1
        else:
                b = r*x1*(1-x1)/x1
        def fl(x):
                return b * x
        def iter_thing(a, x1, x, y, iter):
                Y = []
                X = []
                for i in arange(1, iter, 1):
                        if abs(y) > 2 or abs(x) > 2:
                                break
                        X.append(x)
                        Y.append(y)

                        y = ff(x)
                        X.append(x)
                        Y.append(y)
                        x = y / b

                return X, Y
        if r<1:
                plt.title(f'Итерационная диаграмма логистического \n отображения rx(1-x) при r = {r}')
                plt.plot(iter_thing(r, x1, .2, 0, 30)[0], iter_thing(r, x1, .2, 0, 30)[1], "r")
                plt.plot(iter_thing(r, x1, -.08, 0, 30)[0], iter_thing(r, x1, -.08, 0, 30)[1], "r")
                plt.plot(iter_thing(r, x1, -.15, 0, 5)[0], iter_thing(r, x1, -.15, 0, 5)[1], "r")
        elif 1<r<3:
                plt.title(f'Итерационная диаграмма логистического \n отображения rx(1-x) при r = {r}')
                plt.plot(iter_thing(r, x1, .2, 0, 30)[0], iter_thing(r, x1, .2, 0, 30)[1], "r")
                plt.plot(iter_thing(r, x1, .04, 0, 30)[0], iter_thing(r, x1, .04, 0, 30)[1], "r")
                plt.plot(iter_thing(r, x1, -.05, 0, 30)[0], iter_thing(r, x1, -.05, 0, 30)[1], "r")
        elif r > 3:
                plt.title(f'Итерационная диаграмма логистического \n отображения rx(1-x) при r = {r}')
                plt.plot(iter_thing(r, x1, .2, 0, 300)[0], iter_thing(r, x1, .2, 0, 300)[1], "r")
                plt.plot(iter_thing(r, x1, -.04, 0, 300)[0], iter_thing(r, x1, -.04, 0, 300)[1], "r")
        elif r == 1:
                plt.title(f'Итерационная диаграмма логистического \n отображения rx(1-x) при r = {r}')
                plt.plot(iter_thing(r, x1, .2, 0, 300)[0], iter_thing(r, x1, .2, 0, 300)[1], "r")
                plt.plot(iter_thing(r, x1, -.04, 0, 300)[0], iter_thing(r, x1, -.04, 0, 300)[1], "r")
        x1 = arange(-.5, 1, 0.001)
        y1 = [ff(x) for x in x1]
        y2 = [fl(x) for x in x1]
        plt.plot(x1, y1, 'b')
        plt.plot(x1, y2, 'g')
        plt.grid(True)
        plt.show()