def checkabc(a,b,c):
    if (a + b + c == 1000):
        print(a,b,c)
        if (a**2+b**2 == c**2):
            return True
        else:
            return False
    else:
        return False
found = False
for c in range(1,1000):
    if found:
        break
    for b in range(1, c):
        if found:
            break
        for a in range(1, b):
            if checkabc(a,b,c):
                print(a*b*c)
                found = True
                break
