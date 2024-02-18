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

#print(Cholesky(cov(0.2,2),2))

def correlation(p,Nmc):
	T=1
	bt=np.sqrt(T)*np.random.normal(size=(Nmc,))
	M=Cholesky(cov(p,Nmc),Nmc)
	w=[]
	s=0
	for i in range(Nmc):
		for j in range(i):
			s+=M[i][j]
		w.append(s*bt[i])
	return w
	
print(correlation(0.3,2))
