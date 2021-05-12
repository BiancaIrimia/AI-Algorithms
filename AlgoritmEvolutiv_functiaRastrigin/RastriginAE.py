import math
import random
import numpy as np
import time
import functions as f
import matplotlib.pyplot as plt

MAX_INT: float = 5.12
MIN_INT: float = -5.12


def random_solution(n):
    return [random.uniform(MIN_INT, MAX_INT) for _ in range(n)]


def fitness(n, x):
    f = 10 * n
    for i in range(n):
        f = f + x[i] ** 2 - 10 * math.cos(2 * math.pi * x[i])
    return f


def init_pop(pop_size, n):
    pop = []
    for i in range(pop_size):
        pop.append(random_solution(n))
    return pop


def selectie_turnir(pop, pop_size):
    sample = np.random.default_rng().choice(pop_size, size=5, replace=False)
    best = pop[sample[0]].copy()
    for i in sample:
        if fitness(len(pop[i]), pop[i]) < fitness(len(best), best):
            best = pop[i].copy()
    return best


def best_of_all(pop, copii,  pop_size, n):
    pop_conc =  copii + pop
    pop_conc = sorted(pop_conc, key=lambda x: fitness(n, x))
    return pop_conc[:pop_size]


def show(best, worst, n):
    best_fit = []
    worst_fit = []
    for i in range(len(best)):
        best_fit.append(fitness(n, best[i]))
        worst_fit.append(fitness(n, worst[i]))
    plt.figure()
    plt.title("Evolutia algoritmului")
    plt.plot(best_fit, 'g')
    plt.plot(worst_fit, 'r')
    plt.show()


def meanPop(pop, n):
    sum = 0
    for i in range(0, len(pop)):
        sum = sum + fitness(n, pop[i])
    return sum / len(pop)


def rastriginAE(filename, nr_executii, n, nr_gen, pop_size, funcIncrucisare, funcMutatie):
    exect = 0
    best_of_all_gen = []
    worst_of_all_gen = []
    allavg = []
    timp = []
    bestmean = []
    worstmean = []
    while exect < nr_executii:
        start_time = time.time()
        pop = init_pop(pop_size, n)
        t = 0
        best = [sorted(pop, key=lambda x: fitness(n, x))[0]]
        worst = [sorted(pop, key=lambda x: fitness(n, x))[-1]]
        avg = []
        while t < nr_gen:
            copii = []
            for i in range(pop_size // 2):
                parinte1 = selectie_turnir(pop, pop_size)
                parinte2 = selectie_turnir(pop, pop_size)
                copil1 = parinte1[:]
                copil2 = parinte2[:]
                funcIncrucisare(copil1, copil2, n)

                copii.append(copil1)
                copii.append(copil2)

            copiimutanti = []
            for i in range(len(copii)):
                mutant = funcMutatie(copii[i], t)
                copiimutanti.append(mutant)

            pop = best_of_all(pop, copii,pop_size, n)

            best.append(pop[0])
            worst.append(pop[-1])
            avg.append(meanPop(pop, n))
            t = t + 1
        mean = 0
        for i in range(0, len(avg)):
            mean = mean + avg[i]
        mean = mean / len(avg)
        allavg.append(mean)
        best_of_all_gen.append(sorted(pop, key=lambda x: fitness(n, x))[0])
        worst_of_all_gen.append(sorted(pop, key=lambda x: fitness(n, x))[-1])
        bestmean.append(meanPop(best_of_all_gen, n))
        worstmean.append(meanPop(worst_of_all_gen, n))
        timp.append(start_time)
        exect = exect + 1
    show(best_of_all_gen, worst_of_all_gen, n)
    f.write(filename, bestmean, worstmean, allavg, timp, nr_gen, nr_executii, pop_size, best_of_all_gen[0])
