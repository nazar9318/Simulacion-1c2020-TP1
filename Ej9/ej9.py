import numpy as np
import random as rnd
import matplotlib.pyplot as plt

def ej9(): #M cantidad de partículas a generar
  M=30 #cantidad de pasos de cada partícula
  N=100 #cantidad de partículas
  A=np.zeros((M, 2*N))
  for z in range (2,2*N, 2): #z numero de columna, este for asigna el valor inicial de cada partícula y los siguientes 
    A[1][z]=rnd.randint(0, 100) #elige al azar la posición incial 
    A[1][z+1]=rnd.randint(0, 200)
    r=np.random.random(M)
    
    for i in range (2,M): #simula todos los movimientos de una partícula
      if (r(i)<=0.25):
        A[i][z+1]=A[i-1][z+1]+1 #que se mueva hacia arriba
        A[i][z]=A[i-1][z]
      elif (r(i)<=0.5):
        A[i][z]=A[i-1][z]+1 #que se mueva hacia abajo
        A[i][z+1]=A[i-1][z+1]
      elif (r(i)<=0.75):
        A[i][z+1]=A[i-1][z+1]-1 #que se mueva hacia la izquierda
        A[i][z]=A[i-1][z]
      else:
        A[i][z]=A[i-1][z]-1 #que se mueva hacia la derecha
        A[i][z+1]=A[i-1][z+1]
  

  for a in range (1, M):
    for b in range (1,2*N, 2):
      plt.axis([0, 100, 0, 200])
      plt.plot(A[a][b], A[a][b+1], 'b*')
    plt.show()

ej9()