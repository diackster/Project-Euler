import time
primes_list = []


def is_prime(n):
    prime = True
    for x in primes_list:
        if x > (n ** 0.5 + 1):
            break
        else:
            if n % x == 0:
                prime = False
                break
    if prime:
        primes_list.append(n)
    return prime

def primes(target):
    sum = 0
    for x in range(2,target):
        if is_prime(x):
#            print(x)
            sum+=x
    return sum
start = time.time()
print(primes(2000000))
end = time.time()
print(end - start)