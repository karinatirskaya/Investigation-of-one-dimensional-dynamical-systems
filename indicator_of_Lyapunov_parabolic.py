import numpy as np
import matplotlib.pyplot as plt

def lyapunov_parabolic(r):

    def logistic(x):
        return 1 - r * x ** 2

    def derivative(x):
        return - r * 2 * x

    def track(n, x_start):
        mass = [0] * n
        mass[0] = x_start
        for i in range(1, n):
            mass[i] = logistic(mass[i-1])
        return mass


    def poklyap(T, M, mass):
        V = 1
        x = mass[0]
        k = 0
        s = [0] * M
        for j in range(M):
            for i in range(T):
                V = derivative(x) * V
                x = mass[k + 1]
                k += 1
            if np.linalg.norm(V) != 0:
                s[j] = np.log(np.linalg.norm(V))
                V = V / np.linalg.norm(V)
        return sum(s)/(M * T)

    X = track(200000, 0.1)
    Xob = X[70000:]

    plt.scatter(Xob, [0] * len(Xob))
    if poklyap(1, 100000 - 1, Xob) == 0:
        print('Показателя Ляпунова не существует')
    else:
        print(poklyap(1, 30000 - 1, Xob))
    plt.show()