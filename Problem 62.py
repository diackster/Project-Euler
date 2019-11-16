from collections import Counter

limit = 10000
cubes = {}

def stringifier(n):
    return "".join(sorted(str(n)))

for i in range(333,limit):
    # if len(cubes[stringifier(i * i * i)]) == 0:
    #     cubes[stringifier(i * i * i)] = []

    try:
        cubes[stringifier(i * i * i)] += [i * i * i]
    except KeyError:
        cubes[stringifier(i * i * i)] = []
        cubes[stringifier(i * i * i)] += [i * i * i]
    if len(cubes[stringifier(i * i * i)]) == 5:
        print(cubes[stringifier(i * i * i)])

#print(cubes)







