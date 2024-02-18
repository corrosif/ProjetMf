import numpy as np
import matplotlib.pyplot as plt



Lambda=20
Mu=15
Sigma=8
T=1
Nmc=100000
dt=T/Nmc
X0=X1=X2=15
X3=X4=X5=12
Lambda_e=10
Sigma_e=3



def cov(p,Nmc):
	A=np.full((Nmc,Nmc),p)
	I=np.eye(Nmc)*(p-1)
	cov=A-I
	return cov



def Cholesky(A,Nmc):
	L=[[0]*Nmc for _ in range(Nmc)]
	for i in range(Nmc):
		for j in range(i+1):
			sum=0
			for k in range(j+1):
				sum+=L[i][k]*L[j][k]
			if i==j:
				L[i][i]=np.sqrt(A[i][i]-sum)
			else:
				L[i][j]=(1/L[j][j])*(A[i][j]-sum)
	return L

#print(Cholesky(cov(0.2,2),2))



def marche_correlee(p,N):
	matrice_cov=cov(p,N)
	M=Cholesky(matrice_cov,N)
	t=np.linspace(0,T,Nmc)
	y=[]
	dt=T/Nmc
	for k in range(N):
		X=[X0] #initialisation du marche alea
		for i in range(1,Nmc):
			bt=np.sqrt(dt)*np.random.normal(size=(N,)) #on initialise un vecteur de mvt bro
			s=M[k] @ bt
			X.append(X[i-1]*(np.exp(-Lambda*dt))+Mu*(1-np.exp(-Lambda*dt))+Sigma*s) #on itere en ajoutant la somme du mvt bro
		y.append(X) #on recupere la marche
		X=[] #on vide la liste pour repartir sur une liste vide

	plt.figure(figsize=(10, 6))
	for k in range(N):
		plt.plot(t,y[k])
	plt.show()
	return 1
	
print(marche_correlee(0,2))
			
			
			
			
			
			
			
			
	
	
