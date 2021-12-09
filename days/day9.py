#!/usr/bin/env python3.8
import time, math
start_time = time.time()
with open('../files/day9.txt') as file:
    data = [[*map(int, str(line).strip())] for line in file]
# print(data)

# list_data = [[*map(int,x)] for x in data]
# print(list_data)
# print(data)
# print(data[0])
# print(data[0][0])
low_list = []

for x in range(len(data)):
    for y in range(len(data[0])):
        first_element = data[x][y]
        # Take all adjecent elements for this iteration and check if it is within the scope.
        adjacent_element = [k for k in [[x - 1, y], [x + 1, y], [x, y + 1], [x, y - 1]] if len(data) > k[0] > -1 and len(data[0]) > k[1] > -1]
        # Take out single adjacents to prep for compare.
        adjacents = [data[k[0]][k[1]] for k in adjacent_element]
        lowest_element = sum([1 for x in adjacents if x <= first_element])

        if lowest_element == 0:
            low_list += [[x,y]]

result_one = sum([data[k[0]][k[1]] for k in low_list]) + len(low_list)
basins = []

for x,y in low_list:
    # Kinda bruteforced this motherfucker aswell... Not even using brainz.. P.S FEJKI would like this
    first_element = data[x][y]
    if first_element != 9:
        checking = [[x , y]]
        done_checking = []
        while len(checking) > 0:
            l = checking[0]
            checking = checking[1:]
            # This is not clean what so ever... but it works..
            adjacent_element = [k for k in [[l[0] - 1, l[1]], [l[0] + 1, l[1]], [l[0], l[1] - 1], [l[0], l[1] + 1]] if len(data) > k[0] > -1 and len(data[0]) > k[1] > -1]
            adjacents = [k for k in adjacent_element if data[k[0]][k[1]] != 9]
            checking += adjacents
            # This is hella ugly
            data[l[0]][l[1]] = 9
            done_checking += [f"{l[0]}_{l[1]}"]
        basins += [len(set(done_checking))]

result_two =  math.prod(sorted(basins, reverse=True)[:3])


# print(sum([x[1] for x in low_list]))



print("--- Part One:", result_one, " ---")
print("--- Part Two:", result_two, " ---")
print("Execution time: {:.2f}".format((time.time() - start_time)* 1000), "ms")