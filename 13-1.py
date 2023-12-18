#advent of code day 12
import time
import csv
import os
import numpy as np

start_time = time.time()

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

inputs = []
with open(os.path.join(__location__, "input-13-1.txt"),newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter='\n')
    ground = []
    for row in reader:
        if row:
            ground.append(row)
        else:
            inputs.append(ground)
            ground = []    
    inputs.append(ground)

def searchRow(puzzleRow):
    #puzzle is a list of strings where each string is a row in the puzzle
    #reflect has to have something on both sides so pointers start at 1
    center = 0

    possible = []
    while center < len(puzzleRow) - 1:
        match = True
        for ind in range(0,min((len(puzzleRow) - (center + 1)), center + 1)):
            if puzzleRow[center - ind] == puzzleRow[center + ind + 1] and match != False:
                match = True
                point = center
            else:
                match = False
                point = None
        if point is not None:
            possible.append(point)
        center += 1

    return possible
       
def searchCol(puzzle):
    #takes in full puzzle
    #creates column arrays
    #performs searchRow in column
    puzzle = [x[0] for x in puzzle]
    puzzleCols = list(map(list, zip(*puzzle)))

    possibleCol = []
    for col in puzzleCols:
        possibleCol.append(searchRow(col))

    #For Part 2 only
    counterCol = np.zeros(len(puzzle))
    for x in range(len(puzzle)):
        for y in range(len(possibleCol)):
            if x in possibleCol[y]:
                counterCol[x] += 1

    newCol = 0
    for val in counterCol:
        if val == len(puzzle[0]) - 1:
            newCol = np.where(counterCol == val)[0] + 1

    return set(possibleCol[0]).intersection(*possibleCol), newCol

time_s = time.time() - start_time

#Part 1
total = 0
for puzzle in inputs:
    possibleRow = []
    for row in puzzle:
        possibleRow.append(searchRow(row[0]))
    if set(possibleRow[0]).intersection(*possibleRow):
        total += list(set(possibleRow[0]).intersection(*possibleRow))[0] + 1
    elif searchCol(puzzle)[0]:
        total += (list(searchCol(puzzle)[0])[0] + 1) * 100

time_p1 = time.time() - start_time - time_s
print("The solution to Part 1 is {} which took {:.4f} seconds to run".format(total, time_p1))

#Part 2
#instead of swapping the smudge and trying again
#identify rows/cols where it was 1 off from correct
#use those as new rows/cols for reflection
total = 0
for puzzle in inputs:
    possibleRow = []
    for row in puzzle:
        possibleRow.append(searchRow(row[0]))
    counterRow = np.zeros(len(puzzle[0][0]))
    for x in range(len(puzzle[0][0])-1):
        for y in range(len(possibleRow)):
            if x in possibleRow[y]:
                counterRow[x] += 1
    for val in counterRow:
        if val == len(puzzle) - 1:
            total += np.where(counterRow == val)[0] + 1
    possibleCol, newCol = searchCol(puzzle)
    if newCol != 0:
        total += newCol * 100

time_p2 = time.time() - start_time - time_p1
print("The solution to Part 2 is {} which took {:.4f} seconds to run".format(total[0], time_p2))
