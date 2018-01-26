#!/usr/bin/env python
# Envoyer via github sur FAAtp1


import numpy as np
import matplotlib
import matplotlib.pyplot as plt
# np.random.uniform(borne inférieure, borne supérieure, dimensions)



a=[np.random.uniform(0,1),np.random.uniform(0,1)]
b=[np.random.uniform(0,1),np.random.uniform(0,1)]
plt.plot(a,b, 'r-', lw=2)
#pointsx = [20]
#pointsy = [20]
#valeur = []
ax = a[0]
ay = a[1]
bx = b[0]
by = b[1]

d = np.random.uniform(-1,1,40).reshape((20,2))

for i in range(0,20):
    y = d[:,1][i]
    x = d[:,0][i]


    #xp = v1[0]*v2[1] - v1[1]*v2[0]
    xp = ((x - ax)*(by - ay)) - ((y - ay)*(bx - ax))
    if xp > 0:
        plt.scatter(x,y, c="blue")
    else:
        plt.scatter(x,y, c="green")

#for i in range(0,20):
#    if (d[:,1][i] - (a * d[:,0][i] + b ) < 0):
#        plt.scatter(d[:,0][i],d[:,1][i],"bo")
#    else:
 #       plt.scatter(d[:,0][i],d[:,1][i],"ro")


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
