# Redéfinition des variables et fonctions nécessaires pour appliquer la fonction DOMINO
import matplotlib.pyplot as plt
import numpy as np
import copy

# Paramètres initiaux
N = 10  # nb de banque
R = 0.05  # taux de recouvrement
C = [10]*N  # matrice des seuils critiques
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

# Fonction DOMINO
def Domino(X_T, D_sol, D_T):
    D = copy.deepcopy(D_sol)
    D_faillite = copy.deepcopy(D_T)
    A = set(D_faillite)
    for i in D:
        if X_T[i] <= C[i]:
            D_sol.remove(i)  # Liste des banques solvables
            D_T.append(i)  # Liste des banques en faillite
    B = set(D_T)
    D_nouvelle_faillite = B - A
    for i in D_sol:  # Banques solvables
        somme = 0
        for j in D_nouvelle_faillite:  # Banques en faillite pour la vague
            somme += E[i][j]
        X_T[i] -= (1 - R) * somme  # Perte de capital
    return [X_T, D_sol, D_T]

# Fonction pour appliquer la cascade de faillites et trouver la stabilité
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

# Capitaux finaux obtenus précédemment
capitaux_finaux = [20.72, 10.36, 19.97, 9.29, 29.90, 22.35, 13.20, 15.69, 15.46, 15.33]

# Initialisation des listes de banques solvables et en faillite
D_sol_start = [i for i in range(N)]
D_T_start = []

# Application de la fonction Chute_Domino
X_finale, D_sol_finale, D_T_finale, nombre_etapes = Chute_Domino(capitaux_finaux, D_sol_start, D_T_start)

# Résultats
print("Capitaux finaux : ",X_finale)
print("Banque solvable : ", D_sol_finale)
print("Banque en faillite : ", D_T_finale)
print("Nombre d'étape : ", nombre_etapes)