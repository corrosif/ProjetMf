import matplotlib.pyplot as plt
import numpy as np
import copy


N = 10  # nb banques
T = 1  
n = 12  # nb mois
dt = T / n 
sigma = 0.1 
R = 0.05
X_start = np.array([20, 9, 20, 9, 25, 20, 12, 14, 15, 13])  # capital initial banques

np.random.seed(0)  # pour la reproductibilité
capitaux_fin = np.zeros((N, n+1))
capitaux_fin[:, 0] = X_start

for t in range(1, n+1):
    dW = np.random.normal(0, np.sqrt(dt), N)  # mvtm brownien
    capitaux_fin[:, t] = capitaux_fin[:, t-1] + R * capitaux_fin[:, t-1] * dt + sigma * capitaux_fin[:, t-1] * dW

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


C = [10]*N  # matrice des seuils critiques
X_start = [20.72, 10.36, 19.97, 9.29, 29.90, 22.35, 13.20, 15.69, 15.46, 15.33] # on reprend les valeurs d'avant
E = [
    [0,3,0,0,6,0,3,2,4,0],
    [3,0,0,0,0,6,5,0,4,2],
    [3,3,0,0,0,6,5,3,2,1],
    [2,2,2,0,2,0,4,0,6,0],
    [0,2,3,3,0,5,0,2,3,0],
    [0,0,6,0,2,0,0,3,0,0],
    [3,0,4,0,0,0,0,0,0,6],
    [0,3,0,4,0,6,0,0,3,1],
    [2,0,0,3,0,4,6,0,0,3],
    [0,2,0,3,0,2,0,2,3,0],
]


def Domino(X_T, D_sol, D_T):
    D = copy.deepcopy(D_sol)
    D_faillite = copy.deepcopy(D_T)
    A = set(D_faillite)
    for i in D:
        if X_T[i] <= C[i]:
            D_sol.remove(i)  
            D_T.append(i)  
    B = set(D_T)
    D_nouvelle_faillite = B - A
    for i in D_sol:  
        somme = 0
        for j in D_nouvelle_faillite: 
            somme += E[i][j]
        X_T[i] -= (1 - R) * somme  
    return [X_T, D_sol, D_T]

def Chute_Domino(X_T, D_sol, D_T):
    test = False
    q = -1
    while not test:
        q += 1
        X = copy.deepcopy(D_sol)
        [X_1, D_sol_1, D_T_1] = Domino(X_T, D_sol, D_T)
        if len(D_sol_1) == 0 or D_sol_1 == X:
            test = True
    return X_1, D_sol_1, D_T_1, q


np.random.seed(0)  
Nmc = 1000
compteur_ruinees = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}

for _ in range(Nmc):
    capitaux_fin = np.zeros((N, n+1))
    capitaux_fin[:, 0] = X_start
    for t in range(1, n+1):
        dW = np.random.normal(0, np.sqrt(dt), N) 
        capitaux_fin[:, t] = capitaux_fin[:, t-1] + R * capitaux_fin[:, t-1] * (dt) + 0.1 * capitaux_fin[:, t-1] * dW
    
    _, D_sol_finale, D_T_finale, _ = Chute_Domino(capitaux_fin[:, -1].tolist(), [i for i in range(N)], [])
    
    nb_ruinees = len(D_T_finale)
    
    if 1 <= nb_ruinees <= 5: # mise à jour du compteur si le nombre de ruinées est entre 1 et 5
        compteur_ruinees[nb_ruinees] += 1

probabilites_ruinees = {k: v / Nmc for k, v in compteur_ruinees.items()}

print(probabilites_ruinees)
