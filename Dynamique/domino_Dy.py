import matplotlib.pyplot as plt
import numpy as np
import copy
N=5 #nb de banque
R=0.05 #taux de recouvrement
C=[10]*N  #matrice des seuils critiques
X_start=[14,9,8,13,15]#[14,15,11,9,12,12,13,14,15,12]#[20,9,20,9,25,20,12,14,15,13]#[15,9,8,18,12]#[12,9,11,13,12]#
D_sol_start=[i for i in range(N)]
D_T_start=[]
 #matrice des etats du réseau
'''
E=[
	[0,3,0,0,6,0,3,2,4,0],
	[3,0,0,0,0,6,5,0,4,2],
	[3,3,0,0,0,6,5,3,2,1],
	[2,2,2,0,2,0,4,0,6,0],
	[0,2,3,3,0,5,0,2,3,0],
	[0,0,6,0,2,0,0,3,0,0],
	[3,0,4,0,0,0,0,0,0,6],
	[0,3,0,4,0,6,0,0,3,1],
	[2,0,0,3,0,4,6,0,0,3],
	[0,2,0,3,0,2,0,2,3,0],]
'''
E=[
	[0,3,0,0,6],
	[3,0,0,0,0],
	[3,3,0,0,0],
	[2,2,2,0,2],
	[0,2,3,3,0],
]


def Domino(X_T:list,D_sol:list,D_T:list)->list:
	D=copy.deepcopy(D_sol)
	D_faillite=copy.deepcopy(D_T)
	A=set(D_faillite)
	for i in D:
		if X_T[i]<=C[i]:#X_T[i]!= None or 
			D_sol.remove(i)	#méthode pour calculer la liste des banques solvables
			D_T.append(i) #méthode pour calculer la liste des banques en faillites
	B=set(D_T)
	D_nouvelle_faillite=B-A	
	for i in D_sol:			#on se balade dans les banques solvables
		somme=0
		for j in D_nouvelle_faillite:     #on se balade dans les banques en faillites pour la vague
			somme+=E[i][j]	#on calcul a chaque fois l'impact de la faillite a chaque banque en defaut
		X_T[i]-=(1-R)*somme  #on fait perdre le capital aux banques restantes 
	return X_T,D_sol,D_T
#print(Domino([9,15,15,15,15],[0,1,2,3,4],[]))
def Chute_Domino(X_T:list,D_sol:list,D_T:list)->list: #a partir du jeux de base j'ai besoin de connaitre le nombre d'etape avant la faillite, stabilite du systeme
	test=False
	q=-1
	while not test:
		q+=1
		X=copy.deepcopy(D_sol)
		X_1,D_sol_1,D_T_1=Domino(X_T,D_sol,D_T)
		#print([X_1,D_sol_1,D_T_1])
		if len(D_sol_1)==0 or D_sol_1==X:
			test=True
	return X_1,D_sol_1,D_T_1
	
#print(Chute_Domino([9,15,15,15,15],[0,1,2,3,4],[]))
def suppresseur(X,seuil):
	elements_a_supprimer=[]  # Liste temporaire pour stocker les éléments à supprimer
	for x in range(len(X)):
		if X[x] == None or X[x] < seuil:
			elements_a_supprimer.append(x)
	for i in range(len(X)):
		if i in elements_a_supprimer:
			X[i] = None
	return X

#print(suppresseur(X_start,10))

def X_T_None(X_start,D_sol_1,D_T_1):	#->X_T_None
	X_2,D_sol_2,D_T_2=Chute_Domino(X_start,D_sol_1,D_T_1)
	X_T_None=suppresseur(X_2,10)
	return X_T_None
X_start=[9,15,15,15,15]
print(X_T_None(X_start,[0,1,2,3,4],[]))
	












	

