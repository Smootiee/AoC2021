#!/usr/bin/env python3
import time
from itertools import permutations
start_time = time.time()

with open('../files/day8.txt') as file:
    data = [list(map(str,line.split('|')[1].strip().split())) for line in file]
with open('../files/day8.txt') as file:
    data_two = file.readlines()

result_one = sum([sum(1 for y in x if len(y) in [2,3,4,7]) for x in data])

# note to self, SKRIV FAN inte fel på 9an och tro det kommer gå bra då o köra...
numbers = {
    'abcefg': 0,
    'cf': 1,
    'acdeg': 2,
    'acdfg': 3,
    'bcdf': 4,
    'abdfg': 5,
    'abdefg': 6,
    'acf': 7,
    'abcdefg': 8,
    'abcdfg': 9,
}

result_two = 0

for x in data_two:
    one, two = x.split(' | ')
    one = one.split()
    two = two.split()

    for permut in permutations('abcdefg'):
        combinations = str.maketrans('abcdefg', ''.join(permut))
        one_test = [''.join(sorted(k.translate(combinations))) for k in one]
        two_test = [''.join(sorted(k.translate(combinations))) for k in two]

        if all(k in numbers for k in one_test):
            result_two += int(''.join(str(numbers[k]) for k in two_test))
            break

print("--- Part One:", result_one, " ---")
print("--- Part Two:", result_two, " ---")
print("Execution time: {:.2f}".format((time.time() - start_time)* 1000), "ms")
