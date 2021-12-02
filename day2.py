import time
start_time = time.time()

with open("files/day2.txt") as file:
    data = [str(line) for line in file]

horiz_pos = 0
depth = 0
aim = 0


for x in data:
    x = x.rstrip("\n")
    if x.startswith('forward'):
        horiz_pos = int(horiz_pos) + int(x[-1])
        aim = aim + (depth * int(x[-1]))
    elif x.startswith('down'):
        depth = int(depth) + int(x[-1])
    elif x.startswith('up'):
        depth = int(depth) - int(x[-1])

result_one = horiz_pos * depth
result_two = horiz_pos * aim

print("--- Part One:",result_one, " ---")
print("--- Part Two:",result_two, " ---")
print("Execution time: {:.2f}".format((time.time() - start_time)* 1000), "ms")