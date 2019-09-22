def sum_even_fib(n):
    a, b = 1, 2
    sum = 0
    while b < n:
        c = a + b
        if b % 2 == 0:
            sum += b
        a = b
        b = c
    return sum

print(sum_even_fib(4e6))