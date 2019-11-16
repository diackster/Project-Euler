import numpy as np


def get_largest_prime(n):
    primes = []
    i = 2
    # i = n // 2
    # while n % i !=0:
    #     i += -1
    # while True:
    #     if n % i == 0:
    #         print(i)
    #         i = int(n / i)
    #         print(i)
    #     if i > n // 2:
    #         break
    #     i += 1
    for i in range(2, n // 2):
#        print(i)
        if n % i == 0:
            primes.append(i)
            n = int(n / i)
#            print(i)
            print(primes)
    return i


print(get_largest_prime(600851475143))