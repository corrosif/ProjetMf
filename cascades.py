import matplotlib.pyplot as plt
import numpy as np
import random as rd

import fluctuation as fl #biblio perso


N=5

condition_intiale = [10, 12, 15, 18, 20]  # liste capital initial
A = fl.multi_marche(condition_intiale) #je recupere la matrice de fluctuation du capital des banques
X_T=[A[i][-1] for i in range(len(A))] #je recupere la matrice du capital a la maturité
W_T=[18,8,22,56,8]
C=[10,10,10,10,10]  #matrice des seuils critiques

E=[
	[0,3,0,0,6],
	[3,0,0,0,0],
	[3,3,0,0,0],
	[2,2,2,0,2],
	[0,2,3,3,0],
] #matrice des etats du réseau 



#je pars du principe que R est fixé a R=0.2 pour implementer l'algo
N=5

D=[]
D.append([i for i in range(N) if W_T[i]<=C[i]])
D.append(D[-1]+[i for i in range(N) if i not in D[0]])


print(D[0],D[1])
