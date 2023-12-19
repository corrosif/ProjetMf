import matplotlib.pyplot as plt
import numpy as np
import random as rd

import fluctuation as fl #biblio perso

N=5
condition_intiale = [15]*N  # liste capital initial
A = fl.multi_marche(condition_intiale) #je recupere la matrice de fluctuation du capital des banques
X_T=[A[i][-1] for i in range(len(A))] #je recupere la matrice du capital a la maturité
W_T=X_T
C=[10]*N  #matrice des seuils critiques

E=[
	[0,3,0,0,1],
	[3,0,0,0,0],
	[3,3,0,0,0],
	[2,2,2,0,2],
	[0,2,3,3,0],
] #matrice des etats du réseau 

#E*[1,1,1,1,1]=[9,3,6,8,8]

#je pars du principe que R est fixé a R=0.2 pour implementer l'algo

def cascade(k):
	N=5
	R=0.4
	if k==0:
		return [i for i in range(N) if W_T[i]<=C[i]]
	else:
		return cascade(k-1)+[j for j in range(N) if j not in cascade(k-1) and W_T[j]-(1-R)*sum(E[j])<=C[j]]
