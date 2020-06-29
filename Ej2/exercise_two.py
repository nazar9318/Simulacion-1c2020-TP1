import random
import matplotlib.pyplot as plt
from itertools import islice 
import numpy as np

#Ejercicio 1
def modulo(x):
    modulo = 2**32
    multiplicador = 1013904223
    incremento = 1664525
    return (x*multiplicador + incremento) % modulo


def random_generator(cantidad):
    numeros = []
    x = 96102
    for i in range(cantidad):
        numeros.insert(i, modulo(x)/(2.0**32))
        x = modulo(x)
    return numeros

def get_dice_number(x):
    if (x <= 0.16):
        return 1
    elif(x <= 0.33):
        return 2
    elif(x <= 0.5):
        return 3
    elif(x <= 0.66):
        return 4
    elif(x <= 0.83):
        return 5
    else:
        return 6

def register_dice(number,dices):
    dices[number] = dices[number] + 1

def exercise_two():
    quantity = 10000
    releases = {}
    dices = {1:0,2:0,3:0,4:0,5:0,6:0}
    randoms = random_generator(quantity)
    for x in range(0,quantity,2):
        dice_1 = get_dice_number(randoms[x])
        dice_2 = get_dice_number(randoms[x+1])
        register_dice(dice_1,dices)
        register_dice(dice_2,dices)
        suma = dice_1 + dice_2
        print("suma  {}".format(suma))
        if suma in releases:
            releases[suma] = releases[suma] + 1
        else:
            releases[suma] = 1
    return (dices,releases)


(dices,releases) = exercise_two()
print("releases:"+str(releases))
keys = list(releases.keys())
keys.sort()
print("keys:"+str(keys))
values = list(map(lambda key: releases[key],keys))
print("values:"+str(values))


plt.bar([str(i) for i in keys], values, color='g')
plt.show()
