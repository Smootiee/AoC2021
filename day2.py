with open("files/day2.txt") as file:
    data = [str(line) for line in file]

horiz_pos = 0
depth = 0


for x in data:
    x = x.rstrip("\n")
    if x.startswith('forward'):
        horiz_pos = int(horiz_pos) + int(x[-1])
    elif x.startswith('down'):
        depth = int(depth) + int(x[-1])
    elif x.startswith('up'):
        depth = int(depth) - int(x[-1])

print(horiz_pos, depth)
result = horiz_pos * depth

print(result)