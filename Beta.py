import matplotlib.pyplot as plt
import numpy as np
import densiteRepartion as DR

Nmc=10000

def Beta(a,b):
	y=[]
	x=np.linspace(0,1,Nmc)
	for i in range(Nmc):
		u=np.random.uniform(low=0.00000001,high=1.0)
		v=np.random.uniform(low=0.00000001,high=1.0)
		while u**(1/a)+v**(1/b)>1:
			u=np.random.uniform(low=0.00000001,high=1.0)
			v=np.random.uniform(low=0.00000001,high=1.0)
		y.append((u**(1/a))/(u**(1/a)+v**(1/b)))
	return y

#print(Beta(0.5,0.5))
def affichage(a,b,Nmx):
	y=Beta(a,b)
	t,densite=DR.fonction_densite(y,Nmx)
	plt.plot(t,densite)
	plt.show()
	return 1


print(affichage(0.5,0.5,1000))
