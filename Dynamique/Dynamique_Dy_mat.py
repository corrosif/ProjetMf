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

def chute_dyna():
	for i in range Nmc:
		for n in N:
			
		
