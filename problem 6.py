import numpy as np


def sum_of_squares(n):
    a = np.arange(1,n+1)
    return np.array(a * a).sum()

def square_of_sums(n):
    a = np.arange(1,n+1)
    return a.sum() ** 2


print(sum_of_squares(100))
print(square_of_sums(100))
print(square_of_sums(100)-sum_of_squares(100))