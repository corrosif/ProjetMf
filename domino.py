import matplotlib.pyplot as plt
import numpy as np
import copy

N=5 #nb de banque
R=0.05 #taux de recouvrement
condition_intiale = [15]*N  # liste capital initial
C=[10]*N  #matrice des seuils critiques
X_start=[14,9,8,13,15]#[15,9,8,18,12][12,9,11,13,12]
D_sol_start=[i for i in range(N)]
D_T_start=[]

E=[
	[0,3,0,0,6],
	[3,0,0,0,0],
	[3,3,0,0,0],
	[2,2,2,0,2],
	[0,2,3,3,0],
] #matrice des etats du réseau 

#E*[1,1,1,1,1]=[9,3,6,8,8]


def Domino(X_T:list,D_sol:list,D_T:list)->list:
	D=copy.deepcopy(D_sol)
	D_faillite=copy.deepcopy(D_T)
	A=set(D_faillite)
	for i in D:
		if X_T[i]<=C[i]:
			D_sol.remove(i)	#méthode pour calculer la liste des banques solvables
			D_T.append(i) #méthode pour calculer la liste des banques en faillites
	B=set(D_T)
	D_nouvelle_faillite=B-A	
	for i in D_sol:			#on se balade dans les banques solvables
		somme=0
		for j in D_nouvelle_faillite:     #on se balade dans les banques en faillites pour la vague
			somme+=E[i][j]	#on calcul a chaque fois l'impact de la faillite a chaque banque en defaut
		X_T[i]-=(1-R)*somme  #on fait perdre le capital aux banques restantes 
	
	return [X_T,D_sol,D_T]

print(Domino(X_start,D_sol_start,D_T_start))
X_T_0=Domino(X_start,D_sol_start,D_T_start)[0]
D_sol_0=Domino(X_start,D_sol_start,D_T_start)[1]
D_T_0=Domino(X_start,D_sol_start,D_T_start)[2]

print(Domino(X_T_0,D_sol_0,D_T_0))

