import matplotlib.pyplot as plt
import numpy as np
import random as rd

import fluctuation as fl #biblio perso

N=5 #nb de banque
condition_intiale = [15]*N  # liste capital initial
A = fl.multi_marche(condition_intiale) #je recupere la matrice de fluctuation du capital des banques
X_T=[A[i][-1] for i in range(len(A))] #je recupere la matrice du capital a la maturité
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

def cascade(k,X_T): #cascade permet de retourner la liste des banques ayant fait faillite a l'intant q,T
	N=5
	R=0.4
	if k==0:
		return [i for i in range(N) if X_T[i]<=C[i]]
	else:
		return cascade(k-1,X_T)+[j for j in range(N) if j not in cascade(k-1,X_T) and X_T[j]-(1-R)*sum(E[j])<=C[j]]


def liste_cascade(n): #permet d'obtenir une liste de liste des banques faisant faillite
	liste_cascade=[]
	for i in range(n):
		A = fl.multi_marche(condition_intiale) 
		X_T=[A[i][-1] for i in range(len(A))] #permet de generer different scenario de faillite
		liste_cascade.append(cascade(N,X_T)) #N car je veux l'etat final
	return liste_cascade

	
