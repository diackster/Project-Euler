import numpy as np


def find_multiples(n):
    multiples = []
    for i in range(n):
        if i % 3 == 0 or i % 5 == 0:
            multiples.append(i)
    return np.sum(multiples)


print(find_multiples(1000))