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
Lambda=20
Mu=15
Sigma=8
def suppresseur(X,seuil):
	elements_a_supprimer = []  # Liste temporaire pour stocker les éléments à supprimer
	for x in range(len(X)):
		if X[x] == None or X[x] < seuil:
			elements_a_supprimer.append(x)

	for i in range(len(X)):
		if i in elements_a_supprimer:
			X[i] = None
        
	return X

#print(suppresseur(X_start,10))
'''
def Impact_dynamique(X_start):
	l=N;L=1000
	X_T=X_start
	D_T=[]
	D_sol=[i for i  in range(l)]
	cout=0
	for i in range(L):
		drapeau=True
		Y=X_T.copy()
		for n in range(len(X_T)):
			if Y[n]<=10 or drapeau:
				X_T,D_sol,D_T=dm.Domino(X_T,D_sol,D_T)
				drapeau=False
				X_T=suppresseur(X_T,10)
		X_T=fl.dX(X_T)
		print(X_T)
		if len(X_T)==0:
			break
	cout=Id.Impact(X_T,D_sol,D_T)
	return cout
	
X_start=[9]*5	
print(Impact_dynamique(X_start))

def I_S(n,X_init): #permet d'obtenir n valeur d'impact
	I_S=[]
	for i in range(n):
		I_S.append(Impact_dynamique(X_init))
	return I_S
#print(I_S(500,X_start))'''
def marche(X0): 
    # Prepare the output list 
    X = [] 
    Nmc=1000 
    # Single time step for the entire simulation 
    dt = T / Nmc 
    
     
    # Perform the simulation for each initial value in the input vector 
    for x0 in X0: 
        if x0==None: 
            X.append(None) 
        if x0 is not None: 
            newX = x0*(np.exp(-Lambda*dt)) + Mu*(1-np.exp(-Lambda*dt)) + Sigma*np.sqrt(dt)*np.random.normal() 
            X.append(newX) 
    return X 
#print(marche( [9, 15, 12, 15, 15])) 
def impact_2(): 
    Nmc=1000 
    # Single time step for the entire simulation 
    dt = T / Nmc 
     
    V = [9, 15, 10.5, 15, 15] 
    for i in range(Nmc): 
        V = marche(V) 
        #print(V) 
        # Check if any value in V is less than 10 
        for i in range(len(V)): 
            if V[i]!=None: 
                if V[i]>10: 
                    V[i]=V[i]*(np.exp(-Lambda*dt)) + Mu*(1-np.exp(-Lambda*dt)) + Sigma*np.sqrt(dt)*np.random.normal() 
                if V[i]<10: 
                    V[i]=None 
        ''' 
        if any(v < 10 for v in V): 
            V = X_T_None(V,[0,1,2,3,4],[])''' 
    return V 
#impact_2() 
def MarcheUnitaire(X_T_0): 
    X_T=marche(X_T_0) 
    X_T_None1=X_T   
    for i in range(len(X_T)): 
        if X_T[i]!=None and X_T[i]<=10: 
            X_T_None1=dm.X_T_None(X_T,[0,1,2,3,4],[]) 
            break 
    return X_T_None1 
#print(MarcheUnitaire([9, 15, 10.5, 15, 15])) 
 
def MarcheFinale(Nmc,X_demarrage): 
    Y= [] 
    Y=MarcheUnitaire(X_demarrage) 
    for i in range(Nmc): 
        Y=MarcheUnitaire(Y) 
    return Y 
#print(MarcheFinale(1000,[9, 15, 10.5, 15, 15]))

def Impact_final(X_depart):
	Y=MarcheFinale(10000,X_depart)
	D_sol_depart=[i for i in range(N)]
	D_T_depart=[]
	cout=Id.Impact(X_depart,Y,D_sol_depart,D_T_depart)
	return cout
#print(Impact_final([15, 15, 15, 15, 15]))

def loup(X_depart,n):
	Y=[]
	for i in range(n):
		Y.append(Impact_final(X_depart))
	return Y
print(loup([15, 15, 15, 15, 15],20))




#print(Id.Impact([9, 15, 10.5, 15, 15],MarcheFinale(1000,[9, 15, 10.5, 15, 15]),[0,1,2,3,4],[]))






								#on souhaite maintenant tester a chaque instant si domino s'applique


  
