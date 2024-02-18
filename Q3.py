import numpy as np
import matplotlib.pyplot as plt

N = 10  # nb banques
T = 1  
n = 12  # nb mois
dt = T / n 
sigma = 0.1 
mu = 0.05
X_start = np.array([20, 9, 20, 9, 25, 20, 12, 14, 15, 13])  # capital initial banques

np.random.seed(0)  # pour la reproductibilité
capitaux_fin = np.zeros((N, n+1))
capitaux_fin[:, 0] = X_start

for t in range(1, n+1):
    dW = np.random.normal(0, np.sqrt(dt), N)  # mvtm brownien
    capitaux_fin[:, t] = capitaux_fin[:, t-1] + mu * capitaux_fin[:, t-1] * dt + sigma * capitaux_fin[:, t-1] * dW

# affichage
plt.figure(figsize=(10, 6))
for i in range(N):
    plt.plot(range(n+1), capitaux_fin[i], label=f'Bank {i+1}')

plt.title('Evolution des capitaux sur 12 mois')
plt.xlabel('Mois')
plt.ylabel('Capital')
plt.legend()
plt.grid(True)
plt.show()


for index, valeur in enumerate(capitaux_fin):
    print("Banque", index + 1, valeur[-1])
