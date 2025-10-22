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


a =  1.370
b = 0.0387
T = 300
n = np.linspace(1,100,1000)
R = 8.314
V = 10

P_vw = lambda n: n*R*T/(V-n*b) - (a*n**2)/V**2
P_ideal = lambda n: n*R*T/V

P_list1 = np.array([P_vw(N) for N in n])
P_list2 = np.array([P_ideal(N) for N in n])

plt.figure(figsize=(6,6))
plt.plot(n,P_list1, label=r"Gás de Van der Waals")
plt.plot(n,P_list2, color="red",label=r"Gás ideal")
plt.grid(True)
plt.legend()
plt.title(r"Diagrama $P \times N$")
plt.ylabel(r"$P$ (Pa)")
plt.xlabel(r"$N$ (número de moles)")
plt.show()
