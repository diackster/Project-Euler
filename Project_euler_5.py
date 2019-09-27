import numpy as np

def divisible(number):
    is_divisible = True
    factors = np.array([2,3,5,7,11,13,17,19,20])
    # for i in np.nditer(factors):
    #     if number%i != 0:\
    if np.array(number % factors).sum() > 0:
        is_divisible = False
    return is_divisible

number = 100000000
while not divisible(number):
    number += 1
    if number%1000000 == 0:
        print(number)

print(number)


