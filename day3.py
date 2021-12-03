import time
start_time = time.time()

with open("files/day3.txt") as file:
    data = [str(line).rstrip() for line in file]

list_data = list(data)
list_one = []
binary_list = []
for j in range(len(list_data[0])):
    [list_one.append(i[j]) for i in list_data]
    if list_one.count('1') > list_one.count('0'):
        binary_list.append('1')
    else:
        binary_list.append('0')
    list_one = []

number_two = ''.join(map(str, binary_list))
bin_reverse = ''.join('1' if x == '0' else '0' for x in number_two)

power_consumption = int(bin_reverse, 2) * int(number_two, 2)
print("--- Part One:", int(bin_reverse, 2) * int(number_two, 2), " ---")
print("Execution time: {:.2f}".format((time.time() - start_time)* 1000), "ms")
