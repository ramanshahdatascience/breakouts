#! /usr/bin/env python


import csv
from sys import argv

BREAKOUT_SIZE = int(argv[2])
ROUNDS = int(argv[3])

def round_robin_plan(i, j, k):
    return   

with open(argv[1], 'r') as pf:
    reader = csv.reader(pf)
    # Header
    next(reader)

    names = [line[0] for line in reader]

# Ceiling division to compute the number of breakouts
num_breakouts = -(-len(names) // BREAKOUT_SIZE)

padded_size = BREAKOUT_SIZE * num_breakouts

for i in range(ROUNDS):
    print('# Breakout Session {}'.format(i + 1))
    print()
    for j in range(num_breakouts):
        print('## Breakout Room {}'.format(j + 1))
        print()
        for k in range(BREAKOUT_SIZE):
            print('- {}'.format(names[j * BREAKOUT_SIZE + k]))
        print()
    if i < ROUNDS - 1:
        print('\\pagebreak')
        print()
