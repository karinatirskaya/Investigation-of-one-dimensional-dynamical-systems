from matplotlib import pyplot as plt
from numpy import linspace  #проще точки перебрать

def bifur_parabolic():
    A = []  #множества для графика
    X = []
    #Функция отображения параболы
    def parabolic(y, a):
        return 1 - a*y**2

    #Логистическая история
    def logistic(x ,r):
        return r*x*(1-x)

    x_previous = 0.1 #начальное условие
    for a in linspace(- 1/8-0.001, 2, 2000):
        for i in range(100000): #переходный процесс - его отрезаем с помощью невключения этих элементов
            x = x_previous
            x_previous = parabolic(x, a)
        for i in range(30000):  #а вот это уже рисуем
            x = x_previous
            A.append(a)
            X.append(x)
            x_previous = parabolic(x, a)
    fig = plt.figure()
    ax = fig.add_subplot()
    ax.set_title(r'Бифуркационное дерево для отображения параболы $1-ay^2$')
    ax.scatter(A,X, s=0.00001)  #s - параметр размера точек, c - цвет графика (люблю строить бифуркации в черном цвете - видно лучше)
    ax.set_xlabel(r'$ a $')
    ax.set_ylabel(r'$ y $')
    plt.show()