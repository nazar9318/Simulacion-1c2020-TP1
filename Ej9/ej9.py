import numpy as np
import random as rnd
import matplotlib.pyplot as plt

CANTIDAD_DE_MOVIMIENTOS = 300 #cantidad de pasos de cada particula
CANTIDAD_DE_PARTICULAS = 1000 #cantidad de particulas de cada color
ALTO_DE_LA_CAJA = 200
ANCHO_DE_LA_CAJA = 100

def ej9():

  matriz_particulas_amarillas=crear_matriz(0, 49) #genera todas las posiciones de todas las partículas a la izq (azules)
  matriz_particulas_rojas=crear_matriz(50, 100) #genera todas las posiciones de todas las partículas a la der (rojas)
  
  d1_izq=calcular_densidad(matriz_particulas_amarillas, 0, 49)
  d1_der=calcular_densidad(matriz_particulas_amarillas, 50, 100)
  d2_izq=calcular_densidad(matriz_particulas_rojas, 0, 49)
  d2_der=calcular_densidad(matriz_particulas_rojas, 50, 100)

  tiempo=np.arange(300)

  plt.subplot(221)
  plt.plot(tiempo,d1_izq/CANTIDAD_DE_PARTICULAS, '.') #cantidad de azules a la izq
  plt.subplot(222)
  plt.plot(tiempo,d1_der/CANTIDAD_DE_PARTICULAS, '.') #cantidad de azules a la der
  plt.subplot(223)
  plt.plot(tiempo,d2_izq/CANTIDAD_DE_PARTICULAS, '.') #cantidad de rojos a la izq
  plt.subplot(224)
  plt.plot(tiempo,d2_der/CANTIDAD_DE_PARTICULAS, '.') #cantidad de rojos a la der
  plt.show()

  """plt.axis([0, 100, 0, 200])
  for a in range (0, M-1): #loop de instantes de tiempo
    for b in range (0,2*N-2, 2):
      plt.plot(matriz_particulas_amarillas
  [a][b], matriz_particulas_amarillas
  [a][b+1], 'b.') #plotea todos los puntos azules
    for c in range (0,2*N-2, 2):
      plt.plot(matriz_particulas_rojas[a][c], matriz_particulas_rojas[a][c+1], 'r.') #plotea todos los puntos rojos
    plt.show()"""

def calcular_densidad(A, limite_x_inferior, limite_x_superior):

  contador=np.zeros(CANTIDAD_DE_MOVIMIENTOS)
  for a in range (0, CANTIDAD_DE_MOVIMIENTOS): #loop de instantes de tiempo
      for b in range (0,(2*CANTIDAD_DE_PARTICULAS-1), 2):
        if (A[a][b]>=limite_x_inferior and A[a][b]<=limite_x_superior):
          contador[a]=contador[a]+1
  
  return contador

def particula_puede_moverse_a_la_izquierda(A,i,z):
  #Si esta en la parte superior de la caja   
  if A[i][z+1] >= ALTO_DE_LA_CAJA / 2 :
    return A[i-1][z]-1 > ANCHO_DE_LA_CAJA / 2
  return True

def particular_puede_mover_a_la_derecha(A,i,z):
  if A[i][z+1] >= ALTO_DE_LA_CAJA / 2 :
    return A[i-1][z]+1 < ANCHO_DE_LA_CAJA / 2
  return True


def crear_matriz(limite_x_inferior, limite_x_superior): #N cantidad de particulas
  A=np.zeros((CANTIDAD_DE_MOVIMIENTOS, 2*CANTIDAD_DE_PARTICULAS))

  for z in range (0,2*CANTIDAD_DE_PARTICULAS-1, 2): #z numero de columna, este for asigna el valor inicial de cada particula y los siguientes 
    #Posicion inicial en X
    A[0][z]=rnd.randint(limite_x_inferior, limite_x_superior) #elige al azar la posicion incial 
    #Posicion inicial en Y 
    A[0][z+1]=rnd.randint(0, ALTO_DE_LA_CAJA)
    r=np.random.random(CANTIDAD_DE_MOVIMIENTOS)
    
    for i in range (1,CANTIDAD_DE_MOVIMIENTOS): #simula todos los movimientos de una particula desde el segundo instante de tiempo
        if (r[i]<=0.25 and A[i-1][z+1] < ALTO_DE_LA_CAJA):
          A[i][z+1]=A[i-1][z+1]+1 #que se mueva hacia arriba
          A[i][z]=A[i-1][z] 
        elif (r[i]>0.25 and r[i]<=0.5 and A[i-1][z+1] > 0):
          A[i][z+1]=A[i-1][z+1]-1 #que se mueva hacia abajo
          A[i][z]=A[i-1][z]
        elif (r[i]>0.5 and r[i]<=0.75 and A[i-1][z] > 0):
          A[i][z]=A[i-1][z]-1 #que se mueva hacia la izquierda
          A[i][z+1]=A[i-1][z+1]
        elif (r[i]>0.75 and A[i-1][z] < ANCHO_DE_LA_CAJA):
          A[i][z]=A[i-1][z]+1 #que se mueva hacia la derecha
          A[i][z+1]=A[i-1][z+1]
        else:
          A[i][z]=A[i-1][z]
          A[i][z+1]=A[i-1][z+1]
  return A

ej9()
