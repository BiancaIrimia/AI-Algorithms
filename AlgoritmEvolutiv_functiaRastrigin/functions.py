def write(filename, best_of_all_gen, worst_of_all_gen, allavg, timp, nr_gen, nr_executii, pop_size, best_sol):
    mean = 0
    meanTime = 0
    f = open(filename, "a")
    f.write(
        "nr exec = " + str(nr_executii) + " nr_gen = " + str(nr_gen) + " pop_size = " + str(pop_size) + "\n")
    f.write("best_sol = " + str(best_sol) + "\n")
    for i in range(len(best_of_all_gen)):
        f.write(str(best_of_all_gen[i]) + " " + str(allavg[i]) + " " + str(worst_of_all_gen[i]) + "\n")
        mean = mean + allavg[i]
        meanTime = meanTime + timp[i]
    mean = mean / len(allavg)
    meanTime = meanTime / len(timp)
    f.write(str(mean) + "\n")
    f.write(str(meanTime) + "\n\n")

    f.close()
