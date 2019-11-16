import numpy as np

x = np.arange(100,1000)
y = np.arange(100,1000)
z = np.outer(x, y).reshape((1,810000))

print(z)

palindromes = []

for i in np.nditer(z):
#   print(i)
    if i not in palindromes:
        if str(i)[::-1] == str(i):
            palindromes.append(i)
#            print(i)

print(np.max(palindromes))




