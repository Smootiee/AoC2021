#!/usr/bin/env python3
import time
start_time = time.time()

with open("../files/day1.txt") as file:
    data = [int(line) for line in file]

inc_count = 0
inc_count_two = 0
numb = data[0]

# Part One:
for x in data:
    if numb < x:
        inc_count = inc_count + 1
    numb = x

numb_two = data[0] + data[1] + data[2]

# Part Two:
for y in range(0, len(data) - 2):
    if numb_two < data[y] + data[y + 1] + data[y + 2]:
        inc_count_two = inc_count_two + 1
    numb_two = data[y] + data[y + 1] + data[y + 2]

print("--- Part One:", inc_count, " ---")
print("--- Part Two:", inc_count_two, " ---")
print("Execution time: {:.2f}".format((time.time() - start_time)* 1000), "ms")

