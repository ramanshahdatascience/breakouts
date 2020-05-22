#! /usr/bin/env python3


from functools import reduce
from operator import add
import requests

def symbols(line):
    words = line.split()
    if len(words) > 0:
        return sorted(reduce(add, line.split()))
    else:
        return []


r = requests.get('http://www.mathpuzzle.com/MAA/54-Golf%20Tournaments/golferlist.txt')
lines = r.text.splitlines()

# Process this compendium of Social Golfer Problem exact solutions by searching
# for contiguous blocks of lines made of the same symbols.
solution_start_idx = 0
while solution_start_idx < (len(lines) - 1):
    solution_end_idx = solution_start_idx + 1
    solution_symbols = symbols(lines[solution_start_idx])
    while solution_end_idx < len(lines) \
        and symbols(lines[solution_end_idx]) == solution_symbols \
        and len(lines[solution_start_idx].split()) == len(lines[solution_end_idx].split()):
        solution_end_idx += 1
    if (solution_end_idx - solution_start_idx) > 1 and len(solution_symbols) > 0:
        solution = lines[solution_start_idx:solution_end_idx]

        individuals = len(solution_symbols)
        groups = len(solution[0].split())
        people_per_group = individuals // groups
        weeks = len(solution)

        g_p_w_spec = '{:}-{:}-{:}'.format(groups, people_per_group, weeks)

        with open(g_p_w_spec + '.txt', 'w') as solution_file:
            solution_file.write('\n'.join(solution))
            solution_file.write('\n')

    solution_start_idx = solution_end_idx
