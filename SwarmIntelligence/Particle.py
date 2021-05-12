import random
import math

V_MAX = 1
MAX_F: float = 5.12
MIN_F: float = -5.12
MAX_V: float = 1/10 * 5.12
MIN_V: float = -5.12 * 1/10

def fitness(n, x):
    f = 10 * n
    for i in range(len(x)):
        f = f + x[i] ** 2 - 10 * math.cos(2 * math.pi * x[i])
    return f

class Particle:
    def __init__(self, n):
        self.positions = [random.uniform(MIN_F, MAX_F) for _ in range(n)]
        self.pbest = 10000
        self.velocity = [random.uniform(MIN_V, MAX_V) for _ in range(n)]
        self.current_fitness = fitness(n, self.positions)

    def modify_velocity(self, gbest, w, c1, c2):
        v = self.velocity.copy()
        for i in range(0, len(v)):
            v[i] = w * self.velocity[i] + c1 * random.random() * (self.pbest - self.positions[i]) + c2 * random.random() * (gbest - self.positions[i])
            if MIN_V <= v[i] <= MAX_V:
                self.velocity[i] = v[i]


    def modify_position(self):
        for i in range(0, len(self.positions)):
            if MIN_F <= self.positions[i] + self.velocity[i] <= MAX_F:
                self.positions[i] = self.positions[i] + self.velocity[i]
        self.current_fitness = fitness(len(self.positions), self.positions)

    def update_pbest(self):
        if self.current_fitness < self.pbest:
            self.pbest = self.current_fitness

    def set_fitness(self):
        self.current_fitness = fitness(len(self.positions), self.positions)

    def get_fitness(self):
        return self.current_fitness

    def get_pbest(self):
        return self.pbest

    def __repr__(self):
        return "x: " + str(self.positions) + " fitness: " + str(self.current_fitness) + " pbest: " + str(self.pbest) + " velocity: " + str(self.velocity) + "\n"
