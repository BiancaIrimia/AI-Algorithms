def write(filename, exect, iter, nr_particles, dim, allgbest, timp):
    mean = 0
    meanTime = 0
    f = open(filename, "a")
    f.write("nr exec = " + str(exect) + " iteratii = " + str(iter) + " dim = " + str(dim) + " nr_particule = " + str(
        nr_particles) + " \n")
    for i in range(len(allgbest)):
        f.write(str(allgbest[i]) + " \t" + str(timp[i]) + "\n")
        mean = mean + allgbest[i]
        meanTime = meanTime + timp[i]
    mean = mean / len(allgbest)
    meanTime = meanTime / len(timp)
    f.write("medie gbest = " + str(mean) + " \n")
    f.write("timp mediu= " + str(meanTime) + " \n\n")

    f.close()
