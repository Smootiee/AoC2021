import time
start_time = time.time()

with open('../files/day7.txt') as file:
    data = [list(map(int, line.split(','))) for line in file]
data = data[0]

result = min([sum(abs(x - n) for n in data) for x in range(max(data))])
result_two = min([sum(abs(x - n) * (abs(x - n) + 1) // 2 for n in data) for x in range(max(data))])

print("--- Part One:", result, " ---")
print("--- Part Two:", result_two, " ---")
print("Execution time: {:.2f}".format((time.time() - start_time)* 1000), "ms")
