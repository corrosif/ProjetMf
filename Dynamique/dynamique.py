import matplotlib.pyplot as plt
import numpy as np
import copy
import fluctuation as fl
import domino as dm
import densiteRepartion as dr

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








								#on souhaite maintenant tester a chaque instant si domino s'applique


  
