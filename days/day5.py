import time
start_time = time.time()

with open('../files/day5.txt') as file:
    data = [str(line.rstrip()) for line in file]


# Part 1
matrix_one = {}
for x in data:
    coord_a, coord_b = [[*map(int, k.split(","))] for k in x.split(" -> ")]
    coord_x = sorted([coord_a[0], coord_b[0]])
    coord_y = sorted([coord_a[1], coord_b[1]])

    X = Y = None

    if len(set(coord_y)) == 1:
        X = [*range(coord_x[0], coord_x[1] + 1)]
        Y = [coord_y[0]] * len(X)
    elif len(set(coord_x)) == 1:
        Y = [*range(coord_y[0], coord_y[1] + 1)]
        X = [coord_x[0]] * len(Y)

    if X and Y:
        for k, l in zip(X, Y):
            input = k * 1000 + l
            matrix_one[input] = matrix_one.get(input, 0) + 1


result_one = len([x for x in matrix_one.values() if x > 1])

# Part 2, just with diagonal matrix search aswell.
matrix_two = {}
for x in data:
    coord_a, coord_b = [[*map(int, k.split(","))] for k in x.split(" -> ")]
    coord_x = sorted([coord_a[0], coord_b[0]])
    coord_y = sorted([coord_a[1], coord_b[1]])

    X = Y = None

    if len(set(coord_y)) == 1:
        X = [*range(coord_x[0], coord_x[1] + 1)]
        Y = [coord_y[0]] * len(X)
    elif len(set(coord_x)) == 1:
        Y = [*range(coord_y[0], coord_y[1] + 1)]
        X = [coord_x[0]] * len(Y)
    elif coord_y[1] - coord_y[0] == coord_x[1] - coord_x[0]:
        k = 1 if coord_b[0] > coord_a[0] else -1
        l = 1 if coord_b[1] > coord_a[1] else -1
        X = [*range(coord_a[0], coord_b[0] + k, k)]
        Y = [*range(coord_a[1], coord_b[1] + l, l)]

    if X and Y:
        for k, l in zip(X, Y):
            input = k * 1000 + l
            matrix_two[input] = matrix_two.get(input, 0) + 1


result_two = len([x for x in matrix_two.values() if x > 1])


print("--- Part One:", result_one, " ---")
print("--- Part Two:", result_two, " ---")
print("Execution time: {:.2f}".format((time.time() - start_time)* 1000), "ms")