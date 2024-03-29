import matplotlib.pyplot as plt
import numpy as np
import random as rd
from scipy.stats import norm #uniquement pour tester mes algo de var et cvar avec des valeurs theo

import fluctuation as fl

import densiteRepartion as dr

A=[20.163646959883557, 10.267890611516941, 7.785582836953691, 18.167942914134443, 16.871456217092398, 14.20566702572045, 17.77589476564855, 11.868159706375286, 19.55247696013851, 20.030923384995603, 16.512993999560685, 20.500724035318825, 12.432854691274775, 15.439356716489508, 14.404535928942085, 18.40003829262897, 16.82885733883171, 18.54698273008267, 18.558589153248025, 12.403189108514347, 20.465317336316424, 15.449326035447825, 14.473518757321518, 18.09570385260563, 25.005536266860897, 17.151081363462744, 17.909239545674446, 19.83384065164643, 15.264436803920546, 15.88814062271336]       #liste des Is
N=np.random.normal(0,1,100000) #me permet de tester mes algo 

def Var(X,a): # calcul la Var ie P(X(t)<=VAR)=alpha
	t,repartion=dr.fonction_de_repartition(X,1000)
	index=next(i for i, val in enumerate(repartion) if val >= a)
	return index,t[index]
print(Var(N,0.001)) #precision satifaisante

def produit(A,B):
	return [a*b for a,b in zip(A,B)]

def CVar(X,a): #E[L|L>=Var] ou L=-X
	t,densite=dr.fonction_densite(X,1000)
	index,t[index]=Var(X,a)
	Y=densite[:index]
	t=t[:index]
	moyenne=-sum(produit(Y,t))/a
	ppf=norm.ppf(a,0,1)
	pdf=norm.pdf(ppf,0,1)
	theo=pdf/a
	return moyenne,theo


#pour une loi normal on a CVaR CVaR(X,a)=-nu+sigma*(pdf(cdf(a))/a
#print(CVar(N,0.05)) #test




