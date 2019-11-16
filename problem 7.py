def is_prime(n):
    prime = True
    for x in range(2,n+1):
        if n % x == 0 and n != x:
            prime = False
            break
    return prime

def primes(n):
    i = 1
    current = 2
    while i < n:
        current += 1
        while not is_prime(current):
            current += 1
        i += 1
    return current

print(primes(10001))