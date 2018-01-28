#!/usr/bin/env python
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

a=np.random.uniform(-1,1,2)
b=np.random.uniform(-1,1,2)
plt.plot(a,b, 'r-', lw=2)
# le problème venait de la mauvaise compréhension du fonctionnement de plot : ici a contient les x et b les y, et non pas a[0] = x et a[1] = y
ax = a[0]
bx = a[1]
ay = b[0]
by = b[1]

d = np.random.uniform(-1,1,40).reshape((20,2))

for i in range(0,20):
    y = d[:,1][i]
    x = d[:,0][i]
    xp = ((x - ax)*(by - ay)) - ((y - ay)*(bx - ax))
    if xp > 0:
        plt.scatter(x,y, c="blue")
    else:
        plt.scatter(x,y, c="green")
plt.show()
