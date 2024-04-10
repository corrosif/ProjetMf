import matplotlib.pyplot as plt
import numpy as np
import copy
import fluctuation_Dy as fl
import domino_Dy as dm
import densiteRepartion as dr
import ImpactDefaut_Dy as Id

N=dm.N
X_start=dm.X_start
B=fl.multi_marche(X_start)		#on recupere la matrice des fluctuations du capital input X_0->X_T
C=dm.C  #matrice des seuils critiques
D_sol_start=dm.D_sol_start
D_T_start=dm.D_T_start
T=fl.T
Nmc=1000
t=np.linspace(0,T,Nmc)
dt=T/Nmc

def suppresseur(X,seuil):
	elements_a_supprimer = []  # Liste temporaire pour stocker les éléments à supprimer
	for x in X:
		if x < seuil:
			elements_a_supprimer.append(x)

    # Supprimer les éléments de la liste X
	for element in elements_a_supprimer:
		X.remove(element)
	return X
#print(suppresseur(X_start,10))
def Impact_dynamique(X_start):
	l=N;L=1
	X_T=X_start
	D_T=[]
	D_sol=[i for i  in range(l)]
	cout=0
	for i in range(L):
		drapeau=True
		Y=X_T.copy()
		print(Y)
		for n in range(len(X_T)):
			#print('1',X_T)
			if Y[n]<=10 or drapeau:
				X_T,D_sol,D_T=dm.Domino(X_T,D_sol,D_T)
				#print('2',X_T),print(D_sol),print(D_T)
				print(D_sol)
				drapeau=False
				X_T=suppresseur(X_T,10)
		#print('3',X_T)
		X_T=fl.dX(X_T)
		#print('4',X_T)
		if len(X_T)==0:
			break
	#print(X_T),print(D_sol),print(D_T)
	print(X_T)
	cout=Id.Impact(X_T,[0,4],[1,2,3])
	return cout

print(Impact_dynamique(X_start))





								#on souhaite maintenant tester a chaque instant si domino s'applique


  
