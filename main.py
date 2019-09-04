import math
import matplotlib.pyplot as plt
import random

class Vector:

    def __init__(self, x=0.0, y=0.0, z=0.0):
        self.x = x
        self.y = y
        self.z = z

    def get_mag(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def get_unit(self):
        mag = self.get_mag()
        return self / mag

    def __truediv__(self, num):
        return Vector(self.x / num, self.y / num, self.z / num)

    def __mul__(self, num):
        return Vector(self.x * num, self.y * num, self.z * num)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __str__(self):
        return "x: " + str(self.x) + " y: " + str(self.y) + " z: " + str(self.z)

    def copy(self):
        return Vector(self.x, self.y, self.z)

    def getX(self):
        return self.x

    def getY(self):
        return self.y


class Handler:
    m = 0.018
    g = 9.81

    r_i = Vector()
    v_i = Vector()
    p_i = Vector(v_i.x * m, v_i.y * m, v_i.z * m)

    r_f = Vector()
    v_f = Vector()
    p_f = Vector(v_f.x * m, v_f.y * m, v_f.z * m)

    F_g = Vector(0, -m * g, 0)
    net_Force = Vector()
    forces = [F_g]

    def __init__(self, delta_t):
        self.delta_t = delta_t

    def calculate_net_force(self):
        for i in self.forces:
            self.net_Force += i

    def update_momentum(self):
        self.calculate_net_force()
        delta_p = self.net_Force * self.delta_t
        self.p_f = self.p_i + delta_p

    def update_pos(self):
        v_avg = self.p_f / self.m
        delta_r = v_avg * self.delta_t
        self.r_f = self.r_i + delta_r

    def add_force(self, force):
        self.forces.append(force)

    def calculate(self):
        self.update_momentum()
        self.update_pos()
        self.p_i = self.p_f.copy()
        self.r_i = self.r_f.copy()
        self.p_f *= 0


class Spring:

    t = 0.1
    delta_t = 0.05
    iterations = int(round(t / delta_t))

    pos_arr = []

    def __init__(self, L, L_0, k):
        self.handler = Handler(self.delta_t)
        self.handler.r_i = L.copy()
        self.L = L
        self.L_0 = L_0
        self.k = k
        self.pos_arr.append(L.copy())

    def addMass(self, mass):
        s.handler.m += mass

    def update(self):

        self.handler.p_i = Vector(-0.02, -0.01, -0.02)
        self.handler.r_i = Vector(-0.2, -0.61, 0)

        for i in range(0, self.iterations):
            self.handler.forces = []

            s = self.L.get_mag() - self.L_0
            F = self.L.get_unit() * -self.k * s
            self.handler.add_force(F)
            self.handler.add_force(self.handler.F_g)

            self.handler.calculate()

            self.L = self.handler.r_f.copy()

            self.pos_arr.append(self.handler.r_f)


s = Spring(Vector(-0.2, -0.61, 0), 0.325, 0.870)
s.addMass(0.018)
s.update()

xs = [s.delta_t * i for i in range(0, s.iterations + 1)]
ys = [pos.getY() for pos in s.pos_arr]

# plt.plot(xs, ys)
# plt.axis([0, xs[len(xs) - 1], -0.5, 1.5])
# plt.show()

print(s.handler.r_f)
print(s.iterations)

