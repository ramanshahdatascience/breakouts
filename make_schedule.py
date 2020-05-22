#! /usr/bin/env python3


import csv
from functools import reduce
import glob
from operator import add
from sys import argv

BREAKOUT_SIZE = int(argv[2])
ROUNDS = int(argv[3])

def make_translator(indices):
    def translator(cyphertext):
        return [indices[c] for c in cyphertext]

    return translator

with open(argv[1], 'r') as pf:
    reader = csv.reader(pf)
    # Header
    next(reader)

    names = [line[0] for line in reader]

# Ceiling division to compute the number of breakouts
num_breakouts = -(-len(names) // BREAKOUT_SIZE)

padded_size = BREAKOUT_SIZE * num_breakouts

solution_files = glob.glob('{:}-{:}-*.txt'.format(num_breakouts, BREAKOUT_SIZE))
if len(solution_files) == 0:
    raise(Exception('Cannot find a solution for {:}-{:}-x'.format(num_breakouts, BREAKOUT_SIZE)))
with open(solution_files[0], 'r') as sf:
    rounds = [round.split() for round in sf]
# Make the last round's indices sequential. That makes the schedule nicer to
# use for uneven numbers of individuals. Say you schedule 19 people into
# threesomes. You can use the (7-3-10) solution of the SGP by padding the 19
# people at the end with two vacancies. Labeling the schedule this way means
# that you can have 9 rounds in which there are at least two people in each
# group: the two vacancies only meet each other in the 10th round.
symbols = reduce(add, rounds[-1])
indices = {s: i for i, s in enumerate(symbols)}
translator = make_translator(indices)
schedule = [list(map(translator, rd)) for rd in rounds]

# Render schedule in Pandoc Markdown
for i in range(ROUNDS):
    print('# Breakout Session {}'.format(i + 1))
    print()
    for j in range(num_breakouts):
        print('## Breakout Room {}'.format(j + 1))
        print()
        for k in range(BREAKOUT_SIZE):
            idx = schedule[i][j][k]
            if idx < len(names):
                # Omit vacancies from the schedule writeup
                print('- {}'.format(names[idx]))
        print()
    if i < ROUNDS - 1:
        print('\\pagebreak')
        print()
