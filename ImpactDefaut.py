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
Nmc=1000

def X_T(X_start):	#on part de la matrice des conditions initales puis on les fait maturer via les marches multiple de fluctuation.py
	X_T_multi=fl.multi_marche(X_start)
	X_T=[]
	for i in range(N):
		X_T.append(X_T_multi[i][-1])
	return X_T
#print(X_T(X_start))


def Impact(X_start)->int: #calcul le cout financier de la chute du systeme en inpout je prends X_start
	X_T_resultat=X_T(X_start)
	I,L=0,0
	X_j=copy.deepcopy(X_T_resultat)
	X_1,D_sol_1,D_T_1,q=dm.Chute_Domino(X_T_resultat,D_sol_start,D_T_start)
	for j in D_T_1:
		I+=X_j[j]
		for p in D_sol_1:
			L+=(1-R)*E[p][j]
	return I+L
#print(Impact(X_start))

def IndexRisqueSys(X_start): #calcul l'index du risque systemique
	last_value=[]
	for i in range(Nmc):
		last_value.append(Impact(X_start))
	esperance=np.mean(last_value)
	return esperance
print(IndexRisqueSys(X_start))
'''
def I_S(n): #permet d'obtenir n valeur de l'index du risque systemique
	I_S=[]
	for i in range(n):
		I_S.append(IndexRisqueSys(33))
	return I_S	

B=[20.163646959883557, 10.267890611516941, 7.785582836953691, 18.167942914134443, 16.871456217092398, 14.20566702572045, 17.77589476564855, 11.868159706375286, 19.55247696013851, 20.030923384995603, 16.512993999560685, 20.500724035318825, 12.432854691274775, 15.439356716489508, 14.404535928942085, 18.40003829262897, 16.82885733883171, 18.54698273008267, 18.558589153248025, 12.403189108514347, 20.465317336316424, 15.449326035447825, 14.473518757321518, 18.09570385260563, 25.005536266860897, 17.151081363462744, 17.909239545674446, 19.83384065164643, 15.264436803920546, 15.88814062271336]
print(I_S(50))

	

def affichage(n): #affiche le cout de la chute
	for i in range(n):
		A = fl.multi_marche(condition_intiale) 
		X_T=[A[i][-1] for i in range(len(A))]
		print(Impact(X_T))
	return 1
'''


