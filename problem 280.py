import random
import numpy as np
# import matplotlib.pyplot as plt
from multiprocessing import Process, Manager
from datetime import datetime, timedelta


class grid:
    def __init__(self):
        self.upper = [False, False, False, False, False]
        self.lower = [True, True, True, True, True]


class ant:
    def __init__(self):
        self.position = [2, 2]
        self.seed = False
        self.moves = 0

    def get_move(self):
        if self.position[0] == 0 and self.position[1] == 0:
            move = random.choice(['R', 'D'])
        elif self.position[0] == 4 and self.position[1] == 0:
            move = random.choice(['U', 'R'])
        elif self.position[0] == 0 and self.position[1] == 4:
            move = random.choice(['L', 'D'])
        elif self.position[0] == 4 and self.position[1] == 4:
            move = random.choice(['U', 'L'])
        elif self.position[0] == 0:
            move = random.choice(['L', 'R', 'D'])
        elif self.position[1] == 0:
            move = random.choice(['U', 'R', 'D'])
        elif self.position[0] == 4:
            move = random.choice(['L', 'U', 'R'])
        elif self.position[1] == 4:
            move = random.choice(['U', 'L', 'D'])
        else:
            move = random.choice(['U', 'R', 'D', 'L'])

        return move

    def move(self):
        move = self.get_move()
        if move == 'U':
            self.position[0] -= 1
        if move == 'R':
            self.position[1] += 1
        if move == 'D':
            self.position[0] += 1
        if move == 'L':
            self.position[1] -= 1

        self.moves += 1


def ant_run(ant, grid):
    while False in grid.upper:

        ant.move()

        if ant.position[0] == 4 and ant.seed == False and grid.lower[ant.position[1]] == True:
            ant.seed = True
            grid.lower[ant.position[1]] = False

        if ant.position[0] == 0 and ant.seed == True and grid.upper[ant.position[1]] == False:
            grid.upper[ant.position[1]] = True
            ant.seed = False

    return ant.moves


def ant_runner(l, num):
    for i in range(num):
        grid1 = grid()
        ant1 = ant()
        l.append(ant_run(ant1, grid1))


#        if len(l) % 1000 == 0:
#            print(f'Move number: {len(l)}, mean: {np.mean(l)}')


L = []
df_speed = 3000

def run(procs_num, runs):
    if __name__ == "__main__":
        with Manager() as manager:
            L = manager.list()  # <-- can be shared between processes.
            processes = []
            start = datetime.now()
            plan = start + timedelta(0,procs_num*runs/df_speed)
            print(f'Launched {procs_num} processes at {start.time()} for {runs} each. Planned end: {plan.time()}')
            for i in range(procs_num):
                p = Process(target=ant_runner, args=(L, runs))  # Passing the list
                p.start()
                processes.append(p)
            for p in processes:
                p.join()
            end = datetime.now()
            delta = end - start
#            print(delta.seconds)
#            print(len(L))
            print(f'Finished {len(L)/delta.seconds} iter/sec at {end.time()} Mean value: {np.mean(L)}')

#run(1,15000)
#run(2,7500)
run(4,10000)