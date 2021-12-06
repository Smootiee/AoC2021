import time
start_time = time.time()

with open("../files/day2.txt") as file:
    data = [str(line).rstrip() for line in file]

horiz_pos = 0
depth = 0
aim = 0


for x in data:
    if x[0:-2] == 'forward':
        horiz_pos += int(x[-1])
        aim += (depth * int(x[-1]))
    elif x[0:-2] == 'down':
        depth += int(x[-1])
    elif x[0:-2] == 'up':
        depth -= int(x[-1])


print("--- Part One:",horiz_pos * depth, " ---")
print("--- Part Two:",horiz_pos * aim, " ---")
print("Execution time: {:.2f}".format((time.time() - start_time)* 1000), "ms")