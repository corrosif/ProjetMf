import matplotlib.pyplot as plt
import numpy as np

import fluctuation as fl
from domino as dm
import densiteRepartion as dr


def Q1(): #dois retourner la proba que la banque 1,2...5 fasse faillite
	proba=[0,0,0,0,0]
	#A=
	for cascade in A:
			proba[len(cascade)]+=1/len(A) #on va calculer la taille de la faillite
	return proba
print(Q1())

					
PROBA=[0.03, 0.0, 0.12, 0.42, 0.48] # pour 100 valeurs

PROBA2=[0.022, 0.008, 0.166, 0.432, 0.454] # pour 500 valeurs "il s'agit de la proba que la n eme banque fasse faillite"

'''
Objectifs.
 Estimation de la probabilité que le nombre de banques insolvables soit 1, 2, 3, 4 ou 5 est :
[0.325, 0.45, 0.2125, 0.0125, 0.0]
'''

