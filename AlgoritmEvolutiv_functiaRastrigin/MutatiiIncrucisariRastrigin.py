import numpy as np
import random
import RastriginAE as r


def verificare(x, i):
    if x[i] < r.MIN_INT:
        x[i] = r.MIN_INT
    if x[i] > r.MAX_INT:
        x[i] = r.MAX_INT


def incrucisare_medie(x, y, n):
    i = np.random.randint(n, size=2)
    print(i)
    xcopy = x.copy()
    x[i[0]] = (x[i[0]] + y[i[0]]) / 2
    y[i[0]] = (xcopy[i[0]] + y[i[0]]) / 2

    verificare(x, i[0])
    verificare(y, i[0])

    x[i[1]] = (x[i[1]] + y[i[1]]) / 2
    y[i[1]] = (xcopy[i[1]] + y[i[1]]) / 2

    verificare(x, i[1])
    verificare(y, i[1])


def incrucisare_convexa_simpla(x, y, n):
    pos = np.random.randint(n)
    alpha = random.random()
    print(pos)
    print(alpha)
    xcopy = x.copy()
    ycopy = y.copy()
    for i in range(pos, n):
        x[i] = alpha * xcopy[i] + (1 - alpha) * ycopy[i]
        y[i] = alpha * ycopy[i] + (1 - alpha) * xcopy[i]

        verificare(x, i)
        verificare(y, i)


def mutatie_uniforma(x, t):
    for i in range(len(x)):
        if random.random() < 0.3:
            x[i] = random.uniform(r.MIN_INT, r.MAX_INT)


def mutatie_gaussiana(x, t):
    SIGMA = 1 / (t + 1)
    MU = 0
    for i in range(len(x)):
        n = random.gauss(MU, SIGMA)
        if r.MIN_INT <= x[i] + n <= r.MAX_INT:
            x[i] += n
