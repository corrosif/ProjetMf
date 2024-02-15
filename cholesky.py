import numpy as np



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

print(Cholesky(cov(0.2,6),6))
