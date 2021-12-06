from collections import defaultdict
import time
start_time = time.time()

with open('../files/day6.txt') as file:
    data = [list(map(int, line.split(','))) for line in file]
data = data[0]

dict_of_data = defaultdict(int)
dict_of_data_two = defaultdict(int)
for x in data:
    dict_of_data[x] += 1
    # Gjorde absolut inte precis en kekkeMANG
    dict_of_data_two[x] += 1

def lanternfish(dict, days):
    for k in range(0, days):
        # Antalet nollor som existerar vid första läsningen.
        nr_of_zeros = dict[0]
        for l in range(1, 9):
            dict[l - 1] = dict[l]
            # minskar alla element i dictonaryn.
        # sätter alla 0:or till 6:0r + skapar nya barn
        dict[6] += nr_of_zeros
        dict[8] = nr_of_zeros
    return dict


print("--- Part One:", sum(lanternfish(dict_of_data, 80).values()), " ---")
print("--- Part Two:", sum(lanternfish(dict_of_data_two, 256).values()), " ---")
print("Execution time: {:.2f}".format((time.time() - start_time)* 1000), "ms")