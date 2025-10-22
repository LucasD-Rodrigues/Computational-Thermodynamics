import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams

rcParams.update({
    "text.usetex": True,
    "font.family": "serif",  # or 'sans-serif' for a modern look
    "font.serif": ["Computer Modern Roman"],  # default LaTeX font
    "axes.labelsize": 16,    # LaTeX font size
    "font.size": 15,
    "legend.fontsize": 15,
    "xtick.labelsize": 16,
    "ytick.labelsize": 16
})

V = np.linspace(1,20,1000)
a =  1.370
b = 0.0387
R = 8.314
n = 5

class Isotherms:
    def __init__(self,temperature):
        self.T = temperature
    def P(self, V, n): 
        return  n*R*self.T/(V-n*b) - (a*n**2)/V**2

T1 = Isotherms(300)
T2 = Isotherms(500)
T3 = Isotherms(700)

plt.figure(figsize=(6,6))
plt.plot(V, np.array([T1.P(v, n) for v in V]),color="orange", label=r"$T_{1}$")
plt.plot(V, np.array([T2.P(v, n) for v in V]),color="green", label=r"$T_{2}$")
plt.plot(V, np.array([T3.P(v, n) for v in V]), label=r"$T_{3}$")
plt.xlabel(r"$V$ (L)")
plt.ylabel(r"$P$ (atm)")
plt.grid(True)
plt.legend()
plt.show()
