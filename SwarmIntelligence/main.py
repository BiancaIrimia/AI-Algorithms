import SI as si

def main():
    #nr par, dim, iter, exe
    dim = int(input("Dimensiune: "))
    nr_particles = int(input("Numar particule: "))
    iteratii = int(input("Marime generatie: "))
    nr_exec = int(input("Nr executii: "))
    si.swarm("si.txt", nr_particles, dim, iteratii, nr_exec)
    print("done\n")


main()
