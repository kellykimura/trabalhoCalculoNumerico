import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("./data/Populacao_PresidentePrudente.dat")

year = data[:,0]
population = data[:,1]


plt.title("População de Pres. Prudente nos últimos 80 anos")
plt.xlabel("Ano")
plt.ylabel("População")
plt.plot(year, population)
plt.show()