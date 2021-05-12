import Particle as p
import functions as f
import time

w = 0.5
c1 = 2
c2 = 1


def swarm(filename, nr_particles, dim, iter, exect):
    e = 0
    it = iter
    timp = []
    allgbest = []

    while e < exect:
        start_time = time.time()
        particles = []
        gbest = 10000
        for i in range(0, nr_particles):
            particles.append(p.Particle(dim))


        # print(particles)
        iter = it
        while iter > 0:
            for i in range(0, nr_particles):
                particles[i].update_pbest()

            for i in range(0, nr_particles):
                if particles[i].get_pbest() < gbest:
                    gbest = particles[i].get_pbest()

            for i in range(0, nr_particles):
                particles[i].modify_velocity(gbest, w, c1, c2)
                particles[i].modify_position()
            iter = iter - 1

        allgbest.append(gbest)
        timp.append(start_time)
        e = e + 1

    f.write(filename, exect, it, nr_particles, dim, allgbest, timp)
