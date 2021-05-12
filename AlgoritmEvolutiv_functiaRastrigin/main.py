import RastriginAE as r
import MutatiiIncrucisariRastrigin as m


def optiuni():
    print("1. Functia Rastrigin incrucisare medie si mutatie uniforma\n"
          "2. Functia Rastrigin incrucisare medie si mutatie gaussiana\n"
          "3. Functia Rastrigin incrucisare convexa simpla si mutatie uniforma\n"
          "4. Functia Rastrigin incrucisare convexa simpla si mutatie gaussiana\n"
          "0. Exit\n"
          )
def meniu():
    optiuni()
    opt = int(input("Optiune:\n"))
    a = 0.000001
    print(a)
    while opt != 0:
        if opt == 1:
            dim = int(input("Dimensiune: "))
            nr_gen = int(input("Numar generatii: "))
            pop_size = int(input("Marime generatie: "))
            nr_exec = int(input("Nr executii: "))
            r.rastriginAE("rastrigin-solutii2.txt", nr_exec, dim, nr_gen, pop_size, m.incrucisare_medie, m.mutatie_uniforma)
            print("done\n")
            opt = int(input("Optiune:\n"))
        if opt == 2:
            dim = int(input("Dimensiune: "))
            nr_gen = int(input("Numar generatii: "))
            pop_size = int(input("Marime generatie: "))
            nr_exec = int(input("Nr executii: "))
            r.rastriginAE("rastrigin-solutii2.txt", nr_exec, dim, nr_gen, pop_size, m.incrucisare_medie, m.mutatie_gaussiana)
            print("done\n")
            opt = int(input("Optiune:\n"))
        if opt == 3:
            dim = int(input("Dimensiune: "))
            nr_gen = int(input("Numar generatii: "))
            pop_size = int(input("Marime generatie: "))
            nr_exec = int(input("Nr executii: "))
            r.rastriginAE("rastrigin-solutii2.txt", nr_exec, dim, nr_gen, pop_size, m.incrucisare_convexa_simpla, m.mutatie_uniforma)
            print("done\n")
            opt = int(input("Optiune:\n"))
            opt = int(input("Optiune:\n"))
        if opt == 4:
            dim = int(input("Dimensiune: "))
            nr_gen = int(input("Numar generatii: "))
            pop_size = int(input("Marime generatie: "))
            nr_exec = int(input("Nr executii: "))
            r.rastriginAE("rastrigin-solutii2.txt", nr_exec, dim, nr_gen, pop_size, m.incrucisare_convexa_simpla, m.mutatie_gaussiana)
            print("done\n")
            opt = int(input("Optiune:\n"))



def print_hi(name):

    r.rastriginAE("rastrigin-solutii2.txt", 10, 5, 1000, 200, m.incrucisare_convexa_simpla, m.mutatie_gaussiana)



if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
