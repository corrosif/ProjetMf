import matplotlib.pyplot as plt
import numpy as np
import random as rd



Lambda=20
Mu=15
Sigma=8
T=1
Nmc=100000
dt=T/Nmc
N=5
X0=X1=X2=15
X3=X4=X5=12

def marche(X0):
	X=[X0]
	t=[0]
	for i in range(Nmc):
		t.append(t[i]+dt)
		X.append(X[i]*(np.exp(-Lambda*dt))+Mu*(1-np.exp(-Lambda*dt))+Sigma*np.sqrt(dt)*np.random.normal())
	return t,X
#print(marche(15))

def affichage(n):
	for _ in range(n):
		t,X=marche(15)
		plt.plot(t,X)
	plt.show()
	return 1
#print(affichage(10))


def multi_marche(condition_intiale):
	A=[]
	for x in condition_intiale:
		t,X=marche(x)
		A.append(X)
	return A
#print(multi_marche([15,15,15,15,15]))

def affichage_multi(condition_intiale):
	A=multi_marche(condition_intiale)
	t=[i*T/Nmc for i in range(Nmc+1)]
	for j in range(len(A)):
		plt.plot(t,A[j])
	plt.show()
	return 1
	
#print(affichage_multi([15,15,15,15,15]))
'''j'ai ici le moyen d'avoir la matrice de fluctuation du capital de la banque'''

	

	
	
	
	
	
	
	
	
	
	
