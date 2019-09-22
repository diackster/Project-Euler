import random
batch = 1
envelope = []
single = 0

def cut(l):
    buf = []
    while l != 1:
        buf.append(l/2)
        l /= 2
    return buf

def find_a5(l):
    if l == 1:
        return []
    else:
        return cut(l)

def get_rand_list(envelope):
    return envelope.pop(random.randint(0,len(envelope)-1))
iterations = 50000000
def run(iterations):
    global single, envelope
    for i in range(iterations):
        if i % 10000 == 0:
            print(i)
#            print(single / (i+1))
        envelope = [16]
        for j in range(16):
                if len(envelope) == 1 and envelope[0] != 16 and envelope[0] != 1:
                    single += 1
                envelope += find_a5(get_rand_list(envelope))

run(iterations)
print(single/iterations)
