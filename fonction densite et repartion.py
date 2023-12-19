import matplotlib.pyplot as plt
import numpy as np
import random as rd

N=np.random.normal(0,1,10000) #me permet de tester mes algo 

def fonction_densite(X,Nt):
	dt=(max(X)-min(X))/Nt
	proba=[]
	densite=[]
	t=[]
	for i in range(Nt):
		t.append(min(X)+i*dt)
		counter=sum(1 for n in X if t[i]<=n<=t[i]+dt)
		proba.append(counter/len(X))
		densite.append(proba[i]/dt)
	return t,densite

#print(fonction_densite(N,1000))

def fonction_de_repartition(X,Nt):
	t,Y=fonction_densite(X,Nt)
	somme=sum(i for i in Y)
	repartition= np.cumsum(Y)/somme
	return t,repartition
	

#print(fonction_de_repartition(N,1000))

