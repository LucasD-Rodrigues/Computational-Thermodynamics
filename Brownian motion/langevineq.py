import numpy as np
import matplotlib.pyplot as plt

times = np.linspace(0,10,1001)
m = 0.3
b = 0.05
a = 1

h = 0.01
t0 = 0
Y0 = [0,0]


def F(Y, t, Z):
    return np.array([Y[1], (-b/m)*Y[1] + (a/m)*Z])

class Integrator:

    def RK2(F, Y0, t0, h):
        Y_list = []
        for j in range(len(times)):

            Z = np.random.normal(loc=0)
            k1 = h*F(Y0, t0, Z)
            k2 = h*F(Y0 + k1, t0 + h*j, Z)

            Y = Y0 + 0.5*(k1 + k2)
            Y0 = Y
            t0 = t0 + h*j

            Y_list.append(Y)

        return np.array(Y_list)


plt.figure(figsize=(7,7))
plt.plot(times, Integrator.RK2(F,Y0,t0,h)[:,1], color="red", label="Particle velocity")
plt.plot(times, Integrator.RK2(F,Y0,t0,h)[:,0], label = "Particle x-position")
plt.grid(True)
plt.xlabel("Time")
plt.legend()
plt.show()

