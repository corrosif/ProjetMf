import numpy as np
import matplotlib.pyplot as plt



def mouvement_brownien(T,Nmc):
	W,t=[0],[0]
	for i in range(Nmc):
		t.append(t[i]+T/Nmc)
		W.append(W[i]+np.sqrt(T/Nmc)*np.random.normal())
	return t,W
def affichage_mouvement():
	t,W=mouvement_brownien(2,1000000)
	plt.plot(t,W)
	plt.show()
	return 1
print(affichage_mouvement())
