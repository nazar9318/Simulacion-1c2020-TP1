import random
import matplotlib.pyplot as plt


#import func of exercise one
def random_fun():
    return random.uniform(0,1)


def is_zero_or_one():
    if random_fun() <= 0.5:
        return 0
    return 1

def get_dice_number_in_binary():
    return str(is_zero_or_one())+str(is_zero_or_one())+str(is_zero_or_one())

def get_dice_number():
    binary_string = get_dice_number_in_binary()
    return int(binary_string,2) % 6 + 1


def exercise_two():
    releases = {}
    for x in range(10000):
        key  = int(str(get_dice_number())+ str(get_dice_number()))
        if key in releases:
            current = releases[key]
            releases[key] = current + 1
        else:
            releases[key] = 1
    return releases


releases = exercise_two()
print("releases:"+str(releases))


#plt.bar([str(i) for i in releases.keys()], releases.values(), color='g')
#plt.show()
