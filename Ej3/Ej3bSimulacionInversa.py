#!/usr/bin/env python
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import math
from scipy import interpolate

#Defino funcion de distribucion
def f2(x):
    if(x< (-math.pi/2.0) ):
        return 0
    elif( x>(math.pi/2.0) ):
        return 1
    else:
        return 13.0*x/(12.0*math.pi) - (x**3)/(3.0*math.pi**3) +(1.0/2.0)

#armo la inversa a partir de los puntos y luego invirtiendo los ejes
yv = [-2.0,-1.9,-1.8,-1.7,-1.6,-1.5,-1.4,-1.3,-1.2,-1.1,-1.0,-0.9,-0.8,-0.7,-0.6,-0.5,-0.4,-0.3,-0.2,-0.1,0.0,
0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0,1.1,1.2,1.3,1.4,1.5,1.6,1.7,1.8,1.9,2.0]
xv = []

for i in yv:
    print ('x: ' + str(i) + ' y: ' + str(round(f2(i),2)))
    xv.append(round(f2(i),2))
    
print(xv)   

plt.plot(xv, yv, 'm')

# Limitar los valores de los ejes.
plt.xlim(-0.1,1.1 )
plt.ylim(-2.0,2.0 )


# Muestro.
plt.grid()
plt.show()


