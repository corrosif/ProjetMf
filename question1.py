import numpy as np
import matplotlib.pyplot as plt



def mouvement_brownien(T,Nmc):
	W=[0]
	for i in range(Nmc):
		W.append(W[i]+np.sqrt(T/Nmc)*np.random.normal())
	return W
print(mouvement_brownien(2,100000))
