#!/usr/bin/env python
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import math
import numpy.core as np 


pisobre2 = math.pi/2.0

#Defino funcion
def f2(x):
    return 13.0*x/(12.0*math.pi) - (x**3)/(3.0*math.pi**3) +(1.0/2.0)

#Defino limites
x1 = np.linspace(-3.0, -pisobre2)
x2 = np.linspace(-pisobre2, pisobre2)
x3 = np.linspace(pisobre2, 3.0)

#Armo el gráfico
plt.plot(x1, [0.0 for x in x1], 'm',  label='y = 2, x en [-oo, -pi/2]')
plt.plot(x2, [f2(i) for i in x2], 'm', label='y = 13/(12*pi) - (x**2)/pi**3, x en [-pi/2, pi/2]')
plt.plot(x3, [1 for x in x3], 'm', label='y = 0, x en (pi/2, oo]')


# Limitar los valores de los ejes.
plt.ylim(-0.1,1.1 )
plt.xlim(-3.0,3.0 )
# Muestro.
plt.grid()
plt.show()


