#!/usr/bin/env python3
import time
from classes.bingo import Bingo
start_time = time.time()

with open('../files/day4.txt') as f:
    numbers, *boards = f.read().rstrip().split('\n\n')

numbers = [int(numb) for numb in numbers.split(',')]
boards = [[line.split() for line in board.split('\n')] for board in boards]
boards = [[[int(elt) for elt in line] for line in board] for board in boards]
boards = [Bingo(board) for board in boards]

list_of_bingo = []

for numb in numbers:
    for x in range(len(boards) -1, -1, -1):
        boards[x].number_check(numb)
        if boards[x].win_condition():
            list_of_bingo.append(boards[x])
            boards.pop(x)


print("--- Part One:", list_of_bingo[0].score() * list_of_bingo[0].last_numb, " ---")
print("--- Part Two:", list_of_bingo[-1].score() * list_of_bingo[-1].last_numb, " ---")
print("Execution time: {:.2f}".format((time.time() - start_time)* 1000), "ms")