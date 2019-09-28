r = range(2,21)
result = 2
for x in r:
    if (result % x != 0):
        for y in range(2,x+1):
            if (result * y) % x == 0:
                result *= y
                break

print(result)
