def count_div(n):
    count = 0
    divisors = [1, n]
    for i in range(2, n//2+1):
        if n % i == 0:
            divisors.append(i)
            while
            count+=1
    return count+2
n = 1
m = 1
l = count_div(n)
while l < 7:
    print(n, l)
    m += 1
    n += m
    l = count_div(n)

print(n, l)