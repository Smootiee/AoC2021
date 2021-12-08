import time
from itertools import permutations
start_time = time.time()

with open('../files/day8.txt') as file:
    data = [list(map(str,line.split('|')[1].strip().split())) for line in file]
with open('../files/day8.txt') as file:
    data_two = file.readlines()

sum_numbers = 0
result_one = sum([sum(1 for y in x if len(y) in [2,3,4,7]) for x in data])
#print(sum(1 for x in data if len(x) in [1,4,7,8]))
# print(result_one)
for x in data:
    for y in x:
        if len(y) in [2,3,4,7]:
            sum_numbers += 1
    # sum_numbers = len([len(x) if len(x) in (2,3,4,7)])
# print(sum_numbers)

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
        # print(two_test)
        if all(k in numbers for k in one_test):
            result_two += int(''.join(str(numbers[k]) for k in two_test))
            break

print("--- Part One:", result_one, " ---")
print("--- Part Two:", result_two, " ---")
print("Execution time: {:.2f}".format((time.time() - start_time)* 1000), "ms")









'''
  0:      1:      2:      3:      4:
 aaaa    ....    aaaa    aaaa    ....
b    c  .    c  .    c  .    c  b    c
b    c  .    c  .    c  .    c  b    c
 ....    ....    dddd    dddd    dddd
e    f  .    f  e    .  .    f  .    f
e    f  .    f  e    .  .    f  .    f
 gggg    ....    gggg    gggg    ....

  5:      6:      7:      8:      9:
 aaaa    aaaa    aaaa    aaaa    aaaa
b    .  b    .  .    c  b    c  b    c
b    .  b    .  .    c  b    c  b    c
 dddd    dddd    ....    dddd    dddd
.    f  e    f  .    f  e    f  .    f
.    f  e    f  .    f  e    f  .    f
 gggg    gggg    ....    gggg    gggg

'''