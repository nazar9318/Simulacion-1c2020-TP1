import numpy as np
import random as rnd
import matplotlib.pyplot as plt

M=300 #cantidad de pasos de cada particula
N=1000 #cantidad de particulas de cada color

def ej9():

  A_1=crear_matriz(0, 49) #genera todas las posiciones de todas las partículas a la izq (azules)
  A_2=crear_matriz (50, 100) #genera todas las posiciones de todas las partículas a la der (rojas)
  
  d1_izq=calcular_densidad(A_1, 0, 49)
  d1_der=calcular_densidad(A_1, 50, 100)
  d2_izq=calcular_densidad(A_2, 0, 49)
  d2_der=calcular_densidad(A_2, 50, 100)

  tiempo=np.arange(300)

  plt.subplot(221)
  plt.plot(tiempo,d1_izq/N, '.') #cantidad de azules a la izq
  plt.subplot(222)
  plt.plot(tiempo,d1_der/N, '.') #cantidad de azules a la der
  plt.subplot(223)
  plt.plot(tiempo,d2_izq/N, '.') #cantidad de rojos a la izq
  plt.subplot(224)
  plt.plot(tiempo,d2_der/N, '.') #cantidad de rojos a la der
  plt.show()

  """plt.axis([0, 100, 0, 200])
  for a in range (0, M-1): #loop de instantes de tiempo
    for b in range (0,2*N-2, 2):
      plt.plot(A_1[a][b], A_1[a][b+1], 'b.') #plotea todos los puntos azules
    for c in range (0,2*N-2, 2):
      plt.plot(A_2[a][c], A_2[a][c+1], 'r.') #plotea todos los puntos rojos
    plt.show()"""

def calcular_densidad(A, limite_x_inferior, limite_x_superior):

  contador=np.zeros(M)
  for a in range (0, M): #loop de instantes de tiempo
      for b in range (0,(2*N-1), 2):
        if (A[a][b]>=limite_x_inferior and A[a][b]<=limite_x_superior):
          contador[a]=contador[a]+1
  
  return contador


def crear_matriz(limite_x_inferior, limite_x_superior): #N cantidad de particulas
  A=np.zeros((M, 2*N))

  for z in range (0,2*N-1, 2): #z numero de columna, este for asigna el valor inicial de cada particula y los siguientes 
    A[0][z]=rnd.randint(limite_x_inferior, limite_x_superior) #elige al azar la posicion incial 
    A[0][z+1]=rnd.randint(0, 200)
    r=np.random.random(M)
    
    for i in range (1,M): #simula todos los movimientos de una particula desde el segundo instante de tiempo
        if (r[i]<=0.25 and A[i-1][z+1]<200):
          A[i][z+1]=A[i-1][z+1]+1 #que se mueva hacia arriba
          A[i][z]=A[i-1][z]
        elif (r[i]>0.25 and r[i]<=0.5 and A[i-1][z+1]>0):
          A[i][z+1]=A[i-1][z+1]-1 #que se mueva hacia abajo
          A[i][z]=A[i-1][z]
        elif (r[i]>0.5 and r[i]<=0.75 and A[i-1][z]>0):
          A[i][z]=A[i-1][z]-1 #que se mueva hacia la izquierda
          A[i][z+1]=A[i-1][z+1]
        elif (r[i]>0.75 and A[i-1][z]<100):
          A[i][z]=A[i-1][z]+1 #que se mueva hacia la derecha
          A[i][z+1]=A[i-1][z+1]
        else:
          A[i][z]=A[i-1][z]
          A[i][z+1]=A[i-1][z+1]
  return A

ej9()
