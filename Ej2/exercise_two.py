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

def is_zero_or_one(x):
    if x <= 0.5:
        return 0
    return 1

def get_dice_number_in_binary(elements):
    return str(is_zero_or_one(elements[0]))+str(is_zero_or_one(elements[1]))+str(is_zero_or_one(elements[2]))

def get_dice_number(elements):
    binary_string = get_dice_number_in_binary(elements)
    return (int(binary_string,2) % 6) + 1


def exercise_two():
    quantity = 10000
    releases = {}
    randoms = random_generator(quantity*3)
    for x in range(0,quantity*3,6):
        sub_list = randoms[x:x+6]
        sub_list_1 = sub_list[3:]
        sub_list_2 = sub_list[:3]
        dice_1 = get_dice_number(sub_list_1)
        dice_2 = get_dice_number(sub_list_2)
        print("dice_1 {} dice_2 {}".format(dice_1,dice_2))
        suma = dice_1 + dice_2
        print("suma  {}".format(suma))
        if suma in releases:
            releases[suma] = releases[suma] + 1
        else:
            releases[suma] = 1
    return releases
 
releases = exercise_two()
print("releases:"+str(releases))


plt.bar([str(i) for i in releases.keys()], releases.values(), color='g')
plt.show()
