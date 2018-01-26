#!/usr/bin/env python
# Envoyer via github sur FAAtp1


import numpy as np
import matplotlib
import matplotlib.pyplot as plt
# np.random.uniform(borne inférieure, borne supérieure, dimensions)



a=[np.random.uniform(0,1),np.random.uniform(0,1)]
b=[np.random.uniform(0,1),np.random.uniform(0,1)]
plt.plot(a,b, 'r-', lw=2)
pointsx = [20]
pointsy = [20]
valeur = []

d = np.random.uniform(-1,1,40).reshape((20,2))

plt.scatter(d[:,0],d[:,1])

#for i in range(0,20):
#	pointsx[i]=[np.random.uniform(0,1)*100,np.random.uniform(0,1)*100]
#	pointsy[i]=[np.random.uniform(0,1)*100,np.random.uniform(0,1)*100]
#	if (pointsy[i] - (a * pointsx[i] + b ) < 0):
#		valeur[i] = -1
#	else:
#		valeur[i] = 1
#
#plt.scatter(pointsx,pointsy,s=100)

plt.show()
