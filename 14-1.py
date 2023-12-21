#advent of code day 14
import time
import csv
import os
from functools import lru_cache

start_time = time.time()

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

inputs = []
with open(os.path.join(__location__, "2023 Inputs/input-14-1.txt"),newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter='\n')
    for row in reader:
        inputs.append(row)

time_s = time.time() - start_time
        
def swapRowCol(inputs):
    inCols = list(map(list, zip(*inputs)))

    return inCols

inputs = [x[0] for x in inputs]
swappedIn = swapRowCol(inputs)

def bubbleSort(column):
    n = len(column)

    for i in range(n):
        for j in range(0, n - i - 1):
            if column[j] == '.' and column[j + 1] == 'O':
                column[j], column[j + 1] = column[j + 1], column[j]

    return column

#Part 1
for ind, column in enumerate(swappedIn):
    column = bubbleSort(column)
    column = ''.join(column)
    swappedIn[ind] = column

pushedIn = swapRowCol(swappedIn)

total = 0
for ind, row in enumerate(pushedIn):
    circleCount = row.count('O')
    total += circleCount * (len(pushedIn)-ind)

time_p1 = time.time() - start_time - time_s
print("The solution to Part 1 is {} which took {:.4f} seconds to run".format(total, time_p1))

#Part 2
#at each step, pick which is getting sorted, row or column, and which direction
@lru_cache
def north(inputs):
    #inputs is regular row, col grid
    #swap rows and cols, bubble sort to left, swap rows/cols back
    swappedIn = swapRowCol(inputs)
    for ind, column in enumerate(swappedIn):
        column = bubbleSort(column)
        column = ''.join(column)
        swappedIn[ind] = column

    endIn = swapRowCol(swappedIn)
    for ind, row in enumerate(endIn):
        row = ''.join(row)
        endIn[ind] = row

    return tuple(endIn)

@lru_cache
def west(inputs):
    #takes inputs as row, col grid
    #just bubble sorts everything to the left
    inputs = list(inputs)
    for ind, column in enumerate(inputs):
        column = list(column)
        column = bubbleSort(column)
        column = ''.join(column)
        inputs[ind] = column

    return tuple(inputs)

def bubbleSortRev(column):
    n = len(column)

    for i in range(n):
        for j in range(0, n - i - 1):
            if column[j] == 'O' and column[j + 1] == '.':
                column[j], column[j + 1] = column[j + 1], column[j]

    return column

@lru_cache
def south(inputs):
    #takes inputs as row, col grid
    #swap rows and cols, bubble sort to the right, swap rows/cols back
    swappedIn = swapRowCol(inputs)

    for ind, column in enumerate(swappedIn):
        column = bubbleSortRev(column)
        column = ''.join(column)
        swappedIn[ind] = column

    endIn = swapRowCol(swappedIn)
    for ind, row in enumerate(endIn):
        row = ''.join(row)
        endIn[ind] = row

    return tuple(endIn)

@lru_cache
def east(inputs):
    #takes inputs as row, col grid
    #just bubble sorts everything to the right
    inputs = list(inputs)
    for ind, column in enumerate(inputs):
        column = list(column)
        column = bubbleSortRev(column)
        column = ''.join(column)
        inputs[ind] = column

    return tuple(inputs)

origInputs = inputs
inputs = tuple(inputs)
hist = []
for i in range(1000000000):
    current = ''.join(inputs)
    if current in hist:
        cycle = i - hist.index(current)
        f = (1000000000 - hist.index(current)) % cycle + hist.index(current)
        break
    else:
        hist.append(current)
        inputs = north(inputs)
        inputs = west(inputs)
        inputs = south(inputs)
        inputs = east(inputs)

print("The cycle repeats itself starting at i = {} every {} cycles".format(hist.index(current),cycle))
lastCycle = hist[f]         #was using f-1 for some reason, should just be f
splitN = len(origInputs[0])
newInputs = [lastCycle[i:i+splitN] for i in range(0, len(lastCycle), splitN)]

total = 0
for ind, row in enumerate(newInputs):
    circleCount = row.count('O')
    total += circleCount * (len(newInputs)-ind)

time_p2 = time.time() - start_time - time_p1
print("The solution to Part 2 is {} which took {:.4f} seconds to run".format(total, time_p2))



