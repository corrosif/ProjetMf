import matplotlib.pyplot as plt
import numpy as np
import copy
import fluctuation as fl
import domino as dm
import densiteRepartion as dr
#dataset de mon exo reutilisant les anciens scripts 
R=0.05
N=dm.N
C=[10]*N
E=dm.E
X_start=dm.X_start
D_sol_start=[i for i in range(N)]
D_T_start=[]
Nmc2=10000

def Impact(X_init)->int: #calcul le cout financier de la chute du systeme en inpout je prends X_start
	I,L=0,0
	X_j=copy.deepcopy(X_init)
	X_1,D_sol_1,D_T_1,q=dm.Chute_Domino(X_init,D_sol_start,D_T_start)
	for j in D_T_1:
		I+=X_j[j]
		for p in D_sol_1:
			L+=(1-R)*E[p][j]
	return I+L
#print(Impact(X_start))
def IndexRisqueSys(X_init): #calcul l'index du risque systemique
	last_value=[]
	for i in range(Nmc2):
		last_value.append(Impact(X_init))
	esperance=np.mean(last_value)
	return esperance
#print(IndexRisqueSys(X_start))

def I_S(n,X_init): #permet d'obtenir n valeur d'impact
	I_S=[]
	for i in range(n):
		I_S.append(Impact(X_init))
	return I_S	
#print(I_S(500,X_start))

	
'''
def affichage(n): #affiche le cout de la chute
	for i in range(n):
		A = fl.multi_marche(condition_intiale) 
		X_T=[A[i][-1] for i in range(len(A))]
		print(Impact(X_T))
	return 1
	
def X_T(X_init):	#on part de la matrice des conditions initales puis on les fait maturer via les marches multiple de fluctuation.py
	X_T_multi=fl.multi_marche(X_start)
	X_T=[]
	for i in range(N):
		X_T.append(X_T_multi[i][-1])
	return X_T
#print(X_T(X_start))

'''

