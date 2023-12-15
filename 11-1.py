#advent of code day 11
import time
import csv
import os

start_time = time.time()

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

inputs = []
with open(os.path.join(__location__, "input-11-1.txt"),newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter='\n')
    for row in reader:
        inputs.append(row)

print(inputs)

#Generate list of coordinates of galaxies
galaxies = [[row,col] for row, line in enumerate(inputs) for col, value in enumerate(line[0]) if value == "#"]
rows = [item[0] for item in galaxies]
cols = [item[1] for item in galaxies]
cols.sort()

#Generate list of rows and columns which do not contain a single galaxy
empty_row = [row for row, line in enumerate(inputs) if "#" not in line[0]]
empty_col = [col for col in range(len(inputs[0][0])) if col not in cols]

print(empty_row, empty_col)

#Expand the Universe
def expand(rows, cols, galaxies, expansion_rate):
    #rows = empty rows
    #cols = empty cols
    #galaxies = locations of points of interest

    new_galaxies = []
    for galaxy in galaxies:
        row_g = galaxy[0]
        col_g = galaxy[1]
        for row in rows:
            if galaxy[0] > row:
                row_g += expansion_rate-1
        for col in cols:
            if galaxy[1] > col:
                col_g += expansion_rate-1
        new_galaxies.append([row_g, col_g])     

    return new_galaxies   

time_s = time.time() - start_time

expanded = expand(empty_row, empty_col, galaxies, 2)

total_path = 0
for ind, galaxy in enumerate(expanded):
    for ind2, galaxy2 in enumerate(expanded[ind+1::]):
        ind2 += ind+1
        total_path += abs(galaxy2[0]-galaxy[0]) + abs(galaxy2[1] - galaxy[1])
    
time_p1 = time.time() - start_time - time_s
print("The solution to Part 1 is {} which took {} seconds to run".format(total_path, time_p1))

#Part 2
expanded = expand(empty_row, empty_col, galaxies, 1000000)
total_path = 0
for ind, galaxy in enumerate(expanded):
    for ind2, galaxy2 in enumerate(expanded[ind+1::]):
        ind2 += ind+1
        total_path += abs(galaxy2[0]-galaxy[0]) + abs(galaxy2[1] - galaxy[1])
    
time_p2 = time.time() - start_time - time_p1
print("The solution to Part 2 is {} which took {} seconds to run".format(total_path, time_p2))